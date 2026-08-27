# MILESTONES

Dated landings. Canonical sources:
[`CHANGELOG.md`](../CHANGELOG.md) (repository milestones) and
[`docs/governance/Roadmap.md`](../docs/governance/Roadmap.md)
("Recently landed"). Trim here if this file grows; do not trim the
canonical files from a memory session.

**Write-back:** when a PR merges and changes the working picture, add a
dated bullet and update [`state/CURRENT.md`](state/CURRENT.md).

**Sourced:** 2026-08-28. Newest first.

## 2026-08-28 — this branch (unmerged)

- Claude Code **read-and-write** memory protocol: root `CLAUDE.md` +
  `memory/`. Does not restore the Repository Engineer seat (ADR-0014).
  Does not amend the Constitution. **Not on `main` until Crystal merges.**

## 2026-08-20 (CHANGELOG + Roadmap cluster)

- Human door: GitHub + sites + Discord. `docs/guides/Access.md` — this
  repo is not private; OAuth and a twentieth GitHub are refused join paths.
- Cybernetics note: `docs/architecture/CYBERNETICS-VSM.md`. Model, not a
  new OS mode.
- Ink honesty + SourceCode as external peer (`ADR-0016`, Proposed).
  `-Code` marked public in the charter. `ADR-0015` stamped Accepted (PR #118).
- Stop growing the constellation (`ADR-0015`). Nineteen repositories
  measured. No new GitHub repository without an ADR.
- Domain measured: apex 301 → www 200, SvelteKit from `-Code`. Root
  `index.html` + `.nojekyll` so leftover Jekyll Pages is a pointer, not a
  second site. GitHub About description patched out-of-git to one *a*.
- Grok Build takes the Repository Engineer seat (`ADR-0014`, PR #116).
  Claude retained as history.

## 2026-07-29

- Codex of the Oracle in `mythos/content/CODEX-OF-THE-ORACLE.md` —
  authority weight it sets for itself: **zero**. Locked names hold.
  Engineering claims stay in the archive until receipts exist.

## 2026-07-27

- CrystalCore.OS mythos terminal boots from a fresh clone
  (`mythos/crystalcore-os/crystalcore_os.py`), stdlib-only. Verified in
  [`STATUS.md`](../STATUS.md). "Songline" stays a cultural image, never a
  component name. Deliberately **not** implemented: printed security
  commands with no mechanism (`verify-certificates`, `security harden`,
  continuous integrity monitoring) — Incognita Rule.

## 2026-07-24

- Story Library design + self-contained HTML prototype
  (`research/prototypes/story-library/`). Production SvelteKit/React
  components: not built.
- CI honest: src/tests-dependent steps skip because those trees live in
  `-Code`.

## 2026-07-23 — foundation day

- Three-project boundary (`ADR-0011`) + Project-Boundaries + Migration-Plan
  (Vision; nothing moved in that ADR).
- Entry-point docs resynchronized: `src/`, `scripts/`, `tests/` are not in
  this git and never were.
- Name correction to **TerAustralis Incognita** (`ADR-0007`).
- License terminus: uniform CC BY-NC-ND 4.0 (`ADR-0006` → `0008` → `0009`
  → `0010`).
- CrystalCore OS v0.2 Architecture Specification Release (`ADR-0004`,
  `ADR-0005`). No runtime, by design.
- CrystalCore OS v1.0 repository architecture (`ADR-0001`, `ADR-0002`,
  `ADR-0003`). Platform milestone v0.1.

## Platform versions (Roadmap)

| Version | State on disk |
|---|---|
| v0.1 Repository foundation | Delivered 2026-07-23 |
| v0.2 Architecture Specification | Delivered 2026-07-23 |
| v0.3 Engine layer | Not started |
| v0.4 Living Archive | Not started |
| v1.0 Stable platform | Target, not a promise |
