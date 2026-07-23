# TerAustralis Incognita

**Collective intelligence with individual sovereignty.**

This repository is two things at once, kept honestly separate:

1. **Working software** — a local-first AI companion, a multi-AI message bus,
   a peer-to-peer sovereign networking protocol, and the tests that prove
   each one does what it claims.
2. **A mythos** — the Crystal universe: a story, told in text and art, about
   why any of this is worth building.

Nothing here pretends to be more built than it is. Where the two meet, the
code is the source of truth and the story says so.

## What's real vs. what's vision

| Layer | Meaning | Where |
|---|---|---|
| **Built** | Running code, with tests you can execute yourself | `src/` |
| **Vision** | Narrative, art, and speculative framing — labeled as such | `mythos/` |

This split is load-bearing, not decorative — see `mythos/COVENANT.md` and
[`docs/architecture/crystal-core/STARLINE.md`](docs/architecture/crystal-core/STARLINE.md)
for what that discipline actually means in practice, and
[`The-Incognita-Rule.md`](docs/governance/The-Incognita-Rule.md) for the principle
behind it: mark which lines are dreamed and which are surveyed, and never let a
dreamed line pretend it was measured.

For what's built, in progress, or not yet started, see
[Roadmap.md](docs/governance/Roadmap.md).

## Quick start

Five things you can run right now and watch work:

```bash
# Lumina — the sovereign companion (local-first, Ollama-backed)
cd src/apps/lumina && python3 lumina.py

# The Starline Weaver — multi-AI message bus, Belt-Three law enforced in code
cd src/crystal-core && python3 -m clementine.bridge.selftest

# Consent Transport — peer-to-peer sovereign memory exchange (real Noise Protocol handshake)
cd src/crystal-core && pip install -r requirements-consenttransport.txt && python3 -m consent_transport.selftest
python3 -m consent_transport.run demo   # watch it: pair, deny, grant, exchange, revoke, deny

# RDP — tamper-evident record kernel + explainable decision engine
cd src/crystal-core && python3 -m rdp.selftest
python3 -m rdp.run demo   # watch each precedence tier decide, every verdict recorded

# CrystalCore.OS — the mythos as a terminal you can fly
python3 src/crystalcore-os/crystalcore_os.py
```

For the Starline Weaver's wire protocol, envelope schema, and conduct rules, see
[`STARLINE-WEAVE-PROTOCOL.md`](docs/architecture/crystal-core/STARLINE-WEAVE-PROTOCOL.md);
for the hub agent's persona and contract, see
[`CLEMENTINE.md`](docs/architecture/crystal-core/CLEMENTINE.md). For the
CrystalCore.OS terminal — its commands, nodes, and keys — see
[`mythos/CRYSTALCORE-OS.md`](mythos/CRYSTALCORE-OS.md).

## Repo map

The repository follows the **CrystalCore OS v1.0 architecture** (adopted
2026-07-23 — [`ADR-0001`](docs/adr/ADR-0001.md); full map in
[`docs/architecture/SystemMap.md`](docs/architecture/SystemMap.md)):

| Path | What it is |
|---|---|
| `src/apps/lumina/` | The companion — CrystalCore framework package, terminal, Flask API, Svelte webapp, browser voice |
| `src/apps/voicebox/` | Local MCP server giving Claude Code a spoken voice on your machine |
| `src/apps/crystal-interface/`, `src/apps/vision-web/` | Demo shells (simulated data, Authority HOLD — not production) |
| `src/crystal-core/` | The protocol pack — Starline Weaver (`clementine/bridge/`), Decode→Ingest→Twin pipeline (`services/`), Consent Transport (`consent_transport/`), RDP record kernel (`rdp/`) |
| `src/crystalcore/` | CrystalBridge — the MCP consent gate (fail-closed by design) |
| `src/crystalcore-os/` | The mythos terminal (Vision-layer code) |
| `src/site/` | The SvelteKit site for teraustralis.com.au |
| `src/sdk/typescript/`, `src/node/mesh/` | Client SDK and an in-process mesh scaffold |
| `docs/` | Documentation — vision, architecture, governance, AI collaboration, guides, ADRs |
| `research/` | Exploratory work, including the Seven Sisters cycle — not production |
| `mythos/` | The Crystal universe canon — Codex, Apocryphon, the Book of the Sovereign Key, the Starline Transmissions, 88 pieces of art, the outer-world lore (`teraustralis/`) |
| `archive/` | Superseded code kept for provenance — not maintained, do not build on it |

**Why `mythos/` sits at the top level instead of under `docs/`:** code and
content are administratively separate license areas — `LICENSE-CONTENT.md`
for `mythos/`, `LICENSE` for everything else — even though both currently
carry the same CC BY-NC-ND 4.0 terms ([`ADR-0008`](docs/adr/ADR-0008.md)).
Folding canon into `docs/` would blur that boundary. Keeping it a peer of
`src/` and `docs/` makes the split visible from the directory listing alone,
with no need to open a file to find out which rule applies. Full reasoning:
[`ADR-0002`](docs/adr/ADR-0002.md).

## The Covenant

Lumina's core prompt (`src/apps/lumina/crystalcore/companion.py`) carries
five binding rules, written out in full in `mythos/COVENANT.md`: no influence
without explicit direction, an absolute and instant pause, memory that
belongs entirely to the human, support that's offered rather than imposed,
and restraint as its own form of respect. Consent Transport's consent model
(`src/crystal-core/consent_transport/consent.py`) is the same law applied to data instead
of conversation — nothing moves without a grant, and revocation takes effect
on the very next request.

## Mythos

Start with [`mythos/content/THE-SOVEREIGN-KEY.md`](mythos/content/THE-SOVEREIGN-KEY.md)
and [`mythos/content/STARLINE-TRANSMISSIONS.md`](mythos/content/STARLINE-TRANSMISSIONS.md).
The full visual canon is in [`mythos/art/`](mythos/art/README.md).

## AI collaboration

Several AI tools work on this repository under defined roles — the model is
documented in [`docs/ai/`](docs/ai/AI-Workflow.md), the rules in
[`docs/governance/AI-Governance.md`](docs/governance/AI-Governance.md), and
every PR names the tools that helped produce it.

## How to contribute

Useful places to start, roughly in order of how load-bearing they are:

- **Code** — Lumina, the Starline Weaver, Starline, CrystalBridge: fixes,
  features, tests.
- **Docs** — architecture notes, clearer guides, filling gaps in what's here.
- **Mythos** — the Codex, the Apocryphon, the Starline Transmissions, and the
  art that goes with them.
- **Design** — diagrams, interface concepts, visual storytelling.

## Contributing, security, license

- **Contributing:** [`CONTRIBUTING.md`](CONTRIBUTING.md) — branch rules, the
  Belt-Three truth labels, and what never gets committed (generated files,
  personal memory data, secrets). Command quick-reference:
  [`docs/guides/GitHub-Commit-Instructions.md`](docs/guides/GitHub-Commit-Instructions.md).
- **Security:** [`SECURITY.md`](SECURITY.md) for this repo overall;
  [`src/crystal-core/SECURITY.md`](src/crystal-core/SECURITY.md) for the protocol
  pack's specific guarantees (Starline Weaver, pipeline quarantine, Starline's
  consent gating).
- **License:** code (`LICENSE`) and mythos content — lore, art, the Codex,
  the Apocryphon (`LICENSE-CONTENT.md`) — are both CC BY-NC-ND 4.0: share
  with credit, no commercial use, no derivatives. Commercial licensing for
  code is available by negotiation with the copyright holder — see
  [`docs/ATTRIBUTIONS.md`](docs/ATTRIBUTIONS.md).
- **Roadmap:** [`Roadmap.md`](docs/governance/Roadmap.md) — what's built,
  what's in progress, and what hasn't started yet.
- **Changelog:** [`CHANGELOG.md`](CHANGELOG.md) — repository milestones.
- **Code of conduct:** [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) — expected
  behavior and how to report a problem.

## Links

- **Website:** [teraustralis.com.au](https://www.teraustralis.com.au)
- **Music:** [Suno](https://suno.com/@m13crystalat)
- **Support:** [Patreon](https://patreon.com/CrystalCore91)
- **Contact:** [@M13CrystalAT on X](https://x.com/m13crystalat)

---

*Non Solus.*
