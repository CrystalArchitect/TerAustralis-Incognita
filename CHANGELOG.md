# Changelog

Notable changes to this repository, newest first. Day-to-day status lives
in [`docs/governance/Roadmap.md`](docs/governance/Roadmap.md); this file
records the milestones.

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
