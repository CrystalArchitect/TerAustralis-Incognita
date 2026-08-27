# PROJECTS — active project memory, evidence-gated

**Status:** Docs / governance. This file is both the index and the entry
point — a separate `INDEX.md` was deliberately not created here, because
one project currently qualifies and a second index would just be a stub
disagreeing with nothing. Add one back if this file ever needs to split.

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

### Repository Memory Bootstrap

| Field | Value |
|---|---|
| Status | In progress — open PR, unmerged |
| Branch | `claude/memory-system-bootstrap-peiyva` |
| PR | #123 |
| Purpose | Root `CLAUDE.md` + this `memory/` tree: a read-and-write durable memory protocol for Claude Code sessions |
| Owner | Claude Code sessions, with the maintainer's merge decision as the gate |
| Canonical sources | This memory tree itself; [`../../CLAUDE.md`](../../CLAUDE.md); [`ADR-0014`](../../docs/adr/ADR-0014.md) (does not restore the seat this protocol's sessions use) |
| Privacy | Public (repository-internal governance/process) |
| Next action | See [`../state/CURRENT.md`](../state/CURRENT.md) "Now" and this file's own git history for the latest checkpoint — this is the one project in this repository still changing fast enough that a static snapshot here would go stale between sessions |

No dedicated `memory/projects/repository-memory-bootstrap/` subdirectory
was created for this: the work's current truth already lives in
`state/CURRENT.md`, its decisions in `DECISIONS.md`, and its open
questions in `OPEN-QUESTIONS.md` — the same root-level files every other
session reads. A project subdirectory earns its keep once a *second*
in-repository project needs its own PLAN/DECISIONS/HANDOFF set that would
otherwise crowd the root files with detail only that project cares about.
That has not happened yet.

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
