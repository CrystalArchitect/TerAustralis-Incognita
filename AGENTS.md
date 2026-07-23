# AGENTS.md — TeraAustralis-Incognita

## Project

Living vision stack: **TeraAustralis Incognita** · **CrystalVision** ·
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

- `src/` — all executable code (apps, crystal-core, crystalcore,
  crystalcore-os, node, sdk, site, profiles)
- `docs/` — vision · architecture · governance · ai · agents · guides · adr
- `research/` — exploratory, not production
- `mythos/` — the Crystal universe canon + `teraaustralis/` outer lore
  (content license)
- `archive/` — provenance only; never build on it
- `scripts/`, `tests/`, `examples/`, `assets/` — utilities, repo-level
  suites, curated demos, branding

## Checks

Run what CI runs before pushing:

```bash
scripts/maintenance/check.sh
```

(Details: `docs/guides/GitHub-Commit-Instructions.md`.)
