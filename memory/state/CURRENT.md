# CURRENT

Working picture of **this** repository. Overwrite at each checkpoint.
If this file disagrees with [`STATUS.md`](../../STATUS.md) or a newer
canonical source, the canonical source wins — then fix this file.

**As of:** 2026-08-28
**STATUS.md last updated:** 2026-08-20
**Main SHA this branch was cut from:** `bdddf0cdf4c2e47f7d517aaf9edbf1a9ba928b08`

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
| This memory protocol | Docs / process, **unmerged** on this branch | this PR |

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
- Do not merge this branch. The maintainer merges.
- Do not amend the Constitution, locked names, or NAMES.md without
  Crystal's explicit approval.
- Do not promote ADR-0012 or ADR-0016 to Accepted until they merge.
- Do not put personal-layer material in this file ([`PRIVACY.md`](../PRIVACY.md)).
- Do not treat a Grok App Builder sandbox as CrystalCore.OS or as the estate.

## Unverified from this session

Facts offered in chat or in an external dossier that were **not** written
here because they are not on disk, or because PRIVACY forbids them, are
listed in the PR body — not in this file.
