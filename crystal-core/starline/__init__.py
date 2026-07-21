"""Starline — the sovereign communication layer between Clementine agents.

Two locally-running companions exchange consented memory fragments directly,
peer to peer, with no server in the middle. See spec/STARLINE.md.

Scope for this version: strict 1:1, pull-based (a peer must request and be
approved before anything moves), same-LAN or manually-paired discovery.
Group/mesh sharing is deliberately out of scope — see the spec's open
questions for why.

Needs the `cryptography` package (X25519, Ed25519, ChaCha20-Poly1305) —
the one dependency in an otherwise stdlib-only repo. See requirements-starline.txt.
"""

__version__ = "0.1.0"
