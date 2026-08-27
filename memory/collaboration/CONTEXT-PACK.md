# CONTEXT-PACK — Essential Context for New Sessions

**Last updated:** 2026-08-27 (session: memory-bootstrap-peiyva)  
**Purpose:** Bootstrap context for Claude Code sessions starting work on this project

## What we're building

**TerAustralis Incognita** — A sovereign, local-first AI platform combining visionary narrative with working software. Two layers: Crystal universe mythos (vision/story) and executable code (moved to separate repos). No pretense; things labeled honestly (Built/Vision/Partial/Planned/Unknown).

## Current branch and work

**Active branch:** `claude/memory-system-bootstrap-peiyva`

**Current work:** Repository Memory Bootstrap
- Creating durable memory system for Claude Code sessions
- Establishes read-write memory protocol (sessions read CORE/CURRENT at startup, update state before ending)
- Preserves Built/Vision distinction per Incognita Rule
- Implements authority hierarchy: Canonical source > verified memory > working context > hypotheses
- Status: 9 core files created; finalizing 6 supporting files; preparing PR for Crystal's review

**Next session:** Finish remaining memory files, verify links/privacy, commit, push, open PR.

## Known gotchas and blockers

**Never do these:**
- Modify locked names (TerAustralis Incognita, CrystalVision, CrystalCore.Lattice) without Constitution amendment
- Edit Constitution, AI-Governance, or Incognita Rule without explicit approval
- Delete or repoint `mythos/` or `docs/` files (they are read-only canon)
- Invent facts or promote hypotheses to verified status without evidence
- Work on main branch (use feature branches only)

**Privacy boundaries:**
- SAT/CrystalCore internals are protected; may reference, never expose internals
- Operator Frame details stay private
- DUR tokens, private lattice fields, credentials: never commit
- Ovaro and Continuum are separate systems; keep them separate

**Repository structure (immutable):**
- `docs/` — Governance, architecture, guides (read-only)
- `mythos/` — Crystal universe content (read-only)
- `research/` — Exploratory work (safe to modify)
- `dbt/` — Emotion warehouse template (safe to modify)
- `archive/` — Provenance only (read-only)
- `src/` — NOT in this repo (moved to separate repos)

## What to read immediately

1. **CLAUDE.md** (root) — Read-write memory protocol and authority hierarchy
2. **memory/CORE.md** — 114-line essential facts about the project
3. **memory/INDEX.md** — Navigation map (what to read for what)
4. **memory/state/CURRENT.md** — Current repository state snapshot

For substantive work:
- `docs/governance/Constitution.md` — Binding law
- `docs/governance/AI-Governance.md` — How AI systems work with this repo
- `docs/ai/AI-Workflow.md` — AI collaboration workflows

## What to do if you're unsure

1. **About authority:** Read Constitution (§1–8), AI-Governance, and Incognita Rule. Disk is canon. Crystal has final veto.

2. **About what's Built vs. Vision:** Check `memory/state/CURRENT.md` and `STATUS.md`. When sources conflict, canonical repository source wins.

3. **About privacy:** Anything mentioning SAT, CrystalCore internals, DUR, Operator Frame, or credentials — keep in `memory/private/` or reference only, never expose details. Ask if unsure.

4. **About project state:** Read `memory/state/` files (DECISIONS, OPEN-QUESTIONS, MILESTONES, CURRENT) and check `docs/governance/Roadmap.md` for priorities.

5. **About AI collaboration:** Read `memory/collaboration/AI-HANDOFF.md` for current seat assignments, then `docs/ai/AI-Workflow.md` for protocol. Every PR names the tools that touched it.

6. **Before ending work:** Update `memory/state/CURRENT.md` and relevant decision/milestone files with your session's changes. Mark date and session ID. Never modify governance files without approval.

## Links to fuller documentation

- Governance: `docs/governance/` (Constitution, AI-Governance, Incognita Rule, Roadmap)
- Architecture: `docs/architecture/` (SystemMap, lattice design, protocol specs)
- AI workflow: `docs/ai/` (AI-Workflow.md, agent instructions)
- Project state: `STATUS.md`, `CHANGELOG.md`
- Mythos: `mythos/` (vision, art, content)

---

**For the full memory protocol, see CLAUDE.md at repository root.**
