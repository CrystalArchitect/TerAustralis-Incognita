# MILESTONES

Dated landings. Canonical sources:
[`CHANGELOG.md`](../CHANGELOG.md) (repository milestones) and
[`docs/governance/Roadmap.md`](../docs/governance/Roadmap.md)
("Recently landed"). Trim here if this file grows; do not trim the
canonical files from a memory session.

**Write-back:** when a PR merges and changes the working picture, add a
dated bullet and update [`state/CURRENT.md`](state/CURRENT.md).

**Sourced:** 2026-08-28. Newest first.

## 2026-08-30 — Provenance Log started (non-etymology evidence cards)

- [`memory/PROVENANCE-LOG.md`](PROVENANCE-LOG.md) added: the
  general-purpose sibling of `ETYMOLOGY-STACK.md`, for Provenance
  Stack (Starline Arsenal 32) evidence cards on claims that aren't
  about word origins — health/science-adjacent marketing, viral
  claims, etc. First worked card: "structured / EZ water," tiering
  Gerald Pollack's exclusion-zone observation (A−, real but disputed
  and unreplicated) apart from the H₃O₂ structural claim (D, rejected
  by chemists) and the wellness-marketing extension to whole-body
  hydration and fascia signaling (D/C, unsupported).
- Wired into `memory/FRAMEWORKS.md`.
- A second evidence card added same day: a research framework (LLM-assisted
  time-mirror physics + Fermi Paradox explanations) shared from a different
  AI session. Grabby Aliens confirmed against the real 2021 *ApJ* paper (A);
  Dark Forest flagged as a fiction-derived tier mismatch; a Musk/SpaceX
  quote confirmed unsourced by two independent checks.
- Also merged in the same PR: the 90-Day Public Roadmap project tracker
  (`memory/projects/90-Day-Roadmap/`) with a Starline Arsenal critique
  (Asymmetric Thinking, OODA Loop, Margin of Safety), and the Erisian
  Blade / Collaboration Protocol reconciliation in `OPEN-QUESTIONS.md`
  (confirmed real via images Crystal shared; not yet merged into the
  Starline Arsenal skill itself pending confirmation of the exact
  relationship).
- **Merged to main via PR #140** (2026-08-31 01:25 UTC).

## 2026-08-29 — Starline Arsenal reconciled 25 → 31, verification gate resolved

- The verification gate opened when models 14–25 landed (PR #130,
  logged in `OPEN-QUESTIONS.md`) is resolved: the source was two
  independent Claude-authored lineages in Google Drive, not Grok's
  runtime skill as first believed. Models 14–25 confirmed identical
  file-for-file against the 25-model Drive line.
- 6 models unique to a separate 21-model Drive line — Heuristic,
  Miscalibration, Regression to the Mean, Better-Than-Average, Parable,
  Philology — merged in as `models/26-heuristic.md` through
  `models/31-philology.md`.
- That line's dated "Field card" entries (a specific real situation and
  person) excluded from the merge per `PRIVACY.md`.
- `SKILL.md` / `INDEX.md` updated to 31 models, version 2.0.0 → 3.0.0.
- **Merged to main via PR #137** (2026-08-30 03:01 UTC).

## 2026-08-29 — Starline Arsenal full verification pass (1–31), two fidelity gaps fixed

- Extended verification to models 1–13, the only slice not yet checked
  against a source. Fetched fresh from the "Starline Arsenal Models"
  Drive folder; confirmed byte-identical to on-disk.
- Re-reading the 21-model line's full source text surfaced two real
  gaps against what had shipped: `models/30-parable.md` was missing the
  source's "no borrowed lyrics" rule; `models/21-rhetoric.md` and
  `models/25-persuasion.md` had kept plainer wording where a richer,
  later-dated (29 Aug) version existed — five rhetorical canons and the
  ethos/pathos/logos/kairos appeal square, and an explicit "honest no"
  step in Persuasion.
- All three fixed; governance gained the Speech Rule from the same
  source. `SKILL.md` version 3.0.0 → 3.1.0.
- **Merged to main via PR #137** (2026-08-30 03:01 UTC).

## 2026-08-29 — Provenance Stack absorbed from a concurrent PR, collision avoided

- A separate session's PR #138 independently added a 26th model
  ("Provenance Stack") plus `memory/ETYMOLOGY-STACK.md` on top of the old
  25-model `main`, unaware this branch already used 26–31 for six other
  models — the same collision shape as PR #130 earlier the same day.
- Absorbed directly onto this branch rather than left to conflict:
  `ETYMOLOGY-STACK.md` added as-is; the model renumbered to
  `models/32-provenance-stack.md`, content unchanged apart from the
  renumber; the same four proposed cross-references added (First
  Principles, Occam's Razor, Circle of Competence, Inference).
- `SKILL.md` / `INDEX.md` bumped 31 → 32 models, version 3.1.0 → 3.2.0.
- PR #138 left untouched — different session's PR, not pushed to or
  closed.
- **Merged to main via PR #137** (2026-08-30 03:01 UTC). PR #138 now
  shows a real merge conflict (`mergeable_state: dirty`) against the new
  `main`, as expected — resolving or closing it is the maintainer's call.

## 2026-08-29 — memory-state model, design hypothesis (PR #131)

- `memory/MEMORY-STATE-MODEL.md` added: a working-paper framework for
  labeling individual memory entries (Fact/Interpretation/Inheritance/
  Revision/Vision/Unknown) and the operations that can be performed on
  them (Bridge/Carry/Rewrite). Explicitly not implemented — no schema,
  storage engine, or sync mechanism exists. Preparatory design thinking
  for a possible future personal/collective memory system discussed in
  chat, not a change to this repo's own Claude Code memory protocol.
  Pointers added to `FRAMEWORKS.md` and `CANON-MAP.md`, same status as
  the Loop Framework and Number Collision Framework entries there.
- Same PR fixed a pre-existing CI failure on `main`: `TheCrystalVision`
  is a private repo, so its links 404 to `markdown-link-check`'s
  anonymous requests. Extended the existing `TerAustralis-Incognita-Code`
  ignore-pattern convention in `.github/markdown-link-check-config.json`
  to cover it.
- **MERGED to main** at `5994150` (2026-08-29 11:46 UTC).

## 2026-08-28 — frameworks retrieval map (this PR)

- `memory/FRAMEWORKS.md`: retrieval map of named frameworks, Claude Code
  skills, sibling-repo methods, and Drive papers. Points; does not dump
  Drive papers or invent a new framework. Number Collision stays on Drive.
  Loop Framework stays in `the-library`; this git only cites it.
  **Not on `main` until Crystal merges.**
- Wired into `INDEX.md`, `CANON-MAP.md`, `README.md`, `CLAUDE.md` Map,
  and `state/CURRENT.md`.

## 2026-08-28 — merged to `main` (PR #123)

- **Memory Bootstrap: COMPLETE.** PR #123 merged at `3ba08fdcb4e88f5386949bc3cd35a28dcd597fab`,
  authorized explicitly by Crystal Arena-Turner in session. Root
  `CLAUDE.md` and the full `memory/` tree are now live repository
  infrastructure — the durable Claude Code protocol future sessions land
  on, not a proposal awaiting review. Independently verified post-merge
  from a clean clone of `main` (not the working branch): all 17
  memory-tree files present, 0 broken links, 0 markdownlint issues,
  credential grep clean, and a 13-question cold-start trace (authority,
  read-order, Built/Vision/Unknown, decisions, blockers, privacy,
  external boundaries, conflicts, write-back triggers, continuity without
  chat) answerable from disk alone.
- This work happened in three passes plus Crystal's direct decisions —
  full detail in the entries immediately below, left as written since
  they're the accurate record of how this landed, not tidied after the
  fact.

- Claude Code **read-and-write** memory protocol: root `CLAUDE.md` +
  `memory/`. Does not restore the Repository Engineer seat (ADR-0014).
  Does not amend the Constitution. **Not on `main` until Crystal merges.**
  *(True when written, earlier the same day — superseded a few entries up
  by the actual merge. Left as written rather than edited; that's this
  file's own convention.)*
- Same-day reconciliation pass, same branch: two earlier implementation
  passes had been merged together, leaving orphaned duplicate state files
  and a handful of ungrounded claims. Fixed: deleted
  `memory/state/{DECISIONS,OPEN-QUESTIONS,MILESTONES}.md` (superseded by
  the root-level, ADR-cited versions this file lives in); removed a
  fabricated citation to a nonexistent "DUR specification" from
  `evidence/HYPOTHESES.md`; added an explicit no-on-disk-citation warning
  to `collaboration/EXTERNAL-RELATIONSHIPS.md` rather than presenting the
  Ovaro/Continuum/CMX boundary as verified canon; logged a real,
  previously-unrecorded archive framing tension in `evidence/CONFLICTS.md`
  (cross-referenced from this file's own Tier 3 entry); added
  `CANON-MAP.md` (authority map, distinct from `INDEX.md`'s retrieval
  map); wired `collaboration/`, `evidence/`, and `projects/` into
  `README.md` and `INDEX.md`, which previously didn't reference them; and
  added three explicit `CLAUDE.md` rules (permission ≠ readability, AI
  inference ≠ Crystal's decision, update this file on a durable
  correction) that the governing spec required but the prior pass missed.
- Same-day, Crystal's direct approval on PR #123: three items the
  reconciliation pass had flagged as requiring her decision, resolved.
  (1) CMX/Ovaro/Continuum boundary — approved, recorded as a current,
  dated, Crystal-authored decision in `DECISIONS.md` "Direct maintainer
  decisions recorded in memory," **not** a rediscovered older source;
  `EXTERNAL-RELATIONSHIPS.md` and `CANON-MAP.md` updated to cite it. (2)
  Archive framing (`crystalcore/` vs `crystalcore-v0.13/` recovery notes)
  — accepted as currently organized, no repo-wide rewrite; moved from
  Open to Resolved in `evidence/CONFLICTS.md`; struck from
  `OPEN-QUESTIONS.md`'s held-open table with a note that
  `docs/OPEN-DECISIONS.md` itself (canonical, Repository Engineer scope)
  hasn't been synced to match — logged, not silently hidden. (3) No
  `memory/projects/repository-memory-bootstrap/` subdirectory — bootstrap
  concludes as foundational infrastructure, not an ongoing active
  project; completion marking deferred to the post-merge commit per
  Crystal's own sequencing ("mark complete once merged").

## 2026-08-20 (CHANGELOG + Roadmap cluster)

- Human door: GitHub + sites + Discord. `docs/guides/Access.md` — this
  repo is not private; OAuth and a twentieth GitHub are refused join paths.
- Cybernetics note: `docs/architecture/CYBERNETICS-VSM.md`. Model, not a
  new OS mode.
- Ink honesty + SourceCode as external peer (`ADR-0016`, Proposed).
  `-Code` marked public in the charter. `ADR-0015` stamped Accepted (PR #118).
- Stop growing the constellation (`ADR-0015`). Nineteen repositories
  measured. No new GitHub repository without an ADR.
- Domain measured: apex 301 → www 200, SvelteKit from `-Code`. Root
  `index.html` + `.nojekyll` so leftover Jekyll Pages is a pointer, not a
  second site. GitHub About description patched out-of-git to one *a*.
- Grok Build takes the Repository Engineer seat (`ADR-0014`, PR #116).
  Claude retained as history.

## 2026-07-29

- Codex of the Oracle in `mythos/content/CODEX-OF-THE-ORACLE.md` —
  authority weight it sets for itself: **zero**. Locked names hold.
  Engineering claims stay in the archive until receipts exist.

## 2026-07-27

- CrystalCore.OS mythos terminal boots from a fresh clone
  (`mythos/crystalcore-os/crystalcore_os.py`), stdlib-only. Verified in
  [`STATUS.md`](../STATUS.md). "Songline" stays a cultural image, never a
  component name. Deliberately **not** implemented: printed security
  commands with no mechanism (`verify-certificates`, `security harden`,
  continuous integrity monitoring) — Incognita Rule.

## 2026-07-24

- Story Library design + self-contained HTML prototype
  (`research/prototypes/story-library/`). Production SvelteKit/React
  components: not built.
- CI honest: src/tests-dependent steps skip because those trees live in
  `-Code`.

## 2026-07-23 — foundation day

- Three-project boundary (`ADR-0011`) + Project-Boundaries + Migration-Plan
  (Vision; nothing moved in that ADR).
- Entry-point docs resynchronized: `src/`, `scripts/`, `tests/` are not in
  this git and never were.
- Name correction to **TerAustralis Incognita** (`ADR-0007`).
- License terminus: uniform CC BY-NC-ND 4.0 (`ADR-0006` → `0008` → `0009`
  → `0010`).
- CrystalCore OS v0.2 Architecture Specification Release (`ADR-0004`,
  `ADR-0005`). No runtime, by design.
- CrystalCore OS v1.0 repository architecture (`ADR-0001`, `ADR-0002`,
  `ADR-0003`). Platform milestone v0.1.

## Platform versions (Roadmap)

| Version | State on disk |
|---|---|
| v0.1 Repository foundation | Delivered 2026-07-23 |
| v0.2 Architecture Specification | Delivered 2026-07-23 |
| v0.3 Engine layer | Not started |
| v0.4 Living Archive | Not started |
| v1.0 Stable platform | Target, not a promise |
