# VERIFIED — Facts Confirmed by Running Code or Checking Reality

**Status: BUILT** — These facts have been verified by code execution, live checks, or repository inspection.

## Executable code

**CrystalCore.OS terminal boots from source**
- Claim: `mythos/crystalcore-os/crystalcore_os.py` is runnable
- Evidence: Executed 2026-07-27; boots, plays to open First Gate, saves/resumes from fresh clone
- Command: `python3 mythos/crystalcore-os/crystalcore_os.py`
- Status: Verified, stdlib-only, no external dependencies
- Reference: `STATUS.md` (2026-08-20)

**Story Library prototype renders in headless browser**
- Claim: `research/prototypes/story-library` is self-contained HTML with no build step
- Evidence: Verified 2026-07-24 by rendering in headless browser
- Status: Verified, reference implementation for production SvelteKit version
- Reference: `STATUS.md` (2026-08-20)

**CI on main passes**
- Claim: GitHub Actions CI runs green on main branch
- Evidence: Run 2026-07-23 succeeded with honest scope (src/ tests skipped because code moved)
- Status: Verified, green
- Coverage: dbt project, architecture tests, governance validation
- Reference: `.github/workflows/` (actual runs visible in GitHub Actions)

## Live infrastructure

**Domain www.teraustralis.com.au is live and serving SvelteKit**
- Claim: Public website at www.teraustralis.com.au returns 200
- Evidence: Probed 2026-08-20 at 20:28, 20:33, 20:39 UTC; all returned 200 with SvelteKit build
- Last-modified: 2026-08-18 (SvelteKit build artifact)
- Status: Verified, live
- Built from: TerAustralis-Incognita-Code repository (Pages configuration)
- Reference: `STATUS.md` / `OPEN-QUESTIONS.md` (resolved 2026-08-20)

## Code location and migration

**Source code moved from this repository to separate repos**
- Claim: `src/` directory no longer exists in TerAustralis-Incognita; code is in TerAustralis-Incognita-Code and TerAustralis-Incognita-Clementine
- Evidence: Migration completed per Migration-Plan stages 1–2; repository checked 2026-07-23
- Status: Verified, complete
- Details: Executable code moved; governance, architecture, mythos remain in TerAustralis-Incognita
- Reference: `docs/governance/Migration-Plan.md`, `docs/architecture/SystemMap.md`, `STATUS.md`

## Repository structure

**Repository is knowledge/governance/vision hub, not code repository**
- Claim: This repository contains documentation, governance, mythos, and architecture specs; no executable code besides mythos terminals and prototypes
- Evidence: Inspected 2026-08-20; verified all code in separate repos
- Status: Verified
- Reference: `STATUS.md`, `docs/governance/Project-Boundaries.md`, `docs/architecture/SystemMap.md`

---

**For unverified but plausible claims, see `HYPOTHESES.md`. For conflicts between sources, see `CONFLICTS.md`.**
