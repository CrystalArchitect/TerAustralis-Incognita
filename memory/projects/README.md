# PROJECTS — Active Project Index

**Status: BUILT** — Index of projects currently in development.

**Last updated:** 2026-08-27 (session: memory-bootstrap-peiyva)

## Active projects (6)

Only substantial, actively worked projects are listed. Exploratory or stalled work goes in research/ or archive/.

### 1. Repository Memory Bootstrap

| Field | Value |
|-------|-------|
| **Status** | In progress (9 of 15 files created) |
| **Branch** | `claude/memory-system-bootstrap-peiyva` |
| **Purpose** | Create durable memory system for Claude Code sessions; establish read-write protocol |
| **Key files** | `CLAUDE.md`, `memory/CORE.md`, `memory/INDEX.md`, `memory/state/*`, `memory/collaboration/*`, `memory/evidence/*` |
| **Owner** | Claude Code sessions (with Crystal's veto) |
| **Next milestone** | Complete 6 remaining files, verify links/privacy, commit, push, open PR |
| **Reference** | This plan in `/root/.claude/plans/you-are-working-inside-pure-spindle.md` |

### 2. CrystalCore.OS Terminal

| Field | Value |
|-------|-------|
| **Status** | Running (verified 2026-07-27) |
| **Location** | `mythos/crystalcore-os/crystalcore_os.py` |
| **Purpose** | Mythos terminal interface — immersive story you can play through |
| **Key files** | `crystalcore_os.py`, story content in `mythos/` |
| **Status marker** | **BUILT** (working software) / **VISION** (narrative layer) |
| **Next milestone** | Content expansion, integration with Story Library |
| **Reference** | `STATUS.md`, `mythos/crystalcore-os/` |

### 3. Story Library Prototype

| Field | Value |
|-------|-------|
| **Status** | Reference implementation built; production pending |
| **Location** | Reference: `research/prototypes/story-library`; Production: TerAustralis-Incognita-Code repo |
| **Purpose** | User-facing story collection interface (web-based) |
| **Built** | HTML prototype with no build step |
| **Pending** | SvelteKit/React production components, integration with teraustralis.com.au |
| **Status marker** | **BUILT** (prototype) / **DESIGNED** (production spec) / **PENDING** (implementation) |
| **Next milestone** | Begin SvelteKit component implementation (Q4 2026) |
| **Reference** | `research/prototypes/story-library/`, `docs/governance/Roadmap.md` |

### 4. Clementine Companion

| Field | Value |
|-------|-------|
| **Status** | Code moved to separate repo; memory system designed, partially implemented |
| **Location** | Code: TerAustralis-Incognita-Clementine repo; Architecture: `mythos/content/MEMORY.md` |
| **Purpose** | Local-first AI companion (Ollama-backed, sovereign, 4-layer memory system) |
| **Memory layers** | Working (active tasks), Episodic (session history), Semantic (knowledge), Reflective (growth) |
| **Status marker** | **VISION** (architecture) / **PARTIAL** (implementation) |
| **Next milestone** | Complete memory layer implementation; integrate with Story Library |
| **Reference** | `mythos/content/MEMORY.md`, TerAustralis-Incognita-Clementine repo |

### 5. DBT Emotion Warehouse

| Field | Value |
|-------|-------|
| **Status** | Project structure complete; no warehouse configured; never run |
| **Location** | `dbt/crystalcore_emotion_warehouse/` |
| **Purpose** | Template for emotion-data pipeline (analytics infrastructure) |
| **Contents** | Staging models, mart models, macros, tests (all templated) |
| **Status marker** | **BUILT** (project skeleton) / **DESIGNED** (spec) / **PENDING** (warehouse setup) |
| **Next milestone** | Configure warehouse (Snowflake/BigQuery), populate test data, validate pipeline |
| **Reference** | `dbt/crystalcore_emotion_warehouse/`, `STATUS.md` |

### 6. CrystalCore Runtime Specifications

| Field | Value |
|-------|-------|
| **Status** | Designed (v0.3); implementations in separate repos |
| **Location** | Specs: `docs/architecture/crystal-core/` (Starline, CrystalBus, RDP, Consent Transport) |
| **Purpose** | Formal protocol specifications for multi-AI communication and consent |
| **Versions** | v0.3 (current); implementations in progress in separate repos |
| **Status marker** | **DESIGNED** (spec complete) / **PARTIAL** (reference implementations) |
| **Next milestone** | Complete implementations in TerAustralis-Incognita-Code; interop testing |
| **Reference** | `docs/architecture/crystal-core/`, `docs/governance/Roadmap.md` |

---

## How to manage this list

**When starting a new project:**
1. Add an entry here with status, location, purpose, key files, and next milestone
2. Create a `memory/projects/PROJECT-NAME/` directory if substantial
3. Link from relevant state files (`DECISIONS.md`, `OPEN-QUESTIONS.md`)

**When a project completes:**
1. Move to historical section (archive or CHANGELOG)
2. Update status to COMPLETE with completion date
3. Link to PR/commit that finished it

**When a project is abandoned or deferred:**
1. Remove from active list
2. Update `memory/state/OPEN-QUESTIONS.md` if blockers exist
3. Archive in `research/` or comment in this file

---

**For project-specific decisions, blockers, and handoffs, create subdirectories: `memory/projects/PROJECT-NAME/{CURRENT.md,PLAN.md,DECISIONS.md,OPEN-QUESTIONS.md,HANDOFF.md}`**
