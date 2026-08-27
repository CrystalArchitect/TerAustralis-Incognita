# PROJECTS — active project memory, evidence-gated

**Status:** Docs / governance. This file is both the index and the entry
point — a separate `INDEX.md` was deliberately not created here, because
zero projects currently qualify for a subdirectory and a second index
would just be a stub disagreeing with nothing. Add one back if this file
ever needs to split.

## What qualifies for a project subdirectory

Evidence, not a folder existing: a current status doc, recent commits, an
explicit plan, an open branch or PR, or the maintainer naming it active.
Per [`Project-Boundaries.md`](../../docs/governance/Project-Boundaries.md),
this repository (the umbrella) owns **no main application code** —
Clementine, the Starline Weaver, Starline, and CrystalBridge are real,
active, *built* systems, but they live and move in
`TerAustralis-Incognita-Code` and sibling repos, not here. Their status is
already tracked precisely in [`../MILESTONES.md`](../MILESTONES.md),
[`../state/CURRENT.md`](../state/CURRENT.md), and
[`../OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) "Designed, not built" — this
file does not re-derive that picture. Restating it here would just be a
second copy drifting from the first.

## Active in this repository, right now

None. See "Recently concluded" below and "Not active here" further down.

## Recently concluded

### Repository Memory Bootstrap — COMPLETE 2026-08-28

Root `CLAUDE.md` + the `memory/` tree itself. Landed via PR #123, merged
at `3ba08fdcb4e88f5386949bc3cd35a28dcd597fab` with Crystal Arena-Turner's
explicit authorization. This is now foundational repository
infrastructure — the protocol every Claude Code session runs under — not
an ongoing project needing its own memory. No
`memory/projects/repository-memory-bootstrap/` subdirectory was created:
this work's history lives in git (the PR itself) and its current state in
the root files every other session already reads
([`../state/CURRENT.md`](../state/CURRENT.md),
[`../DECISIONS.md`](../DECISIONS.md), [`../MILESTONES.md`](../MILESTONES.md)).
If a future session substantially redesigns this memory architecture,
that work may earn its own project subdirectory at that time — this entry
doesn't reserve one in advance.

## Not active here (tracked in sibling repos or as design-not-built)

For status, do not re-derive — read:

- [`../state/CURRENT.md`](../state/CURRENT.md) — what's Built/Vision/Unknown, now
- [`../MILESTONES.md`](../MILESTONES.md) — dated landings
- [`../OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) — "Designed, not built"
- [`../../docs/governance/Roadmap.md`](../../docs/governance/Roadmap.md) — the Built-layer status page

## When to create a project subdirectory

Only when a genuinely active, substantial piece of work in *this*
repository would otherwise force root-level `DECISIONS.md`/`OPEN-QUESTIONS.md`/
`MILESTONES.md` to carry detail that isn't useful to every other session.
Then, and only then:

```
memory/projects/<project>/
├── README.md          — what/owner/status/canonical sources/privacy
├── CURRENT.md          — current truth only, dated
├── PLAN.md             — ACCEPTED | PROPOSED | BLOCKED | DEFERRED | REJECTED, not a wishlist
├── DECISIONS.md        — date, decision, status, source, reason, consequence
├── OPEN-QUESTIONS.md   — this project's blockers specifically
├── MILESTONES.md       — this project's own dated landings
├── REFERENCES.md       — canonical source paths
└── HANDOFF.md          — lets another session continue without this chat
```

Do not create empty files from this template to look complete. Create only
the files a real handoff would need.
