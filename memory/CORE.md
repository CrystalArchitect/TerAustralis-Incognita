# CORE — Essential Facts

**Status: BUILT** — These are verified facts from repository canon.

## What this project is

**TerAustralis Incognita** is two things kept honestly separate:

1. **Working software** — a local-first AI companion (Clementine), multi-AI message bus (Starline Weaver), peer-to-peer memory exchange (Consent Transport), record kernel (RDP). Code in separate repos.

2. **A mythos** — the Crystal universe: story, art, vision, speculative framing. Canon in `mythos/` and `docs/vision/`.

Nothing pretends to be more built than it is. Where the two meet, code is the source of truth.

**Status per `STATUS.md` (2026-08-20):**
- Running: CrystalCore.OS terminal, research prototypes
- Built not running: dbt emotion warehouse, archived code
- Document: architecture specs, governance, mythos content
- Designed not built: production story library components, protocol implementations (code elsewhere)

## Human authority

**Crystal Arena-Turner** is the human maintainer and authority.

The Constitution is binding. Crystal's veto is final. No AI, persona, or archetype gets the final say.

## Locked names (Constitution §1)

| Name | What it is |
|------|-----------|
| **TerAustralis Incognita** | The complete vision — all three layers |
| **CrystalVision** | Sensing/dreaming/directing interface |
| **CrystalCore.Lattice** | Substrate — multi-AI weave, memory, ontology |

These are locked. Do not rename without explicit Constitution amendment.

## The Incognita Rule

Mark which lines are **dreamed** (vision, story, art) and which are **surveyed** (running code, tested, checkable fact). Never let dreamed lines pretend to be measured.

- **Built** — running, tested code or verified fact
- **Vision** — narrative, art, speculative framing
- **Partial** — partially implemented
- **Planned** — designed, not yet built
- **Unknown** — we don't know yet

This is load-bearing. Blur it at your peril.

## Privacy boundaries

**Protect:**
- SAT/CrystalCore internals (may reference, never expose)
- Operator Frame details
- DUR tokens, private lattice fields
- Credentials, secrets

**Separate systems:**
- **Ovaro** — CMX's agency/shopfront (separate from TerAustralis)
- **Continuum** — CMX product (separate)
- **TerAustralis/SAT/CrystalCore** — Crystal's work (separate from Ovaro/Continuum)

## Governance authority

Read these in order:

1. `docs/governance/Constitution.md` — binding law
2. `docs/governance/AI-Governance.md` — how AI systems work with this repo
3. `docs/governance/The-Incognita-Rule.md` — honesty discipline
4. `AGENTS.md` (root) — how to work on this project

**Key rules:**
- Disk is canon, chat is not
- Label honestly (Built/Vision)
- Name your tools (in PR descriptions)
- No false sacred (fire-circle ethic)
- Crystal keeps the veto

## Repository structure

| Path | What | Status |
|------|------|--------|
| `docs/` | Governance, architecture, AI workflow, agents, ADRs, guides | Built |
| `mythos/` | Crystal universe canon, art, tools, outer lore | Vision + Built |
| `research/` | Exploratory work, seven-sisters cycle | Exploratory |
| `dbt/` | Emotion warehouse dbt project | Built structure |
| `archive/` | Provenance only; never build on it | Historical |
| `src/` | All executable code | **NOT in this repo** (moved to separate repos) |

Code lived here; it now lives in TerAustralis-Incognita-Code and other repos. See `STATUS.md` for full detail.

## What to read next

- For context: `STATUS.md` (what's built/running/designed)
- For direction: `docs/governance/Roadmap.md`
- For this session: `memory/state/CURRENT.md` and `memory/INDEX.md`
- For your role: `docs/governance/AI-Governance.md`

## Active projects (summary)

See `memory/projects/README.md` for full detail.

1. Repository Memory Bootstrap (this work)
2. CrystalCore.OS Terminal (running, verified)
3. Story Library Prototype (built, production pending)
4. Clementine Companion (code elsewhere)
5. DBT Emotion Warehouse (built structure, not running)
6. CrystalCore Runtime Specs (designed v0.3, code elsewhere)

---

**This is the bootstrap layer. Read it once per session, then use `memory/INDEX.md` to navigate deeper.**

For the full memory protocol, see `CLAUDE.md` at the repository root.
