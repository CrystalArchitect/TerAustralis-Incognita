# STATUS

Last updated: 2026-07-24

This file describes the state of this repository, not the ambition of
the system. Same ledger, same categories as the system ledger in
CrystalCore.OS-the-Crystal-Architecture-Archive. This is the umbrella:
canon, governance, mythos, research. The code moved out under the
Migration Plan, and the ledger reflects that.

## Running
Executes, or can be opened and used by someone other than me.

- research/prototypes/story-library — self-contained HTML prototype;
  no build step; renders in a headless browser, verified 2026-07-24.
- CI on main is green (run of 2026-07-23), with honest scope: the
  src/tests-dependent steps skip themselves because those trees now
  live in TerAustralis-Incognita-Code.

## Built, not currently running
Code exists and is complete enough to run. No runtime here exercises it.

- dbt/crystalcore_emotion_warehouse — a full dbt project (staging and
  mart models, macros, tests). No warehouse is configured anywhere, no
  CI runs it, and it was not executed this session.
- archive/ code (legacy/crystalcore-app; 2026/local-snapshot-2026-07-17
  with crystalcore-v0.13 and clementine.py) — quarantined by
  archive/README on purpose: provenance, not production.

## Exists as a document
The repository's actual product.

- docs/ — ADRs, the governance stack (Project-Boundaries.md,
  Migration-Plan.md, licensing), and the crystal-core architecture
  canon (Blueprint v0.3, Runtime Specification v0.3, module
  interfaces, testing specifications).
- mythos/ — content, art, crystalcore-os, teraustralis, and the
  prompt kits under mythos/tools.
- research/seven-sisters (WATER-BRIEF), CHANGELOG, the licensing and
  conduct files at root.

## Designed, not built
- Story Library production components — the prototype above is the
  reference implementation; the SvelteKit/React components it
  specifies for the live site do not exist yet.
- The workflows the mythos/tools prompt kits describe (daily-digest,
  signal-scanner) — written as kits, wired to nothing.
- The Runtime Testing Specifications describe more suite coverage than
  the code tree carries; the four passing suites are the built subset.

## Concept only
Nothing new at this tier in this repository; see the system ledger.

## Known unknowns

- What the domain serves. CNAME claims www.teraustralis.com.au, but
  the latest Pages run deployed nothing — the deploy job skipped, by
  design, because src/site is no longer in this repo, and deploy.yml's
  own notice records that the site was never in git history here. Has
  the SvelteKit site ever been live at that domain, and what is there
  now? Unverified (egress blocked from the session container).
- publish-packages.yml (tag-triggered) and test-packages.yml (watches
  packages/**) can no longer fire on this tree — packages/ does not
  exist. Dormant by drift rather than by decision.
- examples/README.md commands target src/ paths that moved to the code
  repo (the file says so itself); the index awaits re-pointing.
- teraustralis-final.html — the system ledger's one "Running" item is
  not present anywhere in this repository, including archive/.
  Presumed to live in an archived repo; unresolved this session.
