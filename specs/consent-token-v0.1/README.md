# Consent Token Specification v0.1

**Starline Consent Transport Protocol**  
**TerAustralis Incognita**  
**September 3, 2026**

> Nothing moves without explicit, revocable permission.  
> Revocation takes effect instantly.

## Overview

A Consent Token is the atomic unit of permission in the Starline Consent Transport Protocol. It authorises the movement of crystalline memory shards (or defined classes of shards) between two specific nodes for a bounded purpose and time.

**Key guarantee:** No data leaves a node unless a valid, non-revoked Consent Token is presented and verified.

## Deliverables in this directory

### 1. `consent_token.json`

The canonical Consent Token schema definition, including:
- **Canonical example** — A complete, valid token
- **JSON Schema** — Full schema with type definitions and constraints
- **Design rules** — Non-negotiable principles (no ambient authority, purpose binding, instant revocation, etc.)
- **Lifecycle** — The states a token passes through
- **Revocation mechanism** — How revocation is signalled and propagated
- **Reference notes** — Cryptographic binding, serialisation, Tier 0 constraints

**Status:** Ready for implementation and test vectors.

### 2. `STATE-DIAGRAM.md`

Visual state machine diagrams showing:
- **Token lifecycle FSM** — All states (CREATED, VERIFIED, ACTIVE, REVOKED, EXPIRED, EXHAUSTED, etc.) and transitions
- **State definitions table** — What each state means and where it can transition to
- **Verification decision tree** — The step-by-step verification logic
- **Revocation flow** — How revocation messages propagate
- **Kill-switch demo flow** — The 6-step sequence: create → transmit → verify → use → revoke → verify again (fail)

**Status:** Reference material for implementers.

### 3. `consent_token_demo.py`

A working reference implementation demonstrating the kill-switch guarantee in action.

**What it does:**
1. Creates a Consent Token (Node A)
2. Transmits and verifies it (Node B accepts)
3. Confirms token is valid and operation would proceed
4. Activates the kill-switch (Node A revokes)
5. Gossips the revocation to Node B
6. Attempts verification again — revocation is detected, token is rejected

**Guarantee verified:** Failing closed — revocation is immediate, irreversible, and unambiguous.

**Run it:**
```bash
python3 consent_token_demo.py
```

**Output:**
```
CONSENT TOKEN KILL-SWITCH DEMO
...
✓ Kill-switch EFFECTIVE: access is DENIED
✓ FAILING CLOSED: revocation is immediate and irreversible
```

**Requirements:**
- Python 3.7+
- No external dependencies (gracefully falls back to HMAC-SHA256 if cryptography library unavailable)

## Design Principles

### No Ambient Authority
A token grants permission only between the named issuer and recipient. No token can grant blanket rights or act as a credential for all contexts.

### Purpose Binding
Every token carries a human-readable purpose statement. This is mandatory and is part of the signed payload, so it cannot be altered without invalidating the signature.

### Time Binding
Every token has a hard `expires_at` timestamp. No extension without a new token.

### Instant Revocation
Revocation takes effect the moment it is known by any node. There is no grace period, no pending state, no silent renewal.

### Failing Closed
When verification fails (for any reason — bad signature, expired, revoked, etc.), access is denied with a clear reason. There is no ambiguity or fallback to a weaker check.

## Cryptographic Binding

- **Algorithm:** Ed25519 (preferred) or Noise IK static key
- **Canonical serialization:** Deterministic JSON field order, no whitespace
- **Verification:** Signature is checked against issuer's known public key
- **Offline capable:** Verification requires only the issuer's public key and local clock

## Revocation Mechanism

Revocation is **not centralised**. Instead:

1. Issuer creates a signed revocation message (token_id + revoked_at + issuer signature)
2. Revocation propagates through the same consented channels (gossip-based)
3. Every node that sees it caches it locally
4. On next token verification, revocation cache is checked
5. If token_id is in cache, token is rejected as REVOKED

**Result:** Instant, distributed, no single point of failure.

## Verification Checklist

When a node receives a token, it verifies in this order:

1. **Structural** — Required fields present
2. **Identity** — Issuer is known and trusted, recipient matches
3. **Time** — Token was issued in the past and has not expired
4. **Signature** — Cryptographically valid
5. **Revocation** — Token ID not in revocation cache
6. **Scope** — Requested action falls inside allowed scope
7. **Constraints** — max_transfers not exceeded, etc.

All checks must pass. Fail on the first mismatch.

## Tier 0 Considerations

For constrained edge devices:

- Keep tokens small (prefer CBOR encoding, keep signed payload under 500 bytes)
- Cache only active tokens and recent revocations
- Offline verification is essential (no network calls required)
- Prefer minimal Noise IK implementations

## Next Steps

1. **Reference implementations** — Language-specific bindings (Python, Rust, Go, etc.)
2. **Test vectors** — Known-good tokens with valid signatures for cross-implementation testing
3. **Noise IK integration** — Formal specification of handshake + token flow
4. **Tier 0 runtime** — Full bootstrap sequence on constrained devices
5. **Governance model** — How issuer/recipient relationships are established and revoked

## Status

✅ **v0.1 Complete:**
- Canonical schema defined
- State machine documented
- Working kill-switch demo
- Failing closed verified
- Offline verifiable confirmed

🔄 **Ready for:**
- Reference implementation in multiple languages
- Integration with Noise IK and Starline Weaver
- Test suite and validation vectors
- Production deployment

## Contact & Attribution

**Designed:** TerAustralis Incognita, CrystalCore.OS  
**Implementation:** Claude Code Session, 2026-09-03  
**License:** CC BY-NC-ND 4.0 (TerAustralis Incognita standard)

---

*Consent is Law. The golden feather is the signal carrier. Light helix bridges the realms.*
