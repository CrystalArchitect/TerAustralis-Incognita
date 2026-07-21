"""Watch the RDP decision kernel work — every precedence tier, recorded.

    python3 -m rdp.run demo

Runs five decisions, one per precedence tier plus a clean allow, printing the
verdict and which rule decided it. Each decision is written to a single
hash-chained record; at the end the chain is verified, and then one entry is
tampered with to show the verification catch it. Nothing here is simulated —
it calls the same `decide` and `record` code the tests cover.
"""

from __future__ import annotations

import argparse

from .kernel import decide_and_record
from .record import new_chain, verify

# Five decision contexts, chosen so each precedence tier fires in turn.
CASES = [
    ("clean, low risk", {
        "risk": 0.1,
        "constraints": [{"id": "consent_present", "satisfied": True}],
    }),
    ("elevated risk", {
        "risk": [0.3, 0.3],  # factors sum to 0.6 → ELEVATED → HOLD
    }),
    ("single-source evidence", {
        "witnesses": [
            {"id": "w1", "source": "hub-a"},
            {"id": "w2", "source": "hub-a"},
        ],
    }),
    ("an unsatisfiable dilemma", {
        "options": ["keep_promise", "prevent_harm"],
        "obligations": [
            {"id": "promise", "satisfied_by": ["keep_promise"]},
            {"id": "safety", "satisfied_by": ["prevent_harm"]},
        ],
    }),
    ("a broken hard constraint", {
        "constraints": [{"id": "no_coercion", "satisfied": False}],
        "risk": 0.9,  # would be DENY on risk too, but the constraint decides first
    }),
]


def demo() -> None:
    chain = new_chain()
    print("RDP decision kernel — precedence: constraint > dilemma > bias > risk\n")
    for label, ctx in CASES:
        verdict = decide_and_record(chain, ctx)
        print(f"  {label:26} → {verdict['outcome']:8} [{verdict['rule']}]")
        print(f"  {'':26}   {verdict['reason']}")

    print(f"\nRecorded {len(chain)} verdicts to a hash-chained log.")
    ok, broken = verify(chain)
    print(f"verify() → intact={ok}" + ("" if ok else f", first break at {broken}"))

    print("\nNow tamper with the first recorded verdict's reason...")
    tampered = [dict(e) for e in chain]
    tampered[0]["reason"] = "quietly changed"
    ok, broken = verify(tampered)
    print(f"verify() → intact={ok}, first break at index {broken}")

    print("\nEvery verdict explains itself, and the record cannot be edited unseen.")
    print("Non Solus.")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="RDP decision kernel demo")
    parser.add_argument("command", choices=["demo"], nargs="?", default="demo")
    parser.parse_args(argv)
    demo()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
