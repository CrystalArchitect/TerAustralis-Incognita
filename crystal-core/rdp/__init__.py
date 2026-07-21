"""Reciprocal Dawn Protocol (RDP) — the deterministic decision/record layer.

Reconstructed from the RDP-Spec v1.1 handoff summary. The original reference
kernel and conformance fixtures described in that handoff never actually
existed as files — only the prose spec did. So this is a fresh, self-contained
implementation whose own selftest is its ground truth. It is honestly NOT
"conformant to an external frozen suite" (there isn't one); it is a correct,
tested implementation of the protocol as specified.

Modules:
  canonical  — RDP-JCS Profile v1: lexical decimal handling + canonical JSON.
  record     — append-only, SHA-256 hash-chained audit record.

Run the tests:  cd crystal-core && python3 -m rdp.selftest
"""

__version__ = "0.1.0"
