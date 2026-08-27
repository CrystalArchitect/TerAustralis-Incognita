# HYPOTHESES — Plausible but Unverified Claims

**Status: EXPLORATORY** — These are reasonable but not yet confirmed. Never treat them as fact.

## Infrastructure and scaling

**DUR token architecture will scale beyond current proof-of-concept**
- Status: Designed, partially implemented; PoC working
- Would be verified by: Running at production data volume; benchmarking under load; comparing against alternatives
- Priority: Medium (blocking Lattice scaling, not immediate blocker)
- Reference: `docs/architecture/crystal-core/` (DUR specification); `docs/governance/Roadmap.md`

**Emotion-warehouse dbt pipeline meets live data requirements**
- Status: dbt project built; no warehouse configured; never run against real data
- Would be verified by: Configuring warehouse (Snowflake, BigQuery, etc); running pipeline on production data; monitoring performance and data freshness
- Priority: Medium (designed for future phases)
- Reference: `dbt/crystalcore_emotion_warehouse/`; `STATUS.md`

## Deployment and delivery

**Story Library production components can be delivered within planned timeline**
- Status: Reference implementation complete; production spec designed; no production code yet
- Would be verified by: Building SvelteKit/React components; integrating with teraustralis.com.au; collecting user feedback
- Priority: High (on Roadmap for next quarter)
- Reference: `research/prototypes/story-library` (reference); `docs/governance/Roadmap.md`

**Workflow prompt kits will integrate cleanly with Claude Code and Zapier**
- Status: Kits designed and written; no integration code yet
- Would be verified by: Wiring kits to execution layer (Claude Code, Zapier); running in production; measuring success metrics
- Priority: Medium (designed, awaiting implementation)
- Reference: `mythos/tools/` (daily-digest, signal-scanner kits); `docs/ai/AI-Workflow.md`

## Cultural and metaphorical

**Songline metaphor translates effectively to non-Australian teams**
- Status: Metaphor used in vision work; not tested with diverse audiences
- Would be verified by: Gathering feedback from teams outside Australia; measuring comprehension and resonance; iterating on explanations
- Priority: Low (vision-layer concern, not infrastructure blocker)
- Reference: `mythos/` (vision content using Songline metaphor); `memory/collaboration/EXTERNAL-RELATIONSHIPS.md`

---

**For confirmed facts, see `VERIFIED.md`. For conflicts between sources, see `CONFLICTS.md`.**

**Process: When a hypothesis becomes verified (through testing, deployment, or measurement), move it to `VERIFIED.md` with evidence. When a hypothesis fails or is abandoned, archive it in a comment or separate doc.**
