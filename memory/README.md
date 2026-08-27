# Repository Memory System

**Status: BUILT** — This memory system is durable, persistent, and maintained by all Claude Code sessions.

## What this is

A repository-wide memory system designed for Claude Code sessions to maintain durable context across multiple sessions without relying on chat history.

**This is NOT:**
- Clementine's memory system (see `mythos/content/MEMORY.md` for the AI companion's architecture)
- A replacement for disk-based canon (repository files are primary)
- A substitute for reading governance and architecture documents
- A tool for storing invented facts or hypotheses as verified truth

**This IS:**
- A navigation and state-tracking system
- A way for future sessions to understand the repository quickly
- A living record of decisions, blockers, and progress
- A place to record what we know vs. what we're unsure about

## Structure

### Core navigation
- **`CORE.md`** — Minimal essential facts (read first)
- **`INDEX.md`** — Where to read for what (navigation map)

### Living state
- **`state/CURRENT.md`** — Repository state snapshot (updated each session)
- **`state/DECISIONS.md`** — Dated decisions affecting work
- **`state/OPEN-QUESTIONS.md`** — Blockers and unknowns
- **`state/MILESTONES.md`** — Project progress

### Collaboration
- **`collaboration/AI-HANDOFF.md`** — How AI agents work together
- **`collaboration/CONTEXT-PACK.md`** — Essential context for next session
- **`collaboration/EXTERNAL-RELATIONSHIPS.md`** — Partnerships and boundaries

### Evidence
- **`evidence/VERIFIED.md`** — Facts confirmed by running code or checking sources
- **`evidence/HYPOTHESES.md`** — Plausible but unverified claims
- **`evidence/CONFLICTS.md`** — Places where sources disagree

### Projects
- **`projects/README.md`** — Index of active projects only (no empty stubs)
- **`projects/PROJECT-NAME/`** — Per-project memory (CURRENT, PLAN, DECISIONS, OPEN-QUESTIONS, HANDOFF)

## How to use it

**On arrival (every session):**
1. Read `CORE.md`
2. Read `state/CURRENT.md`
3. Use `INDEX.md` to find what else you need
4. Read the canonical source referenced

**Before leaving (every session):**
- Update `state/CURRENT.md` if repository state changed
- Update `state/DECISIONS.md` if decisions were made
- Update `state/OPEN-QUESTIONS.md` if blockers changed
- Update `state/MILESTONES.md` if progress moved
- Record verified facts in `evidence/VERIFIED.md`
- Record conflicts in `evidence/CONFLICTS.md`
- Update project directories if active projects touched

**Marking updates:**
Always include date (YYYY-MM-DD) and session ID when recording new information, so updates can be audited.

## Authority and validation

Memory files **point to** authoritative sources; they do not replace them.

When memory conflicts with canonical repository source:
1. Follow the canonical source
2. Record the conflict in `evidence/CONFLICTS.md`
3. Update the memory to match

Use the **authority hierarchy** from `CLAUDE.md`:
1. Canonical source > 2. Verified memory > 3. Working context > 4. Hypotheses

## Privacy and scope

**Protected:**
- SAT/CrystalCore internals (may reference, never expose)
- Operator Frame implementation details
- DUR tokens, private lattice fields
- Household details, living-person modeling
- Credentials and secrets

**Public:**
- Architecture, decision logs, governance
- Roadmap and project status
- Built code specifications
- Vision and mythos content

## Maintenance

This system is maintained by every Claude Code session that touches it:
- Create new records as needed
- Update existing records before finishing work
- Mark all updates with date and session ID
- Preserve the Built/Vision/Unknown distinction always
- Link to authoritative sources, don't copy them

Never modify locked names, the Constitution, or governance files without Crystal's explicit approval.

---

**See `CLAUDE.md` at the repository root for the full session bootstrap protocol.**
