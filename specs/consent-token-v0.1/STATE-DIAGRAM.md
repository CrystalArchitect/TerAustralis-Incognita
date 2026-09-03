# Consent Token State Diagram

## Finite State Machine: Token Lifecycle

```
                              ┌─────────────────┐
                              │    UNISSUED     │
                              └────────┬────────┘
                                       │
                                       │ issuer.create_token()
                                       ↓
                    ┌──────────────────────────────────────┐
                    │          CREATED (SIGNED)             │
                    │ - token_id assigned                   │
                    │ - signature computed                  │
                    │ - issued_at = now                     │
                    │ - expires_at = future                 │
                    │ - revocation_endpoint set             │
                    └──┬──────────────────┬─────────────────┘
                       │                  │
                       │                  │ validation fails
                       │                  ↓
                       │         ┌─────────────────┐
                       │         │    INVALID      │
                       │         │ (never verified)│
                       │         └─────────────────┘
                       │
                       │ transmit via Noise IK
                       ↓
        ┌──────────────────────────────────┐
        │    RECEIVED (PENDING VERIFY)     │
        │ - in transit or at destination   │
        │ - no verification yet            │
        └──┬──────────────────┬────────────┘
           │                  │
           │ verify OK        │ verify fails
           ↓                  ↓
┌──────────────────┐  ┌─────────────────┐
│  VERIFIED/ACTIVE │  │    REJECTED     │
│ - signature OK   │  │ (bad signature, │
│ - time OK        │  │  expired, etc)  │
│ - scope OK       │  └─────────────────┘
│ - not revoked    │
└──┬──┬──┬─────────┘
   │  │  │
   │  │  └────────┬───────────────────────┐
   │  │           │                       │
   │  │      max_transfers              one_time_use
   │  │      reached?                   triggered?
   │  │           │                       │
   │  │           ↓                       ↓
   │  │      ┌────────────┐          ┌─────────┐
   │  │      │ EXHAUSTED  │          │ CONSUMED│
   │  │      └────────────┘          └─────────┘
   │  │
   │  └──── use (within scope)
   │        │
   │        ↓
   │    [operation proceeds]
   │
   │ issuer sends revocation message
   │
   └────────────┬──────────────────────────┐
                │                          │
                ↓                          │
        ┌──────────────────┐               │
        │     REVOKED      │ ◄─────────────┘
        │ - signature OK   │
        │ - revocation OK  │
        │ - immediate      │
        └──────────────────┘


    expires_at reached?
            │
            ↓ (from ACTIVE, VERIFIED, REVOKED, etc)
    ┌──────────────────┐
    │     EXPIRED      │
    │ (wall clock >    │
    │  expires_at)     │
    └──────────────────┘
```

## State Definitions

| State | Valid | Description | Next States |
|-------|-------|-------------|------------|
| **UNISSUED** | — | Token concept exists but not yet signed | CREATED |
| **CREATED** | ✓ | Signed and ready to transmit | RECEIVED, INVALID |
| **RECEIVED** | ✓ | Arrived at recipient, pending verification | VERIFIED, REJECTED |
| **VERIFIED/ACTIVE** | ✓ | Signature, time, scope, revocation all OK | EXHAUSTED, CONSUMED, REVOKED, EXPIRED |
| **REJECTED** | ✗ | Failed verification (any reason) | — |
| **INVALID** | ✗ | Never passed verification | — |
| **REVOKED** | ✗ | Issuer sent revocation, immediate | — |
| **EXPIRED** | ✗ | Wall clock exceeded expires_at | — |
| **EXHAUSTED** | ✗ | max_transfers reached | — |
| **CONSUMED** | ✗ | one_time_use constraint triggered | — |

## Verification Decision Tree

```
Token received?
    ↓
    ├─ NO → state = UNISSUED
    └─ YES → Perform verification checks:
        ├─ Required fields present?
        │   NO → REJECTED
        │   YES ↓
        ├─ Structural validity (JSON, types)?
        │   NO → REJECTED
        │   YES ↓
        ├─ Identity binding OK?
        │   (issuer known, recipient matches)
        │   NO → REJECTED
        │   YES ↓
        ├─ Time binding OK?
        │   (issued_at ≤ now < expires_at)
        │   NO → REJECTED (or EXPIRED if now > expires_at)
        │   YES ↓
        ├─ Signature valid?
        │   (Ed25519 verify against issuer pubkey)
        │   NO → REJECTED
        │   YES ↓
        ├─ Revocation check?
        │   (token_id in revocation cache?)
        │   YES → REVOKED
        │   NO ↓
        ├─ Scope check OK?
        │   (requested action within scope)
        │   NO → REJECTED
        │   YES ↓
        └─ Constraints OK?
            (max_transfers not exceeded, etc)
            NO → REJECTED or EXHAUSTED
            YES → VERIFIED/ACTIVE
```

## Revocation Flow

```
┌─────────────────┐
│ ACTIVE/VERIFIED │ (any point in lifecycle)
└────────┬────────┘
         │
         │ issuer.revoke(token_id)
         ↓
┌──────────────────────────┐
│ Revocation message sent  │
│ (signed by issuer)       │
└────────┬─────────────────┘
         │
         ├─ gossip through consented channels
         ├─ cached at every node that sees it
         │
         ├─ On next verification:
         │   token_id in cache?
         │   YES → state = REVOKED
         │   (immediate rejection)
         │
         └─ No central revocation list
            (distributed, gossip-based)
```

## Kill-Switch Demo Flow

```
1. CREATE TOKEN
   ↓
   issue_token(
     issuer="node_A",
     recipient="node_B",
     purpose="test transfer",
     expires_at=now+5min
   )
   ↓
   state = CREATED (SIGNED)

2. TRANSMIT & VERIFY
   ↓
   recipient receives token
   ↓
   verify_token(token, issuer_pubkey)
   ↓
   state = VERIFIED/ACTIVE ✓

3. ATTEMPT USE
   ↓
   check_token_valid(token_id)
   ↓
   ✓ ALLOWED (all checks pass)

4. REVOKE (KILL-SWITCH)
   ↓
   issuer.revoke(token_id)
   ↓
   state = REVOKED (immediate)

5. VERIFY AGAIN (AFTER REVOCATION)
   ↓
   verify_token(token, issuer_pubkey)
   ↓
   check revocation cache
   ↓
   token_id found in cache
   ↓
   state = REVOKED
   ✗ REJECTED (no ambiguity: failing closed)
```

## Guarantee: Failing Closed

When a token is revoked:
- Revocation is **immediate** — takes effect the moment it is seen
- **No extension** — revocation cannot be undone
- **No ambiguity** — verification fails with clear "REVOKED" reason
- **No silent grace period** — verification check catches it

This is the kill-switch guarantee: once triggered, no action proceeds under that token.
