#!/usr/bin/env python3
"""
Consent Token Kill-Switch Demo
Starline Consent Transport Protocol v0.1

Demonstrates:
1. Creating a consent token
2. Signing it cryptographically
3. Verifying its signature and state
4. Revoking it via kill-switch
5. Verifying that revocation fails the token (failing closed)

Run: python3 consent_token_demo.py
"""

import json
import uuid
import hashlib
import hmac
import sys
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, asdict


# Try to import Ed25519, but don't fail if unavailable
HAS_ED25519 = False
ed25519 = None
try:
    try:
        from cryptography.hazmat.primitives.asymmetric import ed25519 as ed25519_module
        from cryptography.hazmat.primitives import serialization
        ed25519 = ed25519_module
        HAS_ED25519 = True
    except Exception:
        # If cryptography fails for any reason, skip it
        pass
except:
    pass


@dataclass
class RevocationRecord:
    """A revocation record that gets gossiped through the network"""
    token_id: str
    revoked_at: str
    issuer: str
    issuer_signature: str  # Signature over the revocation itself


class ConsentTokenManager:
    """Minimal reference implementation for consent token lifecycle"""

    def __init__(self, node_id: str, private_key=None):
        self.node_id = node_id

        # Generate or use provided keypair
        if private_key is None:
            if HAS_ED25519:
                self.private_key = ed25519.Ed25519PrivateKey.generate()
                self.public_key = self.private_key.public_key()
            else:
                # Fallback: mock keys for demo purposes
                self.private_key = f"mock_private_key_{node_id}"
                self.public_key = f"mock_public_key_{node_id}"
        else:
            self.private_key = private_key
            self.public_key = private_key.public_key() if HAS_ED25519 else f"mock_public_key_{node_id}"

        # Local revocation cache (gossip-propagated in real system)
        self.revocation_cache: Dict[str, RevocationRecord] = {}

    def create_token(
        self,
        recipient: str,
        purpose: str,
        expires_in_seconds: int = 300,
        shard_ids: Optional[List[str]] = None,
        shard_class: str = "memory",
    ) -> Dict[str, Any]:
        """Create and sign a consent token"""

        now = datetime.utcnow()
        expires_at = now + timedelta(seconds=expires_in_seconds)

        token_data = {
            "version": "0.1",
            "token_id": str(uuid.uuid4()),
            "issuer": self.node_id,
            "recipient": recipient,
            "purpose": purpose,
            "scope": {
                "shard_ids": shard_ids or [],
                "shard_class": shard_class,
                "max_bytes": 8192,
            },
            "issued_at": now.isoformat() + "Z",
            "expires_at": expires_at.isoformat() + "Z",
            "revocable": True,
            "revocation_endpoint": f"{self.node_id}/revocation",
            "constraints": {
                "one_time_use": False,
                "requires_ack": True,
                "max_transfers": 1,
            },
        }

        # Compute signature
        canonical_json = self._canonical_serialize(token_data)
        signature = self._sign(canonical_json)
        token_data["signature"] = signature

        return token_data

    def verify_token(self, token: Dict[str, Any], issuer_public_key=None) -> tuple[bool, str]:
        """
        Verify a token locally.

        Returns: (is_valid, reason)
        - is_valid=True means token can be used
        - is_valid=False means token is rejected (and why)
        """

        try:
            # 1. Structural check
            required = ["version", "token_id", "issuer", "recipient", "purpose",
                       "scope", "issued_at", "expires_at", "signature"]
            if not all(field in token for field in required):
                return False, "REJECTED: missing required fields"

            # 2. Identity binding
            if token["issuer"] not in self.get_trusted_issuers():
                return False, f"REJECTED: unknown issuer {token['issuer']}"

            # 3. Time binding
            now = datetime.utcnow()
            # Parse ISO format timestamps
            issued_at = datetime.fromisoformat(token["issued_at"].rstrip("Z"))
            expires_at = datetime.fromisoformat(token["expires_at"].rstrip("Z"))

            if issued_at > now:
                return False, "REJECTED: token issued in future"

            if expires_at <= now:
                return False, "EXPIRED: wall clock exceeded expires_at"

            # 4. Signature verification
            signature_from_token = token["signature"]
            token_copy = dict(token)
            del token_copy["signature"]
            canonical_json = self._canonical_serialize(token_copy)

            # Use issuer's public key for verification
            issuer_key = issuer_public_key or self._get_issuer_key(token["issuer"])
            is_sig_valid = self._verify_signature(canonical_json, signature_from_token, issuer_key)

            if not is_sig_valid:
                return False, "REJECTED: invalid signature"

            # 5. Revocation check
            token_id = token["token_id"]
            if token_id in self.revocation_cache:
                return False, "REVOKED: token in revocation cache"

            # 6. Scope check (simplified)
            if "scope" not in token or "max_bytes" not in token.get("scope", {}):
                return False, "REJECTED: invalid scope"

            return True, "VERIFIED: token is valid and can be used"

        except Exception as e:
            return False, f"REJECTED: verification error: {str(e)}"

    def revoke_token(self, token_id: str):
        """
        Revoke a token (kill-switch).

        This creates a revocation record that gets gossiped.
        """
        now = datetime.utcnow()

        # Create revocation message and sign it
        revocation_data = {
            "token_id": token_id,
            "revoked_at": now.isoformat() + "Z",
            "issuer": self.node_id,
        }

        canonical = self._canonical_serialize(revocation_data)
        revocation_sig = self._sign(canonical)

        record = RevocationRecord(
            token_id=token_id,
            revoked_at=now.isoformat() + "Z",
            issuer=self.node_id,
            issuer_signature=revocation_sig,
        )

        # Add to local cache (in real system, this gets gossiped)
        self.revocation_cache[token_id] = record
        return record

    def gossip_revocation(self, other_manager: "ConsentTokenManager", token_id: str):
        """Simulate gossiping revocation to another node"""
        if token_id in self.revocation_cache:
            other_manager.revocation_cache[token_id] = self.revocation_cache[token_id]

    # Cryptographic helpers

    def _canonical_serialize(self, data: Dict[str, Any]) -> str:
        """Canonical JSON serialization (deterministic order, no whitespace)"""
        return json.dumps(data, separators=(',', ':'), sort_keys=True)

    def _sign(self, message: str) -> str:
        """Sign a message using this node's private key"""
        if HAS_ED25519:
            message_bytes = message.encode('utf-8')
            signature_bytes = self.private_key.sign(message_bytes)
            return signature_bytes.hex()
        else:
            # Fallback: HMAC-SHA256 using node_id as secret
            import hmac
            message_bytes = message.encode('utf-8')
            secret = str(self.node_id).encode('utf-8')
            signature = hmac.new(secret, message_bytes, hashlib.sha256).hexdigest()
            return signature

    def _verify_signature(self, message: str, signature: str, public_key) -> bool:
        """Verify a signature"""
        if HAS_ED25519 and public_key:
            try:
                message_bytes = message.encode('utf-8')
                signature_bytes = bytes.fromhex(signature)
                public_key.verify(signature_bytes, message_bytes)
                return True
            except Exception:
                return False
        else:
            # Fallback: verify HMAC using stored issuer node_id
            import hmac
            if isinstance(public_key, str) and public_key.startswith("mock_public_key_"):
                node_id = public_key.replace("mock_public_key_", "")
                message_bytes = message.encode('utf-8')
                secret = node_id.encode('utf-8')
                expected_sig = hmac.new(secret, message_bytes, hashlib.sha256).hexdigest()
                return hmac.compare_digest(signature, expected_sig)
            return False

    def _get_issuer_key(self, issuer_id: str):
        """Look up issuer's public key (normally from trusted registry)"""
        # For demo, return our own public key if issuer is us
        if issuer_id == self.node_id:
            return self.public_key
        return None

    def get_trusted_issuers(self) -> List[str]:
        """Return list of trusted issuer IDs"""
        return [self.node_id]


def demo_kill_switch():
    """Run the kill-switch demo"""

    print("=" * 70)
    print("CONSENT TOKEN KILL-SWITCH DEMO")
    print("Starline Consent Transport Protocol v0.1")
    print("=" * 70)
    print()

    # Setup
    node_a = ConsentTokenManager("node_A")
    node_b = ConsentTokenManager("node_B")

    # Register node_a as trusted issuer at node_b
    node_b.revocation_cache  # Initialize

    print("STEP 1: Node A creates a consent token")
    print("-" * 70)
    token = node_a.create_token(
        recipient="node_B",
        purpose="transfer memory shard for synchronisation",
        expires_in_seconds=300,
    )
    print(f"Token ID: {token['token_id']}")
    print(f"Issuer: {token['issuer']}")
    print(f"Recipient: {token['recipient']}")
    print(f"Purpose: {token['purpose']}")
    print(f"Issued at: {token['issued_at']}")
    print(f"Expires at: {token['expires_at']}")
    print(f"Signature (first 32 chars): {token['signature'][:32]}...")
    print(f"State: CREATED (SIGNED) ✓")
    print()

    print("STEP 2: Node B receives and verifies the token")
    print("-" * 70)
    # Simulate node_a's public key being known at node_b
    node_b.get_trusted_issuers = lambda: ["node_A", "node_B"]
    node_b._get_issuer_key = lambda x: node_a.public_key if x == "node_A" else node_b.public_key

    is_valid, reason = node_b.verify_token(token, issuer_public_key=node_a.public_key)
    print(f"Verification result: {is_valid}")
    print(f"Reason: {reason}")
    if is_valid:
        print(f"State: VERIFIED/ACTIVE ✓")
    print()

    if is_valid:
        print("STEP 3: Token is valid, operation would proceed")
        print("-" * 70)
        print("[Transfer would happen here...]")
        print("✓ Access ALLOWED under this token")
        print()

        print("STEP 4: Node A activates KILL-SWITCH (revokes token)")
        print("-" * 70)
        revocation = node_a.revoke_token(token['token_id'])
        print(f"Token {token['token_id'][:8]}... REVOKED")
        print(f"Revocation time: {revocation.revoked_at}")
        print(f"Revocation signature: {revocation.issuer_signature[:32]}...")
        print(f"State: REVOKED ✗")
        print()

        print("STEP 5: Gossip revocation to Node B")
        print("-" * 70)
        node_a.gossip_revocation(node_b, token['token_id'])
        print(f"Revocation cached at node_B")
        print()

        print("STEP 6: Node B attempts to verify token AFTER revocation")
        print("-" * 70)
        is_valid_after, reason_after = node_b.verify_token(token, issuer_public_key=node_a.public_key)
        print(f"Verification result: {is_valid_after}")
        print(f"Reason: {reason_after}")
        if not is_valid_after:
            print(f"State: REVOKED ✗")
            print()
            print("✓ Kill-switch EFFECTIVE: access is DENIED")
            print("✓ FAILING CLOSED: revocation is immediate and irreversible")
        print()

        print("=" * 70)
        print("DEMO COMPLETE: Kill-switch guarantee verified")
        print("=" * 70)


if __name__ == "__main__":
    if not HAS_ED25519:
        print("Warning: cryptography library not available")
        print("Using mock signatures for demo")
        print()

    demo_kill_switch()
