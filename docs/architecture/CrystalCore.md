# CrystalCore — the engineering side

The name map is in [`docs/vision/CrystalCore.md`](../vision/CrystalCore.md).
This page covers the three *built* CrystalCores and how they divide the work.

## The framework (`src/apps/lumina/crystalcore/`)

The sovereign-companion framework Lumina runs on:

- `companion.py` — the brain: memory layers, recall, chat, and the Covenant
  carried in the core prompt
- `memory.py` — the data model (Personality, Memory)
- `profiles.py` — multiple isolated companions, each with its own memory
- `sovereignty_scorer.py` — an unwired 0.1-alpha sketch of eight sovereignty
  metrics (explicitly not in use)

Local-first by construction: Ollama-backed, JSON storage on the user's own
disk, no account, no cloud requirement. The Covenant
([`mythos/COVENANT.md`](../../mythos/COVENANT.md)) is the product spec here,
not decoration — changes must preserve local-first operation, the absolute
pause, and full memory ownership.

## The protocol pack (`src/crystal-core/`)

Four components, stdlib-only except where real cryptography is required:

- **Starline Weaver** (`clementine/bridge/`) — the multi-AI bus. Every
  message must carry a science/story/vision label or it is not heard
  (Belt-Three law, enforced in `agents.py`); a red button halts everything.
  Spec: [`crystal-core/STARLINE-WEAVE-PROTOCOL.md`](crystal-core/STARLINE-WEAVE-PROTOCOL.md).
- **Pipeline** (`services/`) — Decode → Ingest → Twin: validate events,
  quarantine bad ones with reasons, aggregate into a SQLite twin.
- **Starline** (`starline/`) — peer-to-peer memory exchange over a real
  Noise handshake; consent receipts, instant revocation. Spec:
  [`crystal-core/STARLINE.md`](crystal-core/STARLINE.md). The one component
  with a dependency (`cryptography`) — audited primitives are not something
  to hand-roll.
- **RDP** (`rdp/`) — tamper-evident hash-chained records plus an explainable
  decision kernel. It records what other components decide; it does not
  govern them ([`crystal-core/RDP-INTEGRATION.md`](crystal-core/RDP-INTEGRATION.md)).

## The bridge (`src/crystalcore/`)

CrystalBridge: the MCP stdio server that lets a guest AI meet Lumina —
fail-closed. Every tool call passes four checks in order (approval →
permission → scope → provenance, `gate.py`) and lands in an append-only
audit log (`audit.py`). Guest grants live in
`src/profiles/<name>/bridge_config.json`. Guide:
[`docs/guides/MCP-Guest.md`](../guides/MCP-Guest.md).

## Why three, not one

They answer different trust questions. The framework trusts one human
completely and no one else. The pack mediates between many mutually
untrusting agents. The bridge lets outsiders in through a gate that fails
shut. Merging them would blur exactly the boundaries the project exists to
keep sharp.
