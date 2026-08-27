# OPEN-QUESTIONS — Unknowns and Blockers

**Status: BUILT** — These are genuine unknowns, not hypotheses.

## Completely resolved (historical)

**2026-08-20:** "Is the SvelteKit site actually live?" — **VERIFIED**  
Domain www.teraustralis.com.au returns 200 with SvelteKit build (last-modified 2026-08-18). Probe passed at 20:28, 20:33, 20:39 UTC. Code repo owns CNAME and Pages settings.

**2026-07-28:** "Where is the code?" — **VERIFIED**  
Code moved to TerAustralis-Incognita-Code (site, apps) and TerAustralis-Incognita-Clementine. `docs/architecture/SystemMap.md` documents the move.

## Currently unknown

None escalated.

## Design decisions awaiting implementation

**Lattice-delta mechanism**
- Status: **DESIGNED, NOT BUILT** (Constitution §3–4)
- What: Time-stamped evolution records, Weave Map, singularity gates
- Why needed: Track multi-AI changes, gate-based activation
- Blocker: Requires software implementation
- Reference: `docs/architecture/lattice/BOOT_STATUS.md`

**Production Story Library components**
- Status: **DESIGNED, NOT BUILT**
- What: SvelteKit/React components for live story site
- Reference: `research/prototypes/story-library` (reference implementation)
- Next: Implement from spec, integrate with teraustralis.com.au

**Workflow prompt kits integration**
- Status: **DESIGNED, NOT BUILT** (written as kits, wired to nothing)
- What: daily-digest, signal-scanner workflows
- Location: `mythos/tools/`
- Next: Wire to Claude Code, Zapier, or other execution layer

## Hypothetical uncertainties

(Things that might be true but we haven't verified—see `memory/evidence/HYPOTHESES.md` for full treatment)

- Whether DUR token architecture will scale beyond current proof-of-concept
- Whether the emotion-warehouse dbt pipeline meets live data requirements
- Whether Songline metaphor translates effectively to non-Australian teams

---

## What to do if you discover a new unknown

1. Add it here with:
   - What you don't know
   - Why it matters
   - Where you discovered it
   - What would verify it

2. Mark status: Blocked | Waiting | Blocked-on-Crystal | Unknown | Verifying

3. Link to relevant issue/PR/doc

4. Before leaving, update this file with what you learned

---

See also:
- `memory/evidence/HYPOTHESES.md` (plausible but unverified claims)
- `memory/evidence/CONFLICTS.md` (where sources disagree)
- `docs/governance/Roadmap.md` (what we're working on to address unknowns)
