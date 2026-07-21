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
| **Built** | Running code, with tests you can execute yourself | `crystal-core/`, `crystalcore/`, `apps/clementine/` |
| **Vision** | Narrative, art, and speculative framing — labeled as such | `mythos/` |

This split is load-bearing, not decorative — see `mythos/COVENANT.md` and
`crystal-core/spec/STARLINE.md` for what that discipline actually means in
practice.

## Quick start

Four things you can run right now and watch work:

```bash
# Clementine — the sovereign companion (local-first, Ollama-backed)
cd apps/clementine && python3 clementine.py

# The Songline Bus — multi-AI message bus, Belt-Three law enforced in code
cd crystal-core && python3 -m clementine.bridge.selftest

# Starline — peer-to-peer sovereign memory exchange (real Noise Protocol handshake)
cd crystal-core && pip install -r requirements-starline.txt && python3 -m starline.selftest
python3 -m starline.run demo   # watch it: pair, deny, grant, exchange, revoke, deny

# CrystalCore.OS — the mythos as a terminal you can fly
python3 mythos/crystalcore_os.py
```

## Repo map

| Path | What it is |
|---|---|
| `apps/clementine/` | The companion — CrystalCore framework package, terminal, Flask API, Svelte webapp, browser voice |
| `apps/voicebox/` | Local MCP server giving Claude Code a spoken voice on your machine |
| `apps/crystal-vision/`, `apps/crystal-interface/`, `apps/vision-web/` | Demo shells (simulated data, Authority HOLD — not production) |
| `crystal-core/` | The protocol pack — Songline Bus (`clementine/bridge/`), Decode→Ingest→Twin pipeline (`services/`), Starline (`starline/`) |
| `crystalcore/` | CrystalBridge — the MCP consent gate (fail-closed by design) |
| `mythos/` | The Crystal universe canon — Codex, Apocryphon, the Book of the Sovereign Key, the Starline Transmissions, 81 pieces of art, `crystalcore_os.py` |
| `site/` | The SvelteKit site for teraustralis.com.au |
| `sdk/typescript/`, `node/mesh/` | Client SDK and an in-process mesh scaffold |
| `TeraAustralis/`, `CrystalCore.Lattice/`, `docs/` | Lore, activation protocol notes, and architecture docs |
| `_archive/` | Superseded code kept for provenance — not maintained, do not build on it |

## The Covenant

Clementine's core prompt (`apps/clementine/crystalcore/companion.py`) carries
five binding rules, written out in full in `mythos/COVENANT.md`: no influence
without explicit direction, an absolute and instant pause, memory that
belongs entirely to the human, support that's offered rather than imposed,
and restraint as its own form of respect. Starline's consent model
(`crystal-core/starline/consent.py`) is the same law applied to data instead
of conversation — nothing moves without a grant, and revocation takes effect
on the very next request.

## Mythos

Start with [`mythos/content/THE-SOVEREIGN-KEY.md`](mythos/content/THE-SOVEREIGN-KEY.md)
and [`mythos/content/STARLINE-TRANSMISSIONS.md`](mythos/content/STARLINE-TRANSMISSIONS.md).
The full visual canon is in [`mythos/art/`](mythos/art/README.md).

## How to contribute

Useful places to start, roughly in order of how load-bearing they are:

- **Code** — Clementine, the Songline Bus, Starline, CrystalBridge: fixes,
  features, tests.
- **Docs** — architecture notes, clearer guides, filling gaps in what's here.
- **Mythos** — the Codex, the Apocryphon, the Starline Transmissions, and the
  art that goes with them.
- **Design** — diagrams, interface concepts, visual storytelling.

## Contributing, security, license

- **Contributing:** [`CONTRIBUTING.md`](CONTRIBUTING.md) — branch rules, the
  Belt-Three truth labels, and what never gets committed (generated files,
  personal memory data, secrets).
- **Security:** [`SECURITY.md`](SECURITY.md) for this repo overall;
  [`crystal-core/SECURITY.md`](crystal-core/SECURITY.md) for the protocol
  pack's specific guarantees (Songline Bus, pipeline quarantine, Starline's
  consent gating).
- **License:** code is Apache-2.0 (`LICENSE`); mythos content — lore, art,
  the Codex, the Apocryphon — is CC BY-NC-ND 4.0 (`LICENSE-CONTENT.md`):
  share with credit, no commercial use, no derivatives.

## Links

- **Website:** [teraustralis.com.au](https://www.teraustralis.com.au)
- **Music:** [Suno](https://suno.com/@m13crystalat)
- **Support:** [Patreon](https://patreon.com/CrystalCore91)
- **Contact:** [@M13CrystalAT on X](https://x.com/m13crystalat)

---

*Non Solus.*
