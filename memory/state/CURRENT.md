# CURRENT

Working picture of **this** repository. Overwrite at each checkpoint.
If this file disagrees with [`STATUS.md`](../../STATUS.md) or a newer
canonical source, the canonical source wins — then fix this file.

**As of:** 2026-08-28 (post-emergency-revert, onboarding simplification merged; frameworks map pending on grok/memory-frameworks-map)
**STATUS.md last updated:** 2026-08-20
**This memory protocol landed on `main` at:** `3ba08fdcb4e88f5386949bc3cd35a28dcd597fab`
(PR #123, merged with Crystal Arena-Turner's explicit authorization)

**This session:** (1) Emergency: reverted one-but-many-field content from public main (PR #127). (2) Secured in private TheCrystalVision repo. (3) Simplified README for onboarding clarity (PR #128, draft).

**History (same day):** the memory tree carried orphaned duplicate state
files from an earlier, less-grounded implementation pass, and a handful
of unverified or fabricated citations (a nonexistent "DUR specification"
reference; an Ovaro/Continuum/CMX boundary with no on-disk source at the
time). A reconciliation pass fixed both, then Crystal reviewed and
directly resolved the three items that reconciliation had flagged as
requiring her decision — recorded in
[`../DECISIONS.md`](../DECISIONS.md) "Direct maintainer decisions" and
[`../evidence/CONFLICTS.md`](../evidence/CONFLICTS.md). Full account:
[`../MILESTONES.md`](../MILESTONES.md).

## Now

| Item | Label | Source |
|---|---|---|
| This git is the umbrella (canon, governance, mythos). No main app code. | Built (as a docs repo) | ADR-0011, STATUS, README |
| `src/` is **not** in this git and never was | Built (negative fact) | README status note, SystemMap |
| Public site is live from `TerAustralis-Incognita-Code` (www 200, apex 301) | Built, measured 2026-08-20 | STATUS |
| CrystalCore.OS mythos terminal runs from a fresh clone of *this* repo | Vision software that runs | STATUS, README Quick start |
| Lattice-delta / Weave-Map / gate board | Designed, **not built** | Constitution implementation note |
| Grok Build holds the Repository Engineer seat | Built (governance) | ADR-0014, AGENTS.md |
| Claude Code is not in the weave; profile retained as history | Built (governance) | ADR-0014, `docs/ai/Claude.md` |
| No new GitHub repository without an ADR | Built (governance) | ADR-0015 |
| `samuelsalmon3/SourceCode` is an external peer, not a module | Vision until ADR-0016 merges | ADR-0016 **Proposed** |
| License: uniform CC BY-NC-ND 4.0 | Built (legal) | ADR-0010, ADR-0013 |
| Locked names: TerAustralis Incognita · CrystalVision · CrystalCore.Lattice | Built (law) | Constitution §1 |
| Songline is never a component name | Built (law) | NAMES.md, Indigenous-Data-Sovereignty.md |
| This memory protocol (root `CLAUDE.md` + `memory/`) | Built (docs / process), **live on `main`** | PR #123, merged 2026-08-28 |
| CMX/Ovaro/Continuum external boundary | Built (governance, memory-recorded) | `memory/DECISIONS.md` "Direct maintainer decisions," 2026-08-28 |
| Frameworks retrieval map (`memory/FRAMEWORKS.md`) | Docs / process. **On this PR, not `main` until merged.** Points; does not dump Drive papers. | this branch, 2026-08-28 |

## Seats

- **Maintainer / human veto:** Crystal. Unchanged.
- **Repository Engineer:** Grok Build. Boundaries travel with the seat:
  no push to `main`, no history rewrite, no locked-name changes, no
  silent edits to another contributor's Vision-layer content, no merge.
- **Creative Grok:** separate seat. Does not implement.
- **Claude Code:** historical. A session that runs anyway follows
  [`CLAUDE.md`](../../CLAUDE.md) and writes back here. That is not a seat
  restore.

## What you can run from a clone of *this* repo

From STATUS and README:

- `python3 mythos/crystalcore-os/crystalcore_os.py` — mythos terminal
- `research/prototypes/story-library` — self-contained HTML
- CI on main: markdown lint and links. Python tests live in `-Code`.

Clementine, Starline Weaver, Consent Transport, RDP, CrystalBridge
self-tests: described for the code tree / `-Code`. They will **not** run
from a fresh clone of this umbrella.

## dbt

`dbt/crystalcore_emotion_warehouse` exists here as a full dbt project.
No warehouse is configured. Not executed (STATUS). Treat as **Built, not
currently running** / **Unknown** as a data product.

## Site pipeline

```
mythos/ (this repo, canonical)
  → manual copy → vision/site/src/content/ (Code)
  → deploy.yml → GitHub Pages → www.teraustralis.com.au
```

New canon is not public until the copy step happens. That sync method is
still an open decision.

## Do not do

- Do not create a twentieth GitHub repository (ADR-0015).
- Do not merge a PR on your own initiative. The maintainer merges, or
  gives explicit, dated, in-session authorization to do so — as happened
  for PR #123 (2026-08-28). That authorization was specific to that PR,
  not a standing grant.
- Do not amend the Constitution, locked names, or NAMES.md without
  Crystal's explicit approval.
- Do not promote ADR-0012 or ADR-0016 to Accepted until they merge.
- Do not put personal-layer material in this file ([`PRIVACY.md`](../PRIVACY.md)).
- Do not treat a Grok App Builder sandbox as CrystalCore.OS or as the estate.

## Unverified from this session

Facts offered in chat or in an external dossier that were **not** written
here because they are not on disk, or because PRIVACY forbids them, are
listed in the PR body — not in this file.
