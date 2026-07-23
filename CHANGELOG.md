# Changelog

Notable changes to this repository, newest first. Day-to-day status lives
in [`docs/governance/Roadmap.md`](docs/governance/Roadmap.md); this file
records the milestones.

## 2026-07-23 — Code license: CC BY-NC-ND 4.0, superseding ADR-0006 §1

A separate, uncoordinated Claude session changed `LICENSE` from Apache-2.0
to CC BY-NC-ND 4.0 for full commercial exclusivity on the code, reversing
`ADR-0006`'s open-core decision without a superseding ADR, and its rewrite
of `NOTICE` also silently dropped the "TerAustralis Incognita" name and
copyright holder that `ADR-0007` had just fixed. The maintainer confirmed
CC BY-NC-ND 4.0 for code is the intended direction. `ADR-0008` records that
formally and fixes the resulting inconsistencies.

### Changed
- `docs/adr/ADR-0008.md` added: supersedes `ADR-0006` §1 only (§§2–3 —
  the six IP principles, trademark status — are unaffected); verifies via
  `git log` that no third-party contributor's code is affected by the
  relicensing (only the maintainer and Claude have ever committed here);
  adds a contribution-licensing clause to `CONTRIBUTING.md` reconciling
  "no derivative redistribution" with the repo's own pull-request workflow.
- `NOTICE` restored to "TerAustralis Incognita" / Crystal Arena-Turner as
  copyright holder, without touching the CC BY-NC-ND terms.
- `docs/ATTRIBUTIONS.md`'s "License Enforcement" and "Rebranding & Theft
  Prevention" sections rewritten — they had contradicted the rest of the
  same document by telling readers commercial use was freely permitted.
- Roughly a dozen other stale "code is Apache-2.0" references corrected for
  consistency: `README.md`, `LICENSE-CONTENT.md`, `mythos/README.md`,
  `mythos/COVENANT.md`, the `GOVERNANCE.md`/`LICENSE-CONTENT.md` site
  content mirrors, `docs/governance/Development-Standards.md`,
  `docs/architecture/crystal-core/Crystal-Runtime-Specification-v0.3.md`,
  two component `README.md`s, and the live site's `Footer.svelte` (was
  telling visitors the code was Apache-2.0 with a link to apache.org).
- Two nested per-component `LICENSE` files with full Apache-2.0 text
  (`src/crystal-core/LICENSE`, `src/apps/crystal-interface/LICENSE`)
  deleted — a monorepo with one root `LICENSE` doesn't need duplicates
  that can drift out of sync again.
- `src/sdk/typescript/package.json`'s `license` field updated to match;
  flagged in `ADR-0008` as worth a second look since a No-Derivatives
  license on a published npm package is unusual.

## 2026-07-23 — Name correction: TerAustralis Incognita

The project's name was being spelled "TeraAustralis Incognita" (two a's)
across most of the repository, but the maintainer's registered ABN trading
name is **TerAustralis Incognita** (one 'a') — confirmed by `README.md`'s
title, `NOTICE`, and every ABN reference under `archive/`, which already
agreed with the correct spelling. The double-a spelling was drift introduced
during the v1.0 reorganization, not a deliberate choice. Full reasoning:
[`docs/adr/ADR-0007.md`](docs/adr/ADR-0007.md).

### Changed
- `mythos/teraaustralis/` renamed to `mythos/teraustralis/` (history
  preserved via `git mv`); every internal path reference updated to match.
- Prose references to the project name corrected throughout live docs:
  `README.md`, `NOTICE`, `CONTRIBUTING.md`, `AGENTS.md`,
  `docs/governance/Constitution.md` (§1's locked name, corrected via its own
  §8 amendment process — see that file's amendment log), `docs/vision/Mission.md`,
  `docs/adr/ADR-0006.md`, and the mythos content that moved with the
  directory.
- `docs/adr/ADR-0001.md`, `docs/adr/ADR-0002.md`, and this file's own older
  entries are left unedited as the historical record of what was actually
  done at the time; `ADR-0007` supersedes the spelling detail without
  rewriting them.
- GitHub repository URLs and `git clone` instructions are unchanged — they
  still correctly point at `CrystalArchitect/TeraAustralis-Incognita`, the
  actual (unrenamed) repository name. Renaming the repository itself is
  flagged in `ADR-0007` as a separate, maintainer-only decision.

## 2026-07-23 — CrystalCore OS v0.2: Architecture Specification Release

Following review of v0.1, redefined v0.2 from "build the Engine" to
"clarify the architecture before implementing it" — a documentation-only
release, no runtime, by design. Rationale and the full decisions:
[`docs/adr/ADR-0004.md`](docs/adr/ADR-0004.md) (naming) and
[`docs/adr/ADR-0005.md`](docs/adr/ADR-0005.md) (the orchestrator concept).

### Changed
- `docs/vision/CrystalCore.md` rewritten from a five-row disambiguation
  table into the canonical taxonomy: CrystalCore Framework, CrystalCore
  Protocol, CrystalBridge, and CrystalCore OS, with the pre-existing
  mythos-terminal/platform name collision documented honestly rather than
  silently resolved. Any future runtime component is barred from becoming a
  fifth or sixth "CrystalCore" — it gets a name that describes its role.
- `docs/architecture/CrystalCore.md`'s section headers aligned to the new
  canonical names (Framework / Protocol pack / CrystalBridge).
- `docs/ai/AI-Architecture.md`'s orchestrator section: the previously
  separate "AI Router" idea folded into one name, "AI Orchestrator,"
  defined as recommend-then-human-decides (Task → Capability Assessment →
  Recommended AI → Human Review) rather than autonomous dispatch.
- `docs/governance/Roadmap.md`'s platform roadmap renumbered: v0.2 is now
  this specification release (delivered); the actual Engine build moves to
  v0.3, gated on the specification reaching implementation-level detail;
  the former v0.3 (Living Archive) becomes v0.4.

### Added
- `docs/ai/Decision-Matrix.md` — a task-type → recommended-AI →
  human-review-level table. This is the AI Orchestrator concept's first
  real increment, not a placeholder: no runtime, no automation, no new
  failure mode.
- `docs/adr/ADR-0004.md` and `ADR-0005.md`.

## 2026-07-23 — CrystalCore OS v1.0 repository architecture

The repository adopted the CrystalCore OS v1.0 layout (platform milestone
v0.1). Full mapping and rationale:
[`docs/adr/ADR-0001.md`](docs/adr/ADR-0001.md) — highlights:

### Changed
- All code moved under `src/` as a uniform shift (`apps/`, `crystal-core/`,
  `crystalcore/`, `node/`, `sdk/`, `site/`, `profiles/`, plus the mythos
  terminal to `src/crystalcore-os/`); runtime behavior unchanged and
  verified by the self-tests and suites.
- Component specs moved to `docs/architecture/crystal-core/`; root
  governance docs to `docs/governance/` (Constitution amendment logged);
  guides to `docs/guides/`; the Lattice sketch to
  `docs/architecture/lattice/`.
- `_archive/` became `archive/{legacy,2026}/`; `TeraAustralis/` folded into
  `mythos/teraaustralis/` with the strategy doc at
  `docs/vision/SouthernPillar.md`.
- Seven Sisters cycle material moved from the protocol pack to
  `research/seven-sisters/`.
- CI and the Pages deploy retargeted; the mesh-stub suite (`tests/`) now
  runs in CI; every path reference in code, docs, and the site swept.

### Added
- The documentation tree: `docs/{vision,architecture,governance,ai,agents,
  guides,adr}/` with per-area content, including the AI collaboration
  model and the first three ADRs.
- GitHub scaffolding: PR template, issue templates (bug / feature /
  mythos), discussion templates, CODEOWNERS.
- `scripts/maintenance/check.sh` (mirrors CI locally), area READMEs for
  `research/`, `archive/`, `assets/`, `examples/`, `scripts/`, and this
  changelog.

### Removed
- The inert nested `.github/` under the old `crystal-core/` (its issue
  templates were promoted to the root; its dead Pages workflow and
  boilerplate template deleted).

*(No earlier entries — the changelog starts with the v1.0 architecture;
prior history is in `git log` and the roadmap's "Recently landed".)*
