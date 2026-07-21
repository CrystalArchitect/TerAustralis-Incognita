"""Adapters that record decisions from the pack's real consent gates onto an RDP
chain — the honest wiring sketched in RDP-INTEGRATION.md, made concrete.

The whole point is *clean separation*, so note what this module does NOT do:

  * It does not import ConsentGate, Starline, or any enforcement code.
  * It never decides anything. It accepts the *fields of a decision that has
    already been made* and turns them into a canonical, hash-chained record.

So the direction is strictly one-way and the coupling is zero: the gate enforces,
then (afterwards) hands the outcome here to be witnessed. If this recording
failed entirely, the gate's allow/deny would be unaffected — RDP is the ledger,
not the lock.

    from rdp.record import new_chain, verify
    from rdp.adapters import record_gate_decision

    chain = new_chain()
    result = gate.check(guest, tool, arguments)          # enforcement (elsewhere)
    record_gate_decision(                                # witnessing (here)
        chain,
        guest=guest, tool=tool,
        decision=result.decision, allowed=result.allowed, reason=result.reason,
        arguments=arguments, ts=now_iso8601(),
    )
"""

from __future__ import annotations

from typing import Any

from .canonical import sha256_hex
from .record import append

EVENT_KIND = "consent.gate.decision"


def gate_event(
    *,
    guest: str,
    tool: str,
    decision: str,          # "allow" | "refuse"
    allowed: bool,
    reason: str,
    ts: Any,                # caller-supplied timestamp (str or number) — never generated here
    arguments: dict[str, Any] | None = None,
    args_fingerprint: str | None = None,
) -> dict[str, Any]:
    """Build the canonical consent-decision event (does not append it).

    The tool arguments are recorded as a *fingerprint* — the canonical SHA-256 of
    the arguments — not as the raw payload. That keeps potentially-sensitive
    inputs out of the ledger while still letting anyone who holds the original
    arguments prove they match. Pass ``args_fingerprint`` yourself if you need a
    different hashing rule (see the note in RDP-INTEGRATION.md about numeric
    precision under the decimal-6 canonical profile).
    """
    if args_fingerprint is None and arguments is not None:
        args_fingerprint = sha256_hex(arguments)
    return {
        "kind": EVENT_KIND,
        "guest": guest,
        "tool": tool,
        "decision": decision,
        "allowed": bool(allowed),
        "reason": reason,
        "args_fingerprint": args_fingerprint or "",
        "ts": ts,
    }


def record_gate_decision(chain: list[dict[str, Any]], **fields: Any) -> dict[str, Any]:
    """Append a gate decision to *chain* and return the stamped event.

    Call this *after* the gate has decided — never before — so RDP can never sit
    between the gate and its own verdict. Takes the same keyword fields as
    ``gate_event``.
    """
    return append(chain, gate_event(**fields))


def _utc_now_iso() -> str:
    """Default clock — a UTC ISO-8601 timestamp. Injectable so tests stay
    deterministic (the canonical form must not depend on wall-clock)."""
    import datetime

    return datetime.datetime.now(datetime.timezone.utc).isoformat()


class recording_gate:
    """Wrap any consent gate so each decision is written to an RDP chain.

    This is the thin glue that keeps RDP a *ledger, not a lock*:

      * It does not import ConsentGate — it wraps any object whose ``check()``
        returns a result with ``.decision``, ``.allowed`` and ``.reason`` (the
        shape of CrystalBridge's ``GateResult``). Duck-typed on purpose.
      * On each call it lets the wrapped gate decide *first* (enforcement,
        unchanged), then records the outcome *after* the result exists. RDP never
        sits between the gate and its verdict — if the gate raises, nothing is
        recorded; if recording somehow failed, the allow/deny already stands.

    Timestamps come from *clock* (default: real UTC ISO-8601), injectable so the
    canonical record stays reproducible under test.

        gate = ConsentGate(config)                 # enforcement (CrystalBridge)
        chain = new_chain()
        gate = recording_gate(gate, chain)         # + witnessing (RDP)
        result = gate.check("hub-a", "recall", {"query": "x"})
        verify(chain)                              # (True, -1)
    """

    def __init__(self, gate: Any, chain: list[dict[str, Any]], *, clock: Any = _utc_now_iso):
        self._gate = gate
        self._chain = chain
        self._clock = clock

    def check(self, guest: str, tool: str, arguments: dict[str, Any] | None = None, **kw: Any) -> Any:
        result = self._gate.check(guest, tool, arguments, **kw)   # decide first
        record_gate_decision(                                     # then witness
            self._chain,
            guest=guest,
            tool=tool,
            decision=result.decision,
            allowed=result.allowed,
            reason=result.reason,
            arguments=arguments,
            ts=self._clock(),
        )
        return result
