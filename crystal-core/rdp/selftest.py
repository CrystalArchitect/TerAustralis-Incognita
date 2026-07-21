"""Self-test for RDP — canonical JSON, the hash chain, and the decision kernel.

    python3 -m rdp.selftest

These tests *are* the specification. There is no external conformance suite for
RDP — the handoff that described one referred to reference files that never
existed — so correctness here means: the canonical form is deterministic and
matches the profile's stated rules, the hash chain detects any tampering, and
the decision kernel resolves every context through its fixed precedence order.
The empty-string SHA-256 is pinned as a fixed anchor so the hash primitive
itself can't drift underneath us.
"""

from __future__ import annotations

import json
from decimal import Decimal
from pathlib import Path

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
from .kernel import (
    ALLOW,
    DENY,
    ESCALATE,
    HOLD,
    REVIEW,
    RULE_BIAS,
    RULE_CONSTRAINT,
    RULE_DILEMMA,
    RULE_RISK,
    decide,
    decide_and_record,
    risk_band,
    risk_score,
    satisfiability,
    witness_bias,
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


def test_conformance_vectors():
    """vectors.json is the language-neutral interop contract — every entry must
    match the code exactly, so the published file can never drift from it."""
    path = Path(__file__).with_name("vectors.json")
    doc = json.loads(path.read_text(encoding="utf-8"))
    vectors = doc["vectors"]
    assert vectors, "vectors.json must not be empty"
    for v in vectors:
        obj = json.loads(v["input_json"], parse_float=Decimal, parse_int=int)
        got = canonical_serialize(obj)
        assert got == v["canonical"], (v["note"], got, v["canonical"])
        assert sha256_hex(got) == v["sha256"], (v["note"], sha256_hex(got))


# --- decision kernel -------------------------------------------------------

def test_risk_bands_and_boundaries():
    assert risk_band(0.0) == "LOW"
    assert risk_band(0.24) == "LOW"
    assert risk_band(0.25) == "GUARDED"      # boundary belongs to the higher band
    assert risk_band(0.5) == "ELEVATED"
    assert risk_band(0.75) == "SEVERE"
    assert risk_band(1.0) == "SEVERE"
    assert _raises(ValueError, risk_band, -0.1)
    assert _raises(ValueError, risk_band, 1.1)


def test_risk_score_normalization():
    assert risk_score(0.4) == 0.4
    assert risk_score([0.2, 0.3, 0.1]) == 0.6      # factors sum
    assert risk_score([0.9, 0.9]) == 1.0           # clamped to 1
    assert risk_score(-5) == 0.0                    # clamped to 0
    assert _raises(TypeError, risk_score, True)     # bool is not a risk number
    assert _raises(TypeError, risk_score, "high")


def test_satisfiability_and_dilemma():
    # a true dilemma: each obligation is met by some option, none by both
    sat, dil = satisfiability(["a", "b"], [
        {"id": "keep_promise", "satisfied_by": ["a"]},
        {"id": "prevent_harm", "satisfied_by": ["b"]},
    ])
    assert sat is False and dil is True
    # satisfiable: option 'a' meets both
    sat, dil = satisfiability(["a", "b"], [
        {"id": "x", "satisfied_by": ["a"]},
        {"id": "y", "satisfied_by": ["a", "b"]},
    ])
    assert sat is True and dil is False
    # an impossible single obligation is unsatisfiable but NOT a dilemma
    sat, dil = satisfiability(["a"], [{"id": "z", "satisfied_by": ["nonexistent"]}])
    assert sat is False and dil is False
    # no obligations at all is trivially satisfiable
    assert satisfiability(["a"], []) == (True, False)


def test_witness_bias_detection():
    assert witness_bias([]) == []
    assert witness_bias([{"id": "w1", "source": "a"}]) == []      # lone witness, no flag
    assert witness_bias([{"id": "w1", "source": "a", "biased": True}]) == ["flagged:w1"]
    # two witnesses, one source = monoculture
    reasons = witness_bias([{"id": "w1", "source": "a"}, {"id": "w2", "source": "a"}])
    assert reasons == ["single_source:a"]
    # independent sources = clean
    assert witness_bias([{"id": "w1", "source": "a"}, {"id": "w2", "source": "b"}]) == []


def test_decide_each_tier_in_isolation():
    # tier 1 — constraint violation
    v = decide({"constraints": [{"id": "no_coercion", "satisfied": False}]})
    assert v["outcome"] == DENY and v["rule"] == RULE_CONSTRAINT

    # tier 2 — unsatisfiable dilemma
    v = decide({"options": ["a", "b"], "obligations": [
        {"id": "p", "satisfied_by": ["a"]},
        {"id": "q", "satisfied_by": ["b"]},
    ]})
    assert v["outcome"] == ESCALATE and v["rule"] == RULE_DILEMMA

    # tier 3 — witness bias
    v = decide({"witnesses": [
        {"id": "w1", "source": "a"}, {"id": "w2", "source": "a"},
    ]})
    assert v["outcome"] == REVIEW and v["rule"] == RULE_BIAS

    # tier 4 — risk band, low and severe
    assert decide({"risk": 0.1})["outcome"] == ALLOW
    assert decide({"risk": 0.6})["outcome"] == HOLD
    assert decide({"risk": 0.9})["outcome"] == DENY
    assert decide({})["outcome"] == ALLOW              # empty context = zero-risk allow


def test_decide_precedence_is_strict():
    """A context that trips every tier must return the highest one, and peeling
    off each top tier reveals the next in exact order."""
    ctx = {
        "constraints": [{"id": "no_coercion", "satisfied": False}],
        "options": ["a", "b"],
        "obligations": [
            {"id": "p", "satisfied_by": ["a"]},
            {"id": "q", "satisfied_by": ["b"]},
        ],
        "witnesses": [{"id": "w1", "source": "a"}, {"id": "w2", "source": "a"}],
        "risk": 0.9,
    }
    assert decide(ctx)["rule"] == RULE_CONSTRAINT          # constraint wins over all
    ctx = {**ctx, "constraints": []}
    assert decide(ctx)["rule"] == RULE_DILEMMA             # then the dilemma
    ctx = {**ctx, "obligations": []}
    assert decide(ctx)["rule"] == RULE_BIAS                # then witness bias
    ctx = {**ctx, "witnesses": []}
    assert decide(ctx)["rule"] == RULE_RISK                # finally risk
    assert decide(ctx)["outcome"] == DENY                 # risk 0.9 → SEVERE → DENY


def test_decide_and_record_is_tamper_evident():
    chain = new_chain()
    decision = {"risk": 0.1, "constraints": [{"id": "ok", "satisfied": True}]}
    verdict = decide_and_record(chain, decision)
    assert verdict["outcome"] == ALLOW
    assert len(chain) == 1
    event = chain[0]
    assert event["kind"] == "rdp.verdict"
    # the recorded decision hash matches the canonical hash of the exact input
    assert event["decision_sha256"] == sha256_hex(decision)
    ok, broken = verify(chain)
    assert ok and broken == -1
    # editing the recorded reason breaks the chain
    tampered = [dict(e) for e in chain]
    tampered[0]["reason"] = "something else"
    ok, broken = verify(tampered)
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
        test_conformance_vectors,
        test_risk_bands_and_boundaries,
        test_risk_score_normalization,
        test_satisfiability_and_dilemma,
        test_witness_bias_detection,
        test_decide_each_tier_in_isolation,
        test_decide_precedence_is_strict,
        test_decide_and_record_is_tamper_evident,
        test_determinism_across_independent_chains,
    ]
    for t in tests:
        t()
        print(f"PASS {t.__name__}")
    print(f"\n{len(tests)}/{len(tests)} passed. The record remembers — and cannot be quietly rewritten.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
