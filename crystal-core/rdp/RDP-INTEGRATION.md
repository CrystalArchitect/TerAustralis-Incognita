# RDP and the consent gates — how they relate

**Read this if you've heard RDP called a "governance layer."** It isn't one, and
this doc is here to say so precisely, then show how RDP *does* relate to the
parts of the project that actually govern anything.

## What RDP is, and is not

RDP is a **record + decision kernel**:

- a canonical form (`canonical.py`) and a tamper-evident hash chain (`record.py`),
- a deterministic decision engine (`kernel.py`) that resolves a context to one
  explainable verdict through a fixed precedence order.

RDP is **not**:

- **not a consent enforcer.** It does not hold grants, check permissions, or
  block anything. It has no authority over any action.
- **not a governance layer.** It governs nothing. It decides — deterministically,
  when handed a context — and it records.

The things that *do* enforce consent in this project are already built, and they
are separate from RDP:

| Mechanism | Where | What it does |
|---|---|---|
| **CrystalBridge ConsentGate** | [`crystalcore/gate.py`](../../crystalcore/gate.py) | Fail-closed gate; four checks in order — approval → permission → scope → provenance. Every decision audited ([`crystalcore/audit.py`](../../crystalcore/audit.py)). |
| **Starline consent** | [`starline/consent.py`](../starline/consent.py) | Signed `ConsentReceipt`s; `is_granted()`. Revocation stops *future* requests at once; it cannot retract data a peer already holds, and says so. |
| **The Covenant** | [`../../mythos/COVENANT.md`](../../mythos/COVENANT.md) | The five commitments those gates exist to keep. |

**These are separate modules today.** What follows is *correspondence* — how the
gates' logic lines up with RDP's — and possible future composition. It is **not**
a description of an existing wiring. Nothing currently feeds RDP from the gates.

## Why they correspond

The gates and RDP's kernel share a shape, because they answer the same kind of
question the same way: **legitimacy before prudence, and fail closed.**

- ConsentGate is fail-closed: any failing check refuses, and refusal is the
  default. That is exactly RDP's **tier 1** — a violated hard constraint ends the
  decision with `DENY`, and it outranks every softer consideration below it.
- The Covenant's absolute pause and "no influence without direction" are not
  risk trade-offs; they're hard limits. In RDP terms they are **constraints**, not
  risk inputs — a `HOLD`/`DENY` that no amount of low risk can override.
- "Support is offered, never imposed" is the shape of RDP's **`ESCALATE`/`HOLD`**:
  when acting unbidden would be overreach, the right move is to stop and hand the
  choice back, not to proceed.

So ConsentGate is, in effect, a concrete instance of RDP's constraint tier; a
Starline grant/revocation is a signed record of the kind RDP's chain is built to
hold; the Covenant is the source of the constraints themselves.

## Worked examples

Each of these is real — run them yourself; the verdicts below are the actual
output of `rdp.kernel`, not illustrations.

**1 — a ConsentGate refusal (guest not approved).** The gate's failing `approval`
check becomes an unsatisfied constraint:

```python
from rdp.kernel import decide
decide({"constraints": [{"id": "gate.approval", "satisfied": False}]})
# → {'outcome': 'DENY', 'rule': 'constraint_violation', ...}
```

**2 — a Starline request after revocation.** `is_granted() == False` is a
constraint violation:

```python
decide({"constraints": [{"id": "starline.consent_granted", "satisfied": False}]})
# → {'outcome': 'DENY', 'rule': 'constraint_violation', ...}
```

**3 — a clean action, consent present, low risk.** No constraint broken, so the
decision falls through to the risk tier:

```python
decide({
    "constraints": [
        {"id": "gate.approval",             "satisfied": True},
        {"id": "starline.consent_granted",  "satisfied": True},
    ],
    "risk": 0.1,
})
# → {'outcome': 'ALLOW', 'rule': 'risk_band', ...}
```

**Recording it.** Any of these can be written to a tamper-evident chain:

```python
from rdp.record import new_chain, verify
from rdp.kernel import decide_and_record

chain = new_chain()
decide_and_record(chain, {"constraints": [{"id": "gate.approval", "satisfied": False}]})
verify(chain)   # (True, -1) — intact; chain[0]["kind"] == "rdp.verdict"
```

## Wiring a real gate to the chain — the adapter

The correspondence above is now backed by a small, decoupled adapter:
[`adapters.py`](adapters.py). It is the honest minimum — nothing in `gate.py` or
`consent.py` imports RDP, and `adapters.py` imports neither of them. The gate
enforces; afterwards it hands the *outcome* to the adapter to be witnessed.

**What gets written.** When a `ConsentGate.check()` returns a `GateResult`, the
adapter records one canonical event per decision:

```python
from rdp.record import new_chain, verify
from rdp.adapters import record_gate_decision

chain = new_chain()
result = gate.check(guest, tool, arguments)      # enforcement — unchanged, elsewhere
record_gate_decision(                            # witnessing — after the fact
    chain,
    guest=guest, tool=tool,
    decision=result.decision, allowed=result.allowed, reason=result.reason,
    arguments=arguments, ts="2026-07-21T10:00:00Z",
)
# chain[-1] == {"kind": "consent.gate.decision", "guest", "tool", "decision",
#               "allowed", "reason", "args_fingerprint", "ts", "event_hash"}
verify(chain)   # (True, -1) — and it pinpoints the first tampered decision if not
```

The **arguments are stored as a fingerprint** (`sha256_hex` of the canonical
arguments), never the raw payload — so a consent input that carries sensitive
data doesn't leak into the ledger, while anyone holding the original arguments
can still prove they match.

**Keeping the separation clean.** The adapter is called *after* the gate decides
and can never sit between the gate and its verdict. If recording failed
entirely, the allow/deny would stand unchanged — RDP is the ledger, not the lock.
That's the whole design: two policies are available depending on how strong a
guarantee you want —

- *Best-effort audit* (what the adapter does): record after enforcing; a record
  failure is logged, not fatal. The gate stays independent.
- *Mandatory witness* ("no action without a recorded decision"): append first and
  treat an append failure as a refuse. Stronger, but it couples the two — a
  deliberate choice, not the default.

**Edge cases that matter once real consent events flow:**

- **Numeric precision.** The RDP-JCS profile quantizes numbers to 6 decimals, so
  the `args_fingerprint` collapses differences below 1e-6. Fine for string/ID
  arguments; if an argument carries values that must be bit-exact, pass your own
  `args_fingerprint` computed with a non-quantizing serialization.
- **JSON-only inputs.** Canonicalization rejects non-string keys and non-JSON
  types (`bytes`, `datetime`, …). Normalize arguments to JSON-safe values before
  recording, or `gate_event` will raise — which is honest, but must be handled.
- **Concurrency.** The chain is linear and `append` reads-the-tip-then-writes, so
  it is **not** thread-safe. Serialize appends (one writer, or a lock) when a live
  gate is deciding concurrently, or the tip will race.
- **Timestamps are data, supplied by the caller** — the adapter never generates
  them, so the canonical form stays deterministic and reproducible.
- **Revocation.** A Starline `ConsentReceipt` (signed grant *or* revoke) records
  the same way; the signature is a string and rides through canonicalization
  untouched, so the chain proves the exact grant→revoke sequence.

There is no "governance," no "firewall," and no mythic framing in any of this.
RDP records and decides; the gates enforce; the Covenant is the law they keep.

---

*Non Solus.*
