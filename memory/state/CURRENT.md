# CURRENT

Working picture of **this** repository. Overwrite at each checkpoint.
If this file disagrees with [`STATUS.md`](../../STATUS.md) or a newer
canonical source, the canonical source wins — then fix this file.

**As of:** 2026-08-29 (cross-repo memory model restructured and merged to main via PR #129; memory-state model design hypothesis merged to main via PR #131; Starline Arsenal expanded 13 → 25 models via PR #130, then reconciled to 31 on this branch, not yet merged)
**STATUS.md last updated:** 2026-08-20
**This memory protocol landed on `main` at:** `3ba08fdcb4e88f5386949bc3cd35a28dcd597fab`
(PR #123, merged with Crystal Arena-Turner's explicit authorization)

**Session 2026-08-29 (c, merged to main via PR #130):** Claude Code reviewed Starline Arsenal models (all 13 landing in `.claude/skills/starline-arsenal/` since 2026-08-14, committed in bda45cc). Confirmed complete 4-group structure (Deconstructors, Predictors, Creators, Adaptors) with 13 models total. Files already properly indexed and wired as Claude Code skill. Crystal then directed an expansion from 13 to 25 models, confirming Grok's parallel `starline-arsenal` skill (living only in Grok's own runtime, `/home/workdir/.grok/skills/`, not on Drive or GitHub) had grown past 13 with no write-back yet performed. The exact wording of Grok's additional models could not be retrieved (Grok session out of tokens); Crystal explicitly approved drafting 12 new model cards in the same template — 8 proposed by Claude (Occam's Razor, Root Cause Analysis/5 Whys, Game Theory, Circle of Competence, Analogical/Combinatorial Thinking, OODA Loop, Antifragility, Margin of Safety) plus 4 Crystal named directly (Recursion, Inference, Rhetoric, Persuasion). Added as `models/14-occams-razor.md` through `models/25-persuasion.md`, following the existing 6-part card template (Purpose, CrystalCore mapping, 5 Core Questions, Required Concrete Output, Evidence→Interpretation→Experiment→Record, Anti-Pattern). `INDEX.md` and `SKILL.md` updated to 25 total, version bumped 1.0.0 → 2.0.0. **Label: Vision/drafted, not verified against Grok's actual wording** — if Grok's own 21-model text later surfaces, reconcile names/registers against it per the Incognita Rule and record any conflict here (open question logged in `../OPEN-QUESTIONS.md`).

**Session 2026-08-29 (d, on branch, not yet merged):** Resolved the open verification gate on Starline Arsenal 14–25 (logged in session (c) below and `../OPEN-QUESTIONS.md`). Searched Google Drive directly and found the actual source was not Grok's runtime skill but two independent Claude-authored lineages sitting in Drive, neither aware of the other: a 25-model line (matching what session (c) had drafted, confirmed identical file-for-file by direct diff) and a separate 21-model line with 6 additional models not in the first (Heuristic, Miscalibration, Regression to the Mean, Better-Than-Average, Parable, Philology). Merged the 6 unique additions in as `models/26-heuristic.md` through `models/31-philology.md`, following the same template. `SKILL.md` and `INDEX.md` updated to 31 total, version bumped 2.0.0 → 3.0.0. The 21-model line's dated "Field card" entries referencing a specific real situation and person were excluded per `PRIVACY.md` — operational notes, not general model content. Verification gate in `OPEN-QUESTIONS.md` struck as resolved. **Label: Built (skill content), sourced and verified against Drive originals, not against any Grok runtime text (none was ever found to exist separately from these two Drive lineages).**

**Session 2026-08-29 (a, merged to main via PR #129):** Restructured memory for cross-repo work. Umbrella memory/ is now the primary source of truth for all Claude sessions across TerAustralis-Incognita-Code, TheCrystalVision, and other repos. Sessions read umbrella state at startup, then read repo-specific state if available. CLAUDE.md and memory/projects/ updated accordingly.

**Session 2026-08-29 (b, merged to main via PR #131, 11:46 UTC):** Added [`../MEMORY-STATE-MODEL.md`](../MEMORY-STATE-MODEL.md) — a design hypothesis for how individual memory entries could be labeled (Fact/Interpretation/Inheritance/Revision/Vision/Unknown) and manipulated (Bridge/Carry/Rewrite), for a possible future personal/collective memory system discussed in chat but not yet designed on disk. Explicitly not implemented, not a schema, not a change to this repo's existing memory protocol. Pointers added to `FRAMEWORKS.md` and `CANON-MAP.md`. Also fixed the pre-existing `TheCrystalVision` link-check CI failure on `main` in the same PR (same fix independently made on this branch, PR #130).

**Previous sessions:** (1) Emergency: reverted one-but-many-field content from public main (PR #127). (2) Secured in private TheCrystalVision repo. (3) Simplified README for onboarding clarity (PR #128, draft). (4) Memory bootstrap completed and merged to main (PR #123, dated 2026-08-28).

**History (2026-08-28):** the memory tree carried orphaned duplicate state
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
