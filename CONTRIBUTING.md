# Contributing to TerAustralis Incognita

Welcome. This is the canonical monorepo of the Crystal universe — the
narrative, the companion, the protocol, and the bridge all live here.
Contributions are welcome; here's what to know before you open a PR.

Before opening a PR, also read [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) —
short, and specific to how this project actually works. For the exact
clone / check / commit / push commands, see
[`docs/guides/GitHub-Commit-Instructions.md`](docs/guides/GitHub-Commit-Instructions.md);
the full review process is
[`docs/governance/Review-Process.md`](docs/governance/Review-Process.md).

## Ground rules

1. **Work on a branch, propose via pull request.** Direct pushes to `main`
   are reserved for the maintainer.
2. **Never commit generated files.** `.svelte-kit/`, `dist/`, `build/`,
   `node_modules/`, and `__pycache__/` are all ignored — if `git status`
   shows hundreds of files after running a dev server, stop and check
   `.gitignore` before staging.
3. **Never commit personal data.** Lumina's memory and profiles
   (`clementine_memory*`, `clementine_profiles/`) are the user's private
   property and must never enter git — the `.gitignore` enforces this;
   don't work around it.
4. **No secrets.** API keys live in environment variables only. `.env`
   files are ignored and stay that way.
5. **CI must pass.** Every PR runs a Python syntax check, the
   crystal-core self-tests (`clementine.bridge.selftest`,
   `services.selftest`, `starline.selftest`, `rdp.selftest`), and the
   pytest suites. Run them locally first:
   ```bash
   scripts/maintenance/check.sh
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

The *why* behind these labels — and the rest of the project's honesty
discipline — is written out in
[`The-Incognita-Rule.md`](docs/governance/The-Incognita-Rule.md):
mark which lines are dreamed and which are surveyed, and never let a dreamed line
pretend it was measured.

## Licensing — read before reusing content

This repo is dual-licensed:

- **Code** (everything under `src/`, plus `tests/` and `scripts/`):
  **Apache-2.0** — see `LICENSE`.
- **Content** (`mythos/` — the Crystal universe canon, the TeraAustralis
  lore, the art): **CC BY-NC-ND 4.0** — see `LICENSE-CONTENT.md`. You may
  share it with credit; you may **not** remix it or use it commercially.
  Contributions to the mythos are accepted under the same terms.

## Map of the repo

The full map is [`docs/architecture/SystemMap.md`](docs/architecture/SystemMap.md);
the short version:

| Path | What it is |
|------|-----------|
| `src/apps/lumina/` | The sovereign companion (CrystalCore framework, Flask API, Svelte webapp) |
| `src/apps/voicebox/` | Local MCP text-to-speech server |
| `src/apps/crystal-interface/`, `src/apps/vision-web/` | Demo shells (simulated data, Authority HOLD) |
| `src/crystal-core/` | Protocol pack — Starline Weaver, Decode→Ingest→Twin pipeline, Starline, RDP |
| `src/crystalcore/` | CrystalBridge MCP consent gate (fail-closed) |
| `src/site/` | SvelteKit site for teraustralis.com.au |
| `docs/` | Documentation — architecture, governance, AI collaboration, guides, ADRs |
| `research/` | Exploratory work — not production |
| `mythos/` | The canon — Codex, Apocryphon, Covenant, the Book of the Sovereign Key, art |
| `archive/` | Legacy copies kept for provenance — do not build on these |

See [`Roadmap.md`](docs/governance/Roadmap.md) for what's built, in
progress, or not yet started across these paths.

## AI-assisted contributions

AI tools are first-class contributors here, under rules:
[`docs/governance/AI-Governance.md`](docs/governance/AI-Governance.md).
The short version — every PR names the AI tools that helped produce it,
AI claims follow the same evidence rule as everyone else's, and the
maintainer keeps the veto.

## The Covenant applies to code too

Lumina's Sovereignty Covenant (`mythos/COVENANT.md`) is not just
lore — it's the product spec. Changes to the companion must preserve:
local-first operation, opt-in cloud, absolute pause, full memory
ownership, and support that is offered, never imposed.

*Non Solus — Not Alone.*
