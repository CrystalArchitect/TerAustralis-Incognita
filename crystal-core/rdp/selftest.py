"""Self-test for the RDP record kernel — canonical JSON + the hash chain.

    python3 -m rdp.selftest

These tests *are* the specification. There is no external conformance suite for
RDP — the handoff that described one referred to reference files that never
existed — so correctness here means: the canonical form is deterministic and
matches the profile's stated rules, and the hash chain detects any tampering.
The empty-string SHA-256 is pinned as a fixed anchor so the hash primitive
itself can't drift underneath us.
"""

from __future__ import annotations

from decimal import Decimal

from .canonical import (
    MAX_MAGNITUDE,
    canonical_serialize,
    quantize6,
    render_number,
    sha256_hex,
)
from .record import (
    GENESIS_PREV,
    append,
    compute_event_hash,
    new_chain,
    tip_bytes,
    verify,
)

# SHA-256 of the empty string — a value anyone can look up. If this ever fails,
# the hashing itself is wrong, not the protocol.
EMPTY_SHA256 = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"


def _raises(exc, fn, *args) -> bool:
    try:
        fn(*args)
    except exc:
        return True
    return False


def test_empty_string_sha256_anchor():
    assert sha256_hex("") == EMPTY_SHA256
    assert sha256_hex(b"") == EMPTY_SHA256


def test_object_keys_are_sorted():
    assert canonical_serialize({"b": 1, "a": 2}) == '{"a":2.000000,"b":1.000000}'
    # insertion order must not matter
    one = canonical_serialize({"a": 1, "b": 2, "c": 3})
    two = canonical_serialize({"c": 3, "b": 2, "a": 1})
    assert one == two == '{"a":1.000000,"b":2.000000,"c":3.000000}'


def test_number_rendering():
    assert render_number(1) == "1.000000"
    assert render_number(0.5) == "0.500000"
    assert render_number(Decimal("0.5")) == "0.500000"
    # halves round away from zero
    assert render_number(Decimal("0.0000005")) == "0.000001"
    assert render_number(Decimal("-0.0000005")) == "-0.000001"
    # negative zero collapses to the single canonical zero
    assert render_number(Decimal("-0")) == "0.000000"
    assert render_number(-0.0) == "0.000000"
    # the largest allowed magnitude renders in plain (non-exponent) form
    assert render_number(MAX_MAGNITUDE) == "9007199254740991.000000"


def test_quantize6_rejects_unrepresentable():
    assert _raises(ValueError, quantize6, float("nan"))
    assert _raises(ValueError, quantize6, float("inf"))
    assert _raises(ValueError, quantize6, Decimal("NaN"))
    assert _raises(ValueError, quantize6, Decimal("Infinity"))
    assert _raises(ValueError, quantize6, MAX_MAGNITUDE + 1)          # 2**53
    assert _raises(ValueError, quantize6, -(MAX_MAGNITUDE + 1))
    # the boundary value itself is allowed
    assert quantize6(MAX_MAGNITUDE) == Decimal("9007199254740991.000000")


def test_booleans_and_null_are_not_numbers():
    assert canonical_serialize(True) == "true"
    assert canonical_serialize(False) == "false"
    assert canonical_serialize(None) == "null"
    assert canonical_serialize({"ok": True, "n": None}) == '{"n":null,"ok":true}'


def test_nested_structure_is_canonical():
    obj = {"z": [3, 1, 2], "a": {"n": None, "m": "hi"}}
    assert canonical_serialize(obj) == (
        '{"a":{"m":"hi","n":null},"z":[3.000000,1.000000,2.000000]}'
    )


def test_genesis_link():
    chain = new_chain()
    assert tip_bytes(chain) == GENESIS_PREV
    stamped = append(chain, {"kind": "grant", "subject": "did:crystal:a"})
    # the first event must link to the 32-zero genesis previous-hash
    body = {"kind": "grant", "subject": "did:crystal:a"}
    assert stamped["event_hash"] == compute_event_hash(body, GENESIS_PREV).hex()


def test_append_does_not_mutate_caller_and_ignores_incoming_hash():
    chain = new_chain()
    original = {"kind": "grant", "event_hash": "deadbeef"}
    stamped = append(chain, original)
    # caller's dict untouched
    assert original["event_hash"] == "deadbeef"
    # stored hash is the real computed one, not the incoming placeholder
    assert stamped["event_hash"] != "deadbeef"
    ok, broken = verify(chain)
    assert ok and broken == -1


def test_chain_verifies_and_detects_tampering():
    chain = new_chain()
    for i in range(3):
        append(chain, {"kind": "note", "n": i})
    ok, broken = verify(chain)
    assert ok and broken == -1

    # tamper with the *content* of the middle event
    tampered = [dict(e) for e in chain]
    tampered[1]["n"] = 99
    ok, broken = verify(tampered)
    assert not ok and broken == 1

    # tamper with only the *stored hash* of the first event
    tampered2 = [dict(e) for e in chain]
    tampered2[0]["event_hash"] = "00" * 32
    ok, broken = verify(tampered2)
    assert not ok and broken == 0


def test_determinism_across_independent_chains():
    events = [
        {"kind": "grant", "subject": "did:crystal:a", "amount": 12.5},
        {"kind": "revoke", "subject": "did:crystal:a"},
        {"kind": "note", "text": "sovereignty holds"},
    ]
    a = new_chain()
    b = new_chain()
    for e in events:
        append(a, dict(e))
        append(b, dict(e))
    assert [e["event_hash"] for e in a] == [e["event_hash"] for e in b]
    assert tip_bytes(a) == tip_bytes(b)


def main() -> int:
    tests = [
        test_empty_string_sha256_anchor,
        test_object_keys_are_sorted,
        test_number_rendering,
        test_quantize6_rejects_unrepresentable,
        test_booleans_and_null_are_not_numbers,
        test_nested_structure_is_canonical,
        test_genesis_link,
        test_append_does_not_mutate_caller_and_ignores_incoming_hash,
        test_chain_verifies_and_detects_tampering,
        test_determinism_across_independent_chains,
    ]
    for t in tests:
        t()
        print(f"PASS {t.__name__}")
    print(f"\n{len(tests)}/{len(tests)} passed. The record remembers — and cannot be quietly rewritten.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
