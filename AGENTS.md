# AGENTS.md — TerAustralis-Incognita

## Project

Living vision stack: **TerAustralis Incognita** · **CrystalVision** ·
**CrystalCore.Lattice** — organized as the **CrystalCore OS v1.0**
repository architecture (map: `docs/architecture/SystemMap.md`).

## Canon law

1. Read `docs/governance/Constitution.md` before large changes. Locked
   names stay locked.
2. Disk is canon > chat.
3. Substantial work → commit it, honestly labeled (Built/Vision). The
   Lattice-delta convention was never built — see the Constitution's
   implementation note; a normal commit through review is the practice.
4. New AI tool used → name it in your PR description (the PR template
   asks). Full rules: `docs/governance/AI-Governance.md`.
5. Cultural respect: no false sacred; fire-circle ethic (`mythos/NAMES.md`).

## Your role

Per-agent operating instructions live in `docs/agents/` (ChatGPT, Claude,
DeepSeek, Gemini, Grok), with tool profiles and the workflow between them
in `docs/ai/`. Read yours before substantial work.

## Layout

In this repository (git):

- `docs/` — vision · architecture · governance · ai · agents · guides · adr
- `mythos/` — the Crystal universe canon + `teraustralis/` outer lore
  (content license)
- `research/` — exploratory, not production
- `dbt/` — the emotion-warehouse dbt project
- `examples/`, `assets/` — curated demo index, branding
- `archive/` — provenance only; never build on it

Described in the docs but **not in this repository** — the code's
location is being re-established after the maintainer's laptop was
retired
(see `docs/architecture/SystemMap.md`, "Where the code actually lives"):

- `src/` — all executable code (apps, crystal-core, crystalcore,
  crystalcore-os, node, sdk, site, profiles)
- `scripts/`, `tests/` — utilities and repo-level suites

## Checks

Run what CI runs before pushing:

```bash
scripts/maintenance/check.sh
```

`scripts/` is not in this repository, so for docs-only changes here there
is currently nothing to run — see the SystemMap status note.

(Details: `docs/guides/GitHub-Commit-Instructions.md`.)
