# CURRENT

Working picture of **this** repository. Overwrite at each checkpoint.
If this file disagrees with [`STATUS.md`](../../STATUS.md) or a newer
canonical source, the canonical source wins — then fix this file.

**As of:** 2026-09-05 (Roadmap #7 Small Council mechanism decided — Option D, Prototype Demonstration; six-component Phase 2 technical pitch drafted (three CVD diamond parts + a three-part high-heat engine assembly); a real Lynas/Iluka ticker mix-up caught and corrected by Crystal directly on the branch before merge; real outreach sent to Iluka, AR3+ANSTO, and Liquid Instruments; a broken internal link found by CI and fixed; merged to main via PR #162)
**Previous:** 2026-09-04 (cloud estate inventory attempted; GitHub ContextGate PR #124 and flag PR #152 both merged; Supabase project restored to COMING_UP; network egress policy confirmed: AWS/Firebase APIs whitelisted, Railway/ClickHouse/Azure/external websites blocked; AWS credentials InvalidClientTokenId (awaiting card verification); xAI Colossus clarified as Cloud Service Agreement resource, not public API endpoint)
**STATUS.md last updated:** 2026-08-20
**This memory protocol landed on `main` at:** `3ba08fdcb4e88f5386949bc3cd35a28dcd597fab`
(PR #123, merged with Crystal Arena-Turner's explicit authorization)

**Session 2026-08-29 (c, merged to main via PR #130):** Claude Code reviewed Starline Arsenal models (all 13 landing in `.claude/skills/starline-arsenal/` since 2026-08-14, committed in bda45cc). Confirmed complete 4-group structure (Deconstructors, Predictors, Creators, Adaptors) with 13 models total. Files already properly indexed and wired as Claude Code skill. Crystal then directed an expansion from 13 to 25 models, confirming Grok's parallel `starline-arsenal` skill (living only in Grok's own runtime, `/home/workdir/.grok/skills/`, not on Drive or GitHub) had grown past 13 with no write-back yet performed. The exact wording of Grok's additional models could not be retrieved (Grok session out of tokens); Crystal explicitly approved drafting 12 new model cards in the same template — 8 proposed by Claude (Occam's Razor, Root Cause Analysis/5 Whys, Game Theory, Circle of Competence, Analogical/Combinatorial Thinking, OODA Loop, Antifragility, Margin of Safety) plus 4 Crystal named directly (Recursion, Inference, Rhetoric, Persuasion). Added as `models/14-occams-razor.md` through `models/25-persuasion.md`, following the existing 6-part card template (Purpose, CrystalCore mapping, 5 Core Questions, Required Concrete Output, Evidence→Interpretation→Experiment→Record, Anti-Pattern). `INDEX.md` and `SKILL.md` updated to 25 total, version bumped 1.0.0 → 2.0.0. **Label: Vision/drafted, not verified against Grok's actual wording** — if Grok's own 21-model text later surfaces, reconcile names/registers against it per the Incognita Rule and record any conflict here (open question logged in `../OPEN-QUESTIONS.md`).

**Session 2026-08-29 (d, merged to main via PR #137):** Resolved the open verification gate on Starline Arsenal 14–25 (logged in session (c) below and `../OPEN-QUESTIONS.md`). Searched Google Drive directly and found the actual source was not Grok's runtime skill but two independent Claude-authored lineages sitting in Drive, neither aware of the other: a 25-model line (matching what session (c) had drafted, confirmed identical file-for-file by direct diff) and a separate 21-model line with 6 additional models not in the first (Heuristic, Miscalibration, Regression to the Mean, Better-Than-Average, Parable, Philology). Merged the 6 unique additions in as `models/26-heuristic.md` through `models/31-philology.md`, following the same template. `SKILL.md` and `INDEX.md` updated to 31 total, version bumped 2.0.0 → 3.0.0. The 21-model line's dated "Field card" entries referencing a specific real situation and person were excluded per `PRIVACY.md` — operational notes, not general model content. Verification gate in `OPEN-QUESTIONS.md` struck as resolved. **Label: Built (skill content), sourced and verified against Drive originals, not against any Grok runtime text (none was ever found to exist separately from these two Drive lineages).**

**Session 2026-08-29 (e, merged to main via PR #137):** Extended verification to the full 31, per direct request. Fetched models 1–13 fresh from the "Starline Arsenal Models" Drive folder (these pre-date both lineages, landed 2026-08-14) and confirmed byte-identical to on-disk — the last unchecked slice of the armoury. Re-reading the 21-model line's actual source text (not just its per-model excerpts already merged) surfaced two real fidelity gaps: `models/30-parable.md` was missing the source's explicit "no borrowed lyrics" rule, and `models/21-rhetoric.md` / `models/25-persuasion.md` had kept the plainer 25-model-line wording where the 21-model line held a richer, later-dated (29 Aug) version — five rhetorical canons plus the ethos/pathos/logos/kairos appeal square, and an explicit "honest no" step in Persuasion instead of just objection-handling. All three fixed; governance gained the Speech Rule from the same source. `SKILL.md` version bumped 3.0.0 → 3.1.0. No model IDs, slugs, or groups changed. **Label: Built (skill content), all 31 models now checked against a Drive source; where two sources existed for one model, the more complete is what ships.**

**Session 2026-08-29/30 (f, merged to main via PR #137, 2026-08-30 03:01 UTC):** A separate, concurrent Claude Code session opened PR #138 independently, adding `memory/ETYMOLOGY-STACK.md` (a 10-tier evidence-grading method for word-origin claims, generalizing the ad hoc fact-checking already in `LANGUAGE-AS-PROGRAMMING.md`) and a corresponding 26th Starline Arsenal model, "Provenance Stack" — built on top of the old 25-model `main`, unaware this branch had already reconciled to 31 models and claimed 26–31 for six different models (the same kind of collision PR #130 caused earlier in the day). Rather than let it surface as a merge conflict, absorbed PR #138's content directly onto this branch instead of waiting: `ETYMOLOGY-STACK.md` added verbatim, its model renumbered to `models/32-provenance-stack.md` (content unchanged apart from the renumber and updated self-links), and the same four cross-reference sections it proposed added to `01-first-principles.md`, `14-occams-razor.md`, `18-circle-of-competence.md`, `19-inference.md`. `SKILL.md`/`INDEX.md` bumped 31 → 32 models, version 3.1.0 → 3.2.0. PR #138 itself was not touched (not pushed to, not closed) — it belongs to a different session; now that #137 has merged, PR #138 shows a real merge conflict (`mergeable_state: dirty`) as expected — resolving or closing it is the maintainer's call, not this session's. **Label: Built (skill content), Provenance Stack's method and content unverified against any Grok text (same status PR #138 itself claimed) — the renumber and cross-references are this session's own reconciliation work, not independently verified.**

**Session 2026-08-29 (a, merged to main via PR #129):** Restructured memory for cross-repo work. Umbrella memory/ is now the primary source of truth for all Claude sessions across TerAustralis-Incognita-Code, TheCrystalVision, and other repos. Sessions read umbrella state at startup, then read repo-specific state if available. CLAUDE.md and memory/projects/ updated accordingly.

**Session 2026-08-29 (b, merged to main via PR #131, 11:46 UTC):** Added [`../MEMORY-STATE-MODEL.md`](../MEMORY-STATE-MODEL.md) — a design hypothesis for how individual memory entries could be labeled (Fact/Interpretation/Inheritance/Revision/Vision/Unknown) and manipulated (Bridge/Carry/Rewrite), for a possible future personal/collective memory system discussed in chat but not yet designed on disk. Explicitly not implemented, not a schema, not a change to this repo's existing memory protocol. Pointers added to `FRAMEWORKS.md` and `CANON-MAP.md`. Also fixed the pre-existing `TheCrystalVision` link-check CI failure on `main` in the same PR (same fix independently made on this branch, PR #130).

**Session 2026-09-05 (i, merged to main via PR #162):** Roadmap #7 (Small Council, Engagement & Network Reality) mechanism decided: after confirming the previously assumed verification mechanisms (Standards Australia, ASA public consultation) don't exist or have closed, selected **Option D — Prototype Demonstration**, a real engineering co-development replacing external certification. Drafted a Phase 2 technical pitch: a six-component proof-of-concept suite (CVD diamond thermal spreader, frequency resonator, RF window; plus a three-part high-heat engine assembly — combustion chamber, nozzle insert, ceramic thermal liner) proposed through an Iluka Resources → ANSTO/AR3 → Liquid Instruments sourcing narrative (framing only, matching the canon one-pager — not a reported partnership). **Real error caught in review:** the initial draft misnamed the mineral-stage company "Lynas Rare Earths (ASX: ILU)" — ILU is Iluka Resources' ticker (Lynas is LYC); Crystal corrected it directly on the branch before merge (same error class as the earlier Magellan mistake). **Outreach sent** (2026-09-05, Crystal-approved) from `teraustralis.incognita@gmail.com` to Iluka, AR3+ANSTO, and Liquid Instruments using the corrected framing — thread IDs recorded in the PR #162 comment thread. CI's internal-link checker caught a broken relative path in `memory/DECISIONS.md`, fixed before merge. Full detail: `memory/MILESTONES.md` 2026-09-05 entry, `memory/projects/90-Day-Roadmap/CURRENT.md`. **Label: Built (the outreach send is real, verified against the operator's own PR comment); Vision/proposal (the six-component suite itself — no company has committed to build anything).**

**Session 2026-09-04 (h, cloud estate inventory & network policy audit):** Attempted to generate read-only cloud estate inventory across five providers (AWS, Azure, Firebase, Railway, ClickHouse) with multi-session PR monitoring and Supabase project restoration. **GitHub PRs (concurrent monitoring):** ContextGate v0.1.0 tool (TerAustralis-Incognita-Code PR #124) and fabrication pattern flag (TerAustralis-Incognita PR #152) both merged cleanly to `main` by 2026-09-04 08:10 UTC. Deleted 3-hour check-in routine once both closed. **Supabase project restoration:** Project `riwctuzpwaknkvihpbab` (ap-southeast-2, Postgres 17.6.1.147) transitioned from INACTIVE to COMING_UP after restore call; schema queryable once status reaches ACTIVE. **Network egress policy confirmed (blocking):** Organization-level proxy at `127.0.0.1:37131` enforces an allowlist. AWS API ✅, Firebase/GCP ✅; Railway ❌, ClickHouse ❌, Azure management ❌, external websites ❌ (verified via both Bash curl and WebFetch tool). No workaround available from this session. **AWS credentials:** InvalidClientTokenId returned (key expired, rotated, or missing session token); user to verify/regenerate on AWS side after card verification. **xAI Colossus:** Clarified as Cloud Service Agreement (CSA) resource, not a public API endpoint. Colossus campus infrastructure (Memphis/Southaven, training layers) is sales-team-gated. Public inference routes (api.x.ai + regional variants) are the documented end-user access point. **Pending:** AWS credential verification (card hold); Firebase service account JSON generation (if pursuing after network policy confirmation); Supabase status poll (when reaching ACTIVE). **Label: Built (network audit complete and documented), Unknown (cloud estate pending credential fix), Vision (Colossus infrastructure distinction clarified).**

**Session 2026-09-02 (g, comprehensive workspace audit):** Conducted full GitHub code documentation audit, Drive asset inventory, and memory system consistency cross-check. **GitHub:** 21 source files verified, all critical modules (cross_attention_fusion, active_learning, training_pipeline, emotional_intelligence, uncertainty_quantification) documented, zero TODO/FIXME markers, code documentation status complete. **Drive:** 200 total files paginated, 24 key assets catalogued across three categories — Category A BUILT (Clementine, CrystalCore, 10 assets dated 2026-08-29 to 2026-08-31), Category B PROPOSAL (7 strategic proposal docs, May-August 2026), Category C CODEX (7 Atlas/Codex vision assets). **Memory consistency:** GitHub docs audit aligns with existing documentation, Starline Arsenal 32-model structure confirmed, kit-skills tracking updated (8 of 10 now tracked: added `cich-framework`, `the-catch`, `pep8-python-reviewer` to FRAMEWORKS.md; 2 unconfirmed pending Grok ecosystem validation). New findings logged: CVSC collection (Sept 1-2, 15+ docs), Dharawal research thread (Sept 1, 6+ docs), Continuum x SAT working doc, Celestial Portal Build doc. **External blockers:** teraustralis.com.au returns 403 Forbidden (remote network restriction); Google Photos API unavailable (no direct access). Audit conclusions: workspace documentation complete on-disk, Drive inventory current and tagged, memory system consistent with repository state. **Label: Built (verification complete, external scope blocked by network/API constraints).**

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
| 90-Day Public Roadmap (Aug 30 → Nov 28, 2026), Crystal's public accountability plan | Vision/commitment; #7's mechanism decided and real outreach sent 2026-09-05, other items mixed drafted/shipped/not-started | `memory/projects/90-Day-Roadmap/`, 2026-08-30; PR #162, 2026-09-05 |

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
