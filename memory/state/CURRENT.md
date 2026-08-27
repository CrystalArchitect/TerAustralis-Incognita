# CURRENT — Repository State Snapshot

**Last updated:** 2026-08-27 (session: memory-bootstrap-peiyva)  
**Basis:** `STATUS.md` (last updated 2026-08-20)  
**Authority:** See primary source for latest state

## What's running (executable code)

- **CrystalCore.OS terminal** — `mythos/crystalcore-os/crystalcore_os.py`
  - Status: **Running** (verified 2026-07-27)
  - Boots from source, plays to First Gate, saves/resumes from fresh clone
  - Stdlib-only, no external dependencies
  - Command: `python3 mythos/crystalcore-os/crystalcore_os.py`

- **Research prototypes** — `research/prototypes/story-library`
  - Status: **Running** (verified 2026-07-24)
  - Self-contained HTML, no build step
  - Renders in headless browser
  - Reference implementation for production SvelteKit version

- **CI on main**
  - Status: **Green** (run 2026-07-23)
  - Honest scope: src/ tests skipped (code moved to separate repos)
  - Coverage: dbt project, architecture tests, governance validation

## What's built, not running

- **dbt/crystalcore_emotion_warehouse** — Full dbt project
  - Status: **Built** (complete)
  - Staging/mart models, macros, tests exist
  - No warehouse configured, no runtime execution
  - Designed but not integrated

- **archive/** — Legacy code
  - Status: **Built** (versioned)
  - crystalcore-v0.13, clementine.py (local-snapshot-2026-07-17)
  - Read-only for provenance; do not build on it

## What's document (spec/architecture/vision)

- **docs/** — Architecture, governance, AI workflow, guides, ADRs
  - Status: **Built/Current** (continuously updated)
  - Authority: Primary canon for project rules

- **mythos/** — Crystal universe canon, art, tools, outer lore
  - Status: **Vision + Built** (stable; vision content marked)
  - 88 pieces of art, Codex, Apocryphon, Starline Transmissions

- **research/seven-sisters** — Research cycle (WATER-BRIEF, TRANSMIT-LOG)
  - Status: **Exploratory** (not production)

## What's designed, not built

- **Story Library production components** — SvelteKit/React
  - Status: **Designed** (prototype exists)
  - Spec: reference implementation in `research/prototypes/story-library`
  - Code: not in this repository

- **Workflow prompt kits** — `mythos/tools/` (daily-digest, signal-scanner)
  - Status: **Designed** (written as kits)
  - Wiring: to be implemented

- **Runtime Testing Specifications** — `docs/architecture/`
  - Status: **Designed** (spec exists)
  - Built coverage: 4 passing suites (partial subset of spec)

## Where the code actually lives

**This repository contains:**
- Governance, architecture, documentation
- Mythos content, vision, art
- dbt project (unexecuted)
- Archive (read-only)
- **NOT:** `src/` (code tree moved)

**Code now lives in:**
- `TerAustralis-Incognita-Code` (apps, site, protocol implementations)
- `TerAustralis-Incognita-Clementine` (companion)
- Other repos per migration plan

See `docs/architecture/SystemMap.md` and `docs/governance/Migration-Plan.md` for full detail.

## Known issues / uncertainties

### Resolved
- **Domain status** (2026-08-20): www.teraustralis.com.au is live, serving SvelteKit build (last-modified 2026-08-18). Code Pages builds from TerAustralis-Incognita-Code.

### Unknowns
- None currently tracked. See `memory/state/OPEN-QUESTIONS.md` for blockers.

## CI/CD status

- **GitHub Pages**: CrystalCore.OS terminal renders at `crystalcore-os` path (verify by deploy probe)
- **Workflows**: Checked 2026-07-23, green. No breaking changes expected.
- **Link checker**: May falsely report failures during deploy races; retry probe is authoritative

## Summary

**The repository is a knowledge/governance/vision hub, not a code repository.**

- Production code: built, running in separate repos
- Specifications: designed and complete
- Governance: stable and canonical
- Art/mythos: stable content, new work can be added
- Clementine's memory system: designed, partially implemented (see `mythos/content/MEMORY.md`)

---

**For full context, read `STATUS.md` at the repository root.**

This is a memory snapshot. Authority remains with the primary source.
