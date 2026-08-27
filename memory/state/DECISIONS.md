# DECISIONS — Decisions Affecting This Project

**Status: BUILT** — These decisions are from repository canon (ADRs, Constitution amendments, commits, PRs).

## Recent decisions (2026)

**2026-08-20** — Grok Build holds Repository Engineer seat · `docs/adr/ADR-0014.md` · Impact: Claude's historical operating instructions remain in `docs/agents/Claude-Agent.md` as archive; Grok Build is the current repository engineer. Claude sessions should follow Grok.md guidance for current practice.

**2026-07-23** — Locked name correction: "TeraAustralis" → "TerAustralis" (one 'a') · `docs/adr/ADR-0007.md` · Impact: All future uses of the name match the maintainer's ABN trading name. `mythos/teraustralis/` directories renamed to match.

**2026-07-23** — CrystalCore OS v1.0 repository reorganization · `docs/adr/ADR-0001.md`, `docs/adr/ADR-0002.md` · Impact: File structure realigned; src/ moved out; Constitution moved to docs/governance/. Lattice design sketch moved to docs/architecture/lattice/.

**2026-07-23** — Lattice-delta machinery marked designed-not-built · Constitution amendment · Impact: Until Lattice deltas are built, use normal git commits for substantial work. Weave Map, singularity gates, board infrastructure is vision, not infrastructure yet.

**2026-07-21** — No new GitHub repositories without ADR · `docs/adr/ADR-0015.md` · Impact: Future work lands in Code, Clementine, the proposal repo, or this umbrella—not new repos. Reduces fragmentation.

**2026-07-23** — Migration plan stages 1–2 completed · `docs/governance/Migration-Plan.md` · Impact: src/ code moved; publish-packages and test-packages workflows removed by design. Code now in TerAustralis-Incognita-Code, TerAustralis-Incognita-Clementine.

## Locked decisions (Constitution §8 amendments)

These are binding until amended through the Constitution amendment process.

**TerAustralis Incognita** — Locked name (outer civilizational vision)  
**CrystalVision** — Locked name (sensing/dreaming/directing interface)  
**CrystalCore.Lattice** — Locked name (substrate multi-AI weave)

See `docs/governance/Constitution.md` for amendment process.

## Project boundaries

**In-scope for this repository:**
- Governance and decision records
- Architecture and protocol specifications
- Mythos content (vision, art, story)
- Research and exploratory work
- dbt project skeleton (emotion warehouse template)

**Out-of-scope (separate repos):**
- Executable code (moved to TerAustralis-Incognita-Code, etc.)
- Live applications
- Runtime environments

See `docs/governance/Project-Boundaries.md` and `docs/architecture/SystemMap.md`.

## AI collaboration decisions

**Per `docs/ai/AI-Workflow.md`:**
- Every flow ends at the repository through a pull request
- No AI output is canon until merged
- Handoffs happen through artifacts, not vibes
- Every PR names the tools that touched it
- Chaining AIs multiplies fluency, not truth

**Per `docs/governance/AI-Governance.md`:**
- Disk is canon, chat is not
- Label honestly (Built/Vision)
- Name your tools in PRs
- No false sacred (fire-circle ethic)
- Crystal keeps the veto

## Unresolved / TBD

None currently escalated.

---

For the full decision record, see:
- `docs/adr/` — Architecture Decision Records
- `docs/governance/Decision-Records.md` — How to record decisions
- `CHANGELOG.md` — Chronological commit record

Authority: `docs/governance/Constitution.md` (§8 for amendment process)
