# Contributing to TerAustralis Incognita

Welcome. This is the canonical monorepo of the Crystal universe — the
narrative, the companion, the protocol, and the bridge all live here.
Contributions are welcome; here's what to know before you open a PR.

Before opening a PR, also read [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) —
short, and specific to how this project actually works.

## Ground rules

1. **Work on a branch, propose via pull request.** Direct pushes to `main`
   are reserved for the maintainer.
2. **Never commit generated files.** `.svelte-kit/`, `dist/`, `build/`,
   `node_modules/`, and `__pycache__/` are all ignored — if `git status`
   shows hundreds of files after running a dev server, stop and check
   `.gitignore` before staging.
3. **Never commit personal data.** Clementine's memory and profiles
   (`clementine_memory*`, `clementine_profiles/`) are the user's private
   property and must never enter git — the `.gitignore` enforces this;
   don't work around it.
4. **No secrets.** API keys live in environment variables only. `.env`
   files are ignored and stay that way.
5. **CI must pass.** Every PR runs a Python syntax check and the
   crystal-core self-tests (`clementine.bridge.selftest`,
   `services.selftest`). Run them locally first:
   ```bash
   python -m compileall -q apps/clementine crystal-core crystalcore node tests
   cd crystal-core && python -m clementine.bridge.selftest && python -m services.selftest
   ```

## The Belt-Three law (labels)

Everything in this project carries one of three truth labels:

| Layer | Meaning |
|-------|---------|
| **Science** | Astronomy, hydrology, published geography, running code |
| **Story** | Dreaming / Songline narratives (honour; no restricted detail) |
| **Vision** | CrystalCore art, mythos, and protocol fiction |

Keep them straight. Code claims must be true; mythos must be labeled as
mythos; no real-world coercion or fake hydrology, ever. Where real people
appear in Vision-layer content, it is storytelling only — no affiliation or
endorsement implied.

## Licensing — read before reusing content

This repo is dual-licensed:

- **Code** (apps, services, packages, crystalcore, crystal-core, node,
  sdk, tests): **Apache-2.0** — see `LICENSE`.
- **Content** (TeraAustralis lore, `mythos/`, CrystalVision suite,
  universe/brand docs, imagery): **CC BY-NC-ND 4.0** — see
  `LICENSE-CONTENT.md`. You may share it with credit; you may **not**
  remix it or use it commercially. Contributions to the mythos are
  accepted under the same terms.

## Map of the repo

| Path | What it is |
|------|-----------|
| `apps/clementine/` | The sovereign companion (CrystalCore framework, Flask API, Svelte webapp) |
| `apps/voicebox/` | Local MCP text-to-speech server |
| `apps/crystal-vision/`, `apps/crystal-interface/`, `apps/vision-web/` | Demo shells (simulated data, Authority HOLD) |
| `crystal-core/` | Protocol pack — Songline Bus, Decode→Ingest→Twin pipeline, specs |
| `crystalcore/` | CrystalBridge MCP consent gate (fail-closed) |
| `mythos/` | The canon — Codex, Apocryphon, Covenant, the Book of the Sovereign Key, art |
| `site/` | SvelteKit site for teraustralis.com.au |
| `_archive/` | Legacy copies kept for provenance — do not build on these |

See [`ROADMAP.md`](ROADMAP.md) for what's built, in progress, or not yet
started across these paths.

## The Covenant applies to code too

Clementine's Sovereignty Covenant (`mythos/COVENANT.md`) is not just
lore — it's the product spec. Changes to the companion must preserve:
local-first operation, opt-in cloud, absolute pause, full memory
ownership, and support that is offered, never imposed.

*Non Solus — Not Alone.*
