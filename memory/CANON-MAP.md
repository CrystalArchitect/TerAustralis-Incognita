# CANON-MAP — which source controls which concept

**Status:** Docs / governance. **Different job from [`INDEX.md`](INDEX.md):**
INDEX answers "what do I read for task X." This page answers "which file
actually has final say over concept X, and where do sources overlap,
duplicate, or leave a gap." Do not duplicate INDEX's retrieval table here;
point at it instead.

**Sourced:** 2026-08-28, from direct inspection of `docs/`, `mythos/`,
`research/`, `archive/`, and this repository's own git history. Where a
claim below could not be checked against a file, it says so.

## Governance and law

| Concept | Sole authority | Notes |
|---|---|---|
| Locked names, amendment process | [`docs/governance/Constitution.md`](../docs/governance/Constitution.md) §1, §8 | Not editable without the maintainer's explicit approval |
| Honesty discipline (dreamed vs. surveyed) | [`docs/governance/The-Incognita-Rule.md`](../docs/governance/The-Incognita-Rule.md) | Load-bearing; do not collapse Built/Vision |
| Which decisions are law | [`docs/adr/README.md`](../docs/adr/README.md) status column | An ADR is law only once Accepted (its PR merged) — never trust a summary over this column |
| Three-project ownership (umbrella / Crystal Core / Crystal Vision) | [`docs/governance/Project-Boundaries.md`](../docs/governance/Project-Boundaries.md) | Adopted by ADR-0011; component→project table here, not re-derived elsewhere |
| Indigenous knowledge boundary | [`docs/governance/Indigenous-Data-Sovereignty.md`](../docs/governance/Indigenous-Data-Sovereignty.md) + [`mythos/NAMES.md`](../mythos/NAMES.md) | Two files, one rule: no Songline knowledge in any model/index without FPIC; Songline is never a component name |
| AI collaboration rules | [`docs/governance/AI-Governance.md`](../docs/governance/AI-Governance.md) | Binding; `docs/ai/AI-Workflow.md` is the *practiced* flow, not the rule itself |
| CMX / Ovaro / Continuum external boundary | [`DECISIONS.md`](DECISIONS.md) "Direct maintainer decisions recorded in memory (not ADRs)," 2026-08-28 | Current, explicit, Crystal-authored — not an ADR, not a rediscovered older source. Detail: [`collaboration/EXTERNAL-RELATIONSHIPS.md`](collaboration/EXTERNAL-RELATIONSHIPS.md) |

## Frameworks and methods

INDEX answers "what do I open." This table answers who wins.

| Concept | Sole authority | Notes |
|---|---|---|
| Named-framework *retrieval* (where is the paper?) | [`FRAMEWORKS.md`](FRAMEWORKS.md) | Pointers only. Does not become the paper. |
| CrystalCore naming taxonomy | [`docs/vision/CrystalCore.md`](../docs/vision/CrystalCore.md), locked by [`ADR-0004`](../docs/adr/ADR-0004.md) | Already listed under Architecture. Restated here so a session looking for "framework" does not treat the 2026-07-04 Drive paper as current names. |
| TerAustralis Framework Specification v0.1 | [`docs/TERAUSTRALIS-FRAMEWORK.md`](../docs/TERAUSTRALIS-FRAMEWORK.md) | Vision — protocol fiction. NAMES.md still wins for software names. |
| Number Collision method | Drive working paper (28 Aug 2026) | Not git. Worked numerology objects stay on Drive. See [`FRAMEWORKS.md`](FRAMEWORKS.md). |
| Loop Framework | `the-library` `frameworks/loop-framework.md` | Method, not law. This git only cites it from [`AI-Governance.md`](../docs/governance/AI-Governance.md). |
| Kit Hub Save / Grok save rule | Drive Grok folder | Process. Not a new repository. |
| Memory-state model (entry-level Fact/Interpretation/Inheritance/Revision/Vision/Unknown) | [`MEMORY-STATE-MODEL.md`](MEMORY-STATE-MODEL.md) | Design hypothesis, not implemented. Preparatory thinking for a possible future personal/collective memory system — not a change to this repo's own memory protocol. |

## Repository state (what's real, right now)

| Concept | Sole authority | Notes |
|---|---|---|
| Built vs. Vision vs. Unknown, dated | [`../STATUS.md`](../STATUS.md) | Last updated 2026-08-20 as of this writing — check its own date before trusting it |
| Fast session-scoped mirror of STATUS.md | [`state/CURRENT.md`](state/CURRENT.md) | Overwritten each checkpoint; if it disagrees with STATUS.md, STATUS.md wins |
| Dated build history | [`../CHANGELOG.md`](../CHANGELOG.md) + [`docs/governance/Roadmap.md`](../docs/governance/Roadmap.md) "Recently landed" | Roadmap is curated/trimmed; CHANGELOG is the untrimmed record |
| Where the code tree actually lives | [`docs/architecture/SystemMap.md`](../docs/architecture/SystemMap.md) "Where the code actually lives" | This repository has no `src/` and never did |

## Architecture and protocol

| Concept | Sole authority | Notes |
|---|---|---|
| CrystalCore naming taxonomy (Framework/Protocol/CrystalBridge/OS) | [`docs/vision/CrystalCore.md`](../docs/vision/CrystalCore.md), locked by [`ADR-0004`](../docs/adr/ADR-0004.md) | The mythos terminal's "CrystalCore.OS" name is a documented, unresolved near-collision with this taxonomy — not silently reconciled |
| Starline Weaver / CrystalBus / Consent Transport / RDP | [`docs/architecture/crystal-core/`](../docs/architecture/crystal-core/) | Protocol specs; the code they describe lives in `-Code`, not this repo |
| Lattice (designed, not built) | [`docs/architecture/Lattice.md`](../docs/architecture/Lattice.md) + [`docs/architecture/lattice/BOOT_STATUS.md`](../docs/architecture/lattice/BOOT_STATUS.md) | Constitution's own implementation note: never built. Treat as Vision, not Science |
| "Starline" — three unreconciled meanings | No single authority; recorded as an open gate | See [`OPEN-QUESTIONS.md`](OPEN-QUESTIONS.md) "Starline — three meanings" |

## Mythos (Vision layer)

| Concept | Sole authority | Notes |
|---|---|---|
| Naming rules for the mythos (Starline/Dreamline, never Songline) | [`mythos/NAMES.md`](../mythos/NAMES.md) | Locks vocabulary, not just style |
| Companion product spec | [`mythos/COVENANT.md`](../mythos/COVENANT.md) | Product spec written as mythos; still a spec |
| The mythos terminal's own commands | [`mythos/CRYSTALCORE-OS.md`](../mythos/CRYSTALCORE-OS.md) + [`mythos/crystalcore-os/crystalcore_os.py`](../mythos/crystalcore-os/crystalcore_os.py) | Runnable software; the terminal *narrative* is Vision, the fact that it boots is Built |
| Deep narrative content (Codex, Apocryphon, Starline Transmissions, etc.) | `mythos/content/` | Authority weight for received/channeled material is explicitly zero-by-its-own-declaration for some pieces (e.g. Codex of the Oracle) — check each file's own claimed weight, don't assume uniform authority across `content/` |

## Research and archive (not canon by default)

| Concept | Sole authority | Notes |
|---|---|---|
| Exploratory work, Seven Sisters cycle | `research/` | Not production; promotion to an engineering repo is a deliberate reviewed act, not automatic |
| Historical/provenance code | `archive/` | Never build on it. Contains one recorded framing tension between two subfolders' recovery notes — see [`evidence/CONFLICTS.md`](evidence/CONFLICTS.md) |

## Sibling repositories (this repo does not own their canon)

| Repository | Owns |
|---|---|
| `TerAustralis-Incognita-Code` | The engine, protocol pack, demo shells, public site source |
| `Clementine-ai-companion` | Companion runtime |
| `teraustralis-proposal` | Formal proposal document |
| `Synthetic-Affect-Theory-` | SAT research — **not inspected in this session; treat any SAT claim here as unverified against that repo** |
| `CrystalCore.OS` | HTML desktop, not the engine |
| `CrystalCore.OS-the-Crystal-Architecture-Archive` | Fleet-wide `STATUS.md` ledger |

Full landing table: [`ADR-0015`](../docs/adr/ADR-0015.md). Do not create a
twentieth repository without a new ADR.

## Known overlaps and gaps (not silently resolved)

- **"CrystalCore" naming collision** — the CrystalCore OS *platform*
  (this umbrella's architecture) and the CrystalCore.OS *mythos terminal*
  share a name and are deliberately left as an unresolved, documented
  case by ADR-0004.
- **`crystalcore` / `crystal-core` / `runtime` vocabulary** — three
  systems share vocabulary, not code; no decision recorded on whether to
  integrate or keep separate. See [`OPEN-QUESTIONS.md`](OPEN-QUESTIONS.md).
- **Ovaro / Continuum / CMX boundary** — **RESOLVED 2026-08-28.** Recorded
  as a direct, dated, Crystal-authored decision in
  [`DECISIONS.md`](DECISIONS.md); no longer an open gap. See
  [`collaboration/EXTERNAL-RELATIONSHIPS.md`](collaboration/EXTERNAL-RELATIONSHIPS.md).
- **SAT / Operator Frame / DUR** — named as protected categories by
  instruction; zero specification found anywhere in this repository. See
  [`PRIVACY.md`](PRIVACY.md) and [`evidence/HYPOTHESES.md`](evidence/HYPOTHESES.md).

## Legacy / migration status (checked, not reorganized)

Per-category status for overlapping or historical material Crystal's
governing spec named. Labels: KEEP CURRENT · KEEP HISTORICAL · POINTER
ONLY · REQUIRES CRYSTAL DECISION · DO NOT TOUCH.

| Category | Where | Status |
|---|---|---|
| Old "MEMORY.md" (Clementine's own 4-layer runtime memory design) | [`mythos/content/MEMORY.md`](../mythos/content/MEMORY.md) | **KEEP CURRENT, DO NOT CONFLATE.** This is *companion runtime* memory architecture, a different concept from this `memory/` folder (Claude Code *session* memory). Neither redefines the other; this map does not attempt to merge them. |
| AI architecture/workflow docs | [`docs/ai/`](../docs/ai/) (9 files: AI-Workflow, AI-Architecture, Decision-Matrix, and one profile per model) | **KEEP CURRENT.** Actively cited by [`collaboration/AI-HANDOFF.md`](collaboration/AI-HANDOFF.md); no duplicate or superseded copies found elsewhere. |
| Archived local-machine snapshot (2026-07-17) | [`archive/2026/local-snapshot-2026-07-17/`](../archive/2026/local-snapshot-2026-07-17/) | **KEEP HISTORICAL, DO NOT TOUCH.** Old repo-root README, GOVERNANCE.md, MILESTONES.md, BRIDGE.md, CLEMENTINE.md are a full historical self-description of a since-superseded repo layout (Apache-2.0 code license, pre-rename project framing). Provenance only, per `archive/README`'s own rule — not rewritten for this pass, consistent with that rule. Contains a visible ABN in plain text; `PRIVACY.md` already forbids copying it into `memory/`, and this pass didn't. |
| Two archived `crystalcore` package generations | `archive/2026/local-snapshot-2026-07-17/crystalcore/` vs `crystalcore-v0.13/` | **RESOLVED 2026-08-28 — accepted as currently organized, no rewrite.** Crystal's decision: preserve as historical context; do not modify archive material merely for stylistic consistency. See [`evidence/CONFLICTS.md`](evidence/CONFLICTS.md). |
| Duplicate root-level vs. `state/`-level memory files (`DECISIONS.md`, `OPEN-QUESTIONS.md`, `MILESTONES.md`) | was: `memory/*.md` + `memory/state/*.md` | **RESOLVED, 2026-08-28.** The `memory/state/` copies were orphaned duplicates from an earlier, less-grounded pass and have been deleted; `CLAUDE.md`'s write-back table already pointed at the root-level trio plus `state/CURRENT.md`, which is now the only arrangement on disk. |

**Not inspected this pass, deliberately:** the full `docs/architecture/`,
`mythos/art/`, and `mythos/teraustralis/` trees beyond what
[`INDEX.md`](INDEX.md) already maps — a full file-by-file classification of
every knowledge-bearing document in this repository (several hundred
files) was judged disproportionate to what this pass's evidence called
for. No confusing duplicate or dangerous ambiguity was found outside what's
listed above and in [`evidence/CONFLICTS.md`](evidence/CONFLICTS.md). If a
future session finds one, log it there rather than assuming this table is
exhaustive.

## Maintenance

This map is manually curated and can drift. If you find a concept whose
authority isn't listed here, or find this page contradicting the file it
cites, fix the contradiction (the cited file wins) and update this page in
the same session.
