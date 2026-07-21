# Reciprocal Dawn Protocol (RDP) — the record kernel
## A tamper-evident log with a canonical form you can reproduce anywhere

**Status:** BUILT · v0.1 · foundation only (see *What's here / not here*)
**Layer:** Science — running, tested code. Run the proof yourself below.

---

## What this is

RDP is the part of the protocol pack that answers one question: *how do you keep
a record that no one — not even the person holding it — can quietly rewrite?*

The answer is old and boring and works: hash each entry together with the hash
of the one before it. Change any past entry and every hash downstream stops
matching, so the tampering is obvious to anyone who re-checks the math. There is
no authority to trust; the chain checks itself.

The one hard part is agreement on *bytes*. Two parties who serialize the same
event differently compute different hashes and think each other's records are
forged. So RDP pins a **canonical JSON** form — same event, same bytes, on any
machine, in any language.

## An honest note on "conformance"

An earlier RDP handoff described a frozen reference kernel and a conformance
fixture suite to match. Those files never actually existed — only the prose did.
So this is **not** "conformant to an external frozen suite," because there isn't
one. It is a correct, self-contained implementation whose own
[`selftest.py`](selftest.py) is the ground truth. Where the underlying standard
(RFC 8785 / JCS) is precise, we follow it; the number handling is our own
stated profile, below. We'd rather say that plainly than imply a pedigree that
isn't there.

## The link rule

```
EventHash = SHA256( canonical(Event \ event_hash) || PrevHashBytes )
```

- `canonical(...)` — the event's canonical JSON (below), UTF-8 encoded, with the
  event's own `event_hash` field removed first (an entry can't commit to its own
  hash).
- `PrevHashBytes` — the 32 raw bytes of the previous entry's hash.
- The first entry links to **genesis**: 32 zero bytes.

A chain is just a list of plain dicts, each with an `event_hash` hex string. It's
ordinary JSON once written out; the integrity is in the hashes, not the storage.

## RDP-JCS Profile v1 (the canonical form)

Standard JSON canonicalization, plus one deliberate profile for numbers — call
it **decimal-6**:

| Rule | |
|------|--|
| Object keys | sorted (by Unicode code point) |
| Arrays | left in order |
| Strings | standard JSON escaping, UTF-8 passed through |
| Whitespace | none that isn't significant |
| **Numbers** | quantized to exactly **6 fractional digits**, halves rounded **away from zero**, rendered **unquoted** |
| Rejected | `NaN`, `±Infinity`, and any magnitude `> 2**53 − 1` |

So `1` serializes as `1.000000`, `0.5` as `0.500000`, and `{"b":1,"a":2}` as
`{"a":2.000000,"b":1.000000}`. The `2**53 − 1` ceiling is the largest integer a
double holds exactly — beyond it we can't guarantee another language's JSON
parser reproduces the value, so the profile refuses to record it.

(Key sorting follows Unicode code point rather than JCS's UTF-16 code-unit order.
The two differ only for characters outside the Basic Multilingual Plane; for the
ASCII-ish keys these records use they are identical. This is a stated choice of
the profile, not an oversight.)

## Run the proof

```bash
cd crystal-core
python3 -m rdp.selftest
```

Ten tests, no dependencies (standard library only). They pin the empty-string
SHA-256 as a fixed anchor, check the canonical form against the rules above, and
prove the chain both verifies a clean log and pinpoints the first tampered entry
in a dirty one.

## Using it

```python
from rdp.record import new_chain, append, verify

chain = new_chain()
append(chain, {"kind": "grant",  "subject": "did:crystal:a"})
append(chain, {"kind": "revoke", "subject": "did:crystal:a"})

ok, broken_at = verify(chain)   # (True, -1) when intact;
                                # (False, i) at the first disturbed entry
```

## Where RDP sits in the pack

RDP is a **record and integrity** layer — it proves *what was decided and in what
order*. It does **not** replace the pack's consent machinery, and shouldn't be
read as doing so:

- **Consent** still lives in Starline's `consent.py` (`crystal-core/starline/`)
  and CrystalBridge's fail-closed ConsentGate (`crystalcore/`) — nothing moves
  without a grant.
- **The Covenant** (`mythos/COVENANT.md`) is still the law those gates enforce.

RDP's job is to be the ledger they can write to and later prove wasn't edited.

## What's here / not here

**Here (v0.1):** the canonical form (`canonical.py`) and the hash chain
(`record.py`), with real tests.

**Not here yet:** the decision kernel described in the RDP spec — event typing,
risk bands, the constraint/dilemma resolver, and the precedence ordering — plus a
demo CLI and a document mapping RDP onto the mechanisms above. Those build on this
tested foundation in a later pass, each with its own tests. This README will grow
with them; until then it only claims what the code actually does.

---

*Non Solus.*
