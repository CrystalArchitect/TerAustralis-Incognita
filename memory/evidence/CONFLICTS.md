# CONFLICTS — where sources disagree

**Status:** Docs / governance. Record disagreements here instead of
silently picking a winner. Do not close an entry from chat — closing
requires an on-disk resolution (a fix, an ADR, or the maintainer settling
it), same as [`../OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md)'s write-back
rule.

## Open

**Archive: `crystalcore/` vs `crystalcore-v0.13/` recovery framing** ·
Also flagged in [`../OPEN-QUESTIONS.md`](../OPEN-QUESTIONS.md) Tier 3 as
"Drift."
- **What each file claims:** `archive/2026/local-snapshot-2026-07-17/README-SNAPSHOT.md`
  calls the sibling `crystalcore/` folder (32 exports, no `status.py`, no
  SpaceXAI provider) a "complete, working package." `crystalcore-v0.13/RECOVERY-STATUS.md`
  calls *its own* folder (44 exports, includes `status.py` and
  `spacexai.py`) "COMPLETE and verified," and states explicitly that it
  **supersedes** the sibling `crystalcore/` folder ("nothing here is
  missing anymore").
- **On closer read, this is less a factual contradiction than an
  unresolved framing tension:** both folders are internally consistent
  about their own scope (each accurately describes what it recovered), and
  the later file already asserts a supersession relationship. What is
  actually unresolved is whether the earlier `README-SNAPSHOT.md` should
  be edited to point at the supersession, or left as written since it
  predates the v0.13.4 recovery and archive material is not to be rewritten
  for tidiness (`archive/README` — provenance, not production).
- **Authority:** neither file outranks the other; both are archive
  provenance, not current canon. Do not build on either.
- **Status:** Open, low stakes (archive-only). Not blocking anything
  observed in this branch's work.
- **Resolution owner:** the maintainer, if it's worth touching at all —
  archive rewrites are explicitly discouraged by this repository's own
  practice.

## How to log a new conflict

```
**Topic**
- What each source claims, with paths
- Authority: which source outranks, or "neither — escalate"
- Status: Open | Resolved | Deferred
- Resolution owner: maintainer | next session | n/a
```

## Resolved

None yet.
