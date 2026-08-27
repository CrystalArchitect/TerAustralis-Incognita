# CLAUDE.md — TerAustralis-Incognita Session Bootstrap

**Every Claude Code session must read this file first.**

## Before you do anything

1. **Read** `memory/CORE.md` (essential facts)
2. **Read** `memory/state/CURRENT.md` (repository state right now)
3. **Use** `memory/INDEX.md` for task-specific navigation

Then check the repository canon files referenced in INDEX.md.

## Authority hierarchy (highest to lowest)

1. **Canonical repository source** — `docs/`, `mythos/`, locked names in Constitution
2. **Verified repository memory** — `memory/` files backed by evidence
3. **Your current working context** — the chat, the diff, the branch state
4. **Hypotheses / assumptions** — things labeled as unverified or speculative

When memory conflicts with newer canonical source: follow the canonical source and record the conflict in `memory/evidence/CONFLICTS.md`.

## The read-write protocol

This memory system is **not** read-only. Before ending or checkpointing meaningful work:

- [ ] Update `memory/state/CURRENT.md` if repository state changed
- [ ] Update `memory/state/DECISIONS.md` if a decision was made
- [ ] Update `memory/state/OPEN-QUESTIONS.md` if blockers appeared/resolved
- [ ] Update `memory/state/MILESTONES.md` if progress moved
- [ ] Update `memory/projects/*/CURRENT.md` for active projects you touched
- [ ] Record any new verified facts in `memory/evidence/VERIFIED.md`
- [ ] Record conflicts in `memory/evidence/CONFLICTS.md`
- [ ] Update `memory/collaboration/CONTEXT-PACK.md` if future sessions need to know

**Mark updates with date and your session ID** so they can be audited.

## What you must preserve

- **Built / Vision / Unknown distinctions** (Incognita Rule §1–2)
- **Locked names** (Constitution §1: TerAustralis Incognita, CrystalVision, CrystalCore.Lattice)
- **The Constitution and governance files** — never modify without Crystal's explicit approval
- **Privacy boundaries** — do not expose SAT/CrystalCore internals, Operator Frame, DUR tokens, private lattice fields
- **Crystal's veto** — the human maintainer (Crystal Arena-Turner) has final authority

## What you must never do

- Invent canon or promote hypotheses to verified facts without evidence
- Modify locked names or the Constitution without explicit approval
- Blur the line between Built code and Vision narrative
- Treat AI agreement as proof (Incognita Rule §4)
- Work on `main` — use your designated branch
- Delete or destructively reorganize existing corpus without reason

## If you're unsure

1. Check `memory/INDEX.md` for what to read
2. Read the relevant canonical source
3. Ask yourself: "Is this a Built fact or a Vision statement?"
4. If still unsure: mark it as Unknown/Hypothesis, link to the source, and let it stand

## Quick links

- **Governance**: `docs/governance/Constitution.md`, `docs/governance/AI-Governance.md`
- **Repository state**: `STATUS.md`
- **Roadmap & priorities**: `docs/governance/Roadmap.md`
- **AI workflow**: `docs/ai/AI-Workflow.md`
- **This session's task**: See your prompt or `memory/collaboration/CONTEXT-PACK.md`

---

**Disk is canon. Chat is not. Memory is navigation.**

See `memory/README.md` for the full system design.
