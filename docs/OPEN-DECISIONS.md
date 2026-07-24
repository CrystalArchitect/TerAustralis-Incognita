# Outstanding Questions & Open Decisions

This knowledge base documents the CrystalCore.OS architecture **exactly as it exists**, not as it might be redesigned. It is a reconstruction of verified implementation, designed decisions, and remaining open questions — not a proposal for what the system should become.

**Source documents:** Project-Boundaries.md §Open decisions, architecture-survey.md §8 (Tier 2), Migration-Plan §Stages 3–4, technical-findings.md (cross-component analysis) · **Last verified:** 2026-07-23 · **Labels:** Vision 🔮 (decision gates specified, outcomes open)

---

## Decision Gates and Criteria

**Status:** Vision 🔮 (decision structure defined, conditions not yet met)

**Summary:** Six decisions are deliberately held open because they depend on future conditions (release patterns, adoption patterns, organizational changes) that cannot be evaluated today. Each gate specifies what must be true to decide.

**Evidence:**
- Repository: TerAustralis-Incognita / docs/governance/Migration-Plan.md §Stages 3–4 (gates and criteria)
- Verified: Maintainer decision record in ADR-0011 (2026-07-23)

**Details:** See sections below for each decision.

---

## Stage 3 Decision 1: Repo-Count Split (Core / Vision Separation)

**Status:** Vision 🔮 (criteria specified, conditions not yet met)

**Question:** Should TerAustralis-Incognita-Code be split into separate `core` and `vision` repositories?

**Current state:** Single repository with `core/` and `vision/` top-level areas; dependency rule enforced in PR review.

**Decision gate — split ONLY when at least one of these is true:**
1. Release cadences diverge (Core ships on different schedule than Vision).
2. Licensing split becomes real (revisiting ADR-0010; differentiated licenses per repository).
3. External contributors need scoping to one side (third-party Core consumers or Vision-only contributors).
4. CI/product surfaces diverge enough to fight each other (tooling incompatibility, deployment separation required).

**Until then:**
- One repository, two top-level areas.
- Dependency rule (Vision → Core, never backward) enforced in code review.
- Shared CI/CD pipeline (compileall, 70+ tests in one run).

**Why this matters:** Repo splits are hard to undo; this gate prevents premature split based on convenience alone.

**Related:** [ARCHITECTURE.md](ARCHITECTURE.md) (dependency rule), [REPOSITORIES.md](REPOSITORIES.md) (current single-repo structure)

---

## Stage 3 Decision 2: Lumina Framework Extraction

**Status:** Vision 🔮 (criteria specified, Lumina stays whole for now)

**Question:** Should CrystalCore Framework be extracted from Lumina into Crystal Core?

**Current state:** Framework lives embedded in Lumina (vision/apps/lumina/crystalcore/); carries ADR-0004 name while traveling with the companion app.

**Decision gate — extract Framework ONLY when at least one of these is true:**
1. A second companion app needs the Framework (establishes reusability).
2. An external consumer imports it (validates library status).
3. Independent versioning/release pressure appears (decoupling needed for schedules).

**Until then:**
- Lumina stays whole in Crystal Vision (per maintainer directive, recorded ADR-0011).
- Framework keeps ADR-0004 name; split criteria are operationalized above.

**Why this matters:** Premature extraction of a library that only one app uses adds overhead without benefit.

**Related:** [ARCHITECTURE.md](ARCHITECTURE.md) (component → project assignments), [TECHNICAL-FINDINGS.md](TECHNICAL-FINDINGS.md) (Framework lineage: 0.7.0 fork, 0.13.4 unreconciled)

---

## Stage 3 Decision 3: Frozen Repositories' End State

**Status:** Vision 🔮 (three options specified, decision held open)

**Question:** What should happen to the three frozen provenance repositories (The-Crystal-Vision, crystalcore, crystal-vision)?

**Current state:** Three repositories tagged with `-safe-2026-07-17` suffix; deliberately unarchived, never edited. Code rescued into living repos where applicable.

**Options:**

| Option | Mechanism | Benefit | Downside |
|---|---|---|---|
| **A: GitHub Archive** | Set read-only flag via GitHub API / Settings | Makes intent explicit ("this is provenance only"); prevents accidental edits; discoverable in GitHub UI | One-way operation; minimal reversibility. |
| **B: Leave as-is** | Keep current state (unarchived, live-looking) | Fully reversible; low commitment; can decide later | Intent not explicit; relies on discipline to not edit. |
| **C: Archive to external** | Move to cold storage (AWS S3, tarball) | Frees GitHub quota; reduces noise in org | Harder to query via git; less discoverable. |

**Decision criteria:** No explicit gate (other than "sometime Stage 3+"). Maintainer decision.

**Why this matters:** These repos are provenance only; their end state should reflect that clearly without taking them completely offline.

**Related:** [REPOSITORIES.md](REPOSITORIES.md) (frozen repos section), [TIMELINE.md](TIMELINE.md) (provenance snapshots)

---

## Stage 4 Decision 1: Site Placement and Content Sync

**Status:** Vision 🔮 (recommendation made, placement Stage 2, sync open)

**Question (placement):** Where should the public site source live?

**Current state (2026-07-24):** Site source lives at `vision/site/` in TerAustralis-Incognita-Code (moved Stage 2, 2026-07-23). Pages deploy is set up there.

**Recommendation:** Crystal Vision (it is the public face). ✅ Implemented Stage 2.

**Why this matters:** Site is user-facing (Vision project) not engine-facing (Core project).

---

**Question (content sync):** How should canonical mythos content flow to the public site?

**Current state (2026-07-24):** Manual copy required: `mythos/` (umbrella) → `vision/site/src/content/` (Code) → build → deploy.

**Known gap:** The First Remembering (canonical in umbrella) has not yet been copied into site content as of 2026-07-24. This is a known drift risk.

**Options:**

| Option | Mechanism | Benefit | Downside |
|---|---|---|---|
| **A: Manual copy (current)** | Maintainer copies files, commits to `-Code` repo | Explicit, reviewable, low overhead for small team | Publishing delay; manual process prone to drift |
| **B: CI automation** | Script in `-Code` CI fetches from umbrella, commits, triggers site build | Eliminates manual step; auto-sync on umbrella changes | Cross-repo CI coupling; may need tokens/permissions |
| **C: Build-time fetch** | Site build fetches at SvelteKit build time instead of storing copies | No stored drift; source of truth always current | Build dependency on umbrella repo availability; slower deploy |

**Recommendation:** For now, improve A (manual process discipline) via pre-deployment checklist. B (CI automation) is Stage 3–4 enhancement.

**Why this matters:** Canonical content not published is a known gap; the pipeline should make publishing explicit and reliable.

**Related:** [REPOSITORIES.md](REPOSITORIES.md) (content pipeline), [ARCHITECTURE.md](ARCHITECTURE.md) (three-project boundary)

---

## Stage 4 Decision 2: dbt Emotion Warehouse

**Status:** Vision 🔮 (recommendation made, placement deferred)

**Question:** What should happen to `dbt/crystalcore_emotion_warehouse/`?

**Current state (2026-07-24):** Warehouse lives in umbrella repo (inherited from pre-reorg era). Has zero data source (staging models are hardcoded null CTEs). Contains SQL syntax error.

**Recommendation:** Crystal Core's data layer eventually; acceptable to leave in umbrella as research artifact until engineering repo is real.

**Before Stage 4, Tier 1 action:** Fix the SQL syntax error in `stg_emotion_labels.sql`; decide whether to wire staging models to JSONL files `dbt_integration.py` already writes, or retire until ready.

**Why this matters:** The project is not currently emitting emotion predictions that this warehouse would process. It's engineering-ready code for a feature that doesn't exist yet.

**Related:** [TECHNICAL-FINDINGS.md](TECHNICAL-FINDINGS.md) (warehouse state, Tier 1 recommendations)

---

## Unresolved Component Integration Questions

**Status:** Vision 🔮 (patterns identified, decision needed)

**Summary:** Three core systems share vocabulary but not code. They are either intentionally separate or genuinely under-integrated. This requires explicit decision.

**Evidence:**
- Repository: TerAustralis-Incognita-Code / src/
- Audit finding: "The three components that look like they should be layers of one system are not integrated" (architecture-survey.md §4)

**Details:**

| Component | What it is | Test coverage | Integration |
|---|---|---|---|
| `src/crystalcore` | CrystalBridge — MCP consent gate | 🔴 Zero | Isolated |
| `src/crystal-core` | Protocol pack (Starline, RDP, services, Clementine) | ✅ 51 tests | Isolated from crystalcore, internally coherent |
| `src/runtime` | Service orchestration scaffold (coordinator, registry, events, config) | ✅ 75 tests | Isolated; two textual mentions of other systems, both comments |

**Tier 2 recommendation:** Make an explicit call: 
- **Option A:** Intentionally separate systems (document why they're separate; stop echoing vocabulary across them).
- **Option B:** Genuinely integrate them (start from the one demo-only cross-import that already proves it's possible).

**Why this matters:** Ambiguous relationships encourage developers to write integration code in the wrong places.

**Related:** [TECHNICAL-FINDINGS.md](TECHNICAL-FINDINGS.md) (integration audit findings)

---

## Naming Disambiguation: "Starline"

**Status:** Vision 🔮 (collision documented, taxonomy needed)

**Question:** What does "Starline" mean?

**Current collision:**
- **Meaning A:** The real P2P transport (consent_transport, Noise protocol).
- **Meaning B:** Multi-agent message bus ("Starline Weaver").
- **Meaning C:** Fictional game state machine (mythos terminal, `crystalcore-os.py`).

Three meanings appear in two similarly-titled documents (`STARLINE.md` vs. `STARLINE-WEAVE-PROTOCOL.md`).

**Tier 2 recommendation:** Disambiguate the way ADR-0004 disambiguated "CrystalCore" — write a taxonomy ADR for "Starline," lock the meanings, prevent future proliferation.

**Candidates for renaming (to clarify, not change meaning):**
- **Meaning A:** "Consent Transport" or "SonglineTransport" (already has clear module names).
- **Meaning B:** "Starline Weaver" (already distinguished in one document).
- **Meaning C:** "Songline Network" (fictional, distinct from protocol names).

**Why this matters:** Vocabulary collisions force readers to infer from context, making specifications harder to search and understand.

**Related:** [GOVERNANCE.md](GOVERNANCE.md) (ADR-0004 precedent), [TECHNICAL-FINDINGS.md](TECHNICAL-FINDINGS.md) (naming collision audit)

---

## Lineage Reconciliation: 0.7.0 vs. 0.13.4 Fork

**Status:** Vision 🔮 (lineage documented, reconciliation deferred)

**Question:** How should the pre-reorg `crystalcore` versions (0.7.0 vs. 0.13.4) be reconciled?

**Current state (2026-07-24):**
- Lumina's embedded Framework forked the 0.7.0 line (tested, integrated with Lumina, 16 tests passing).
- The-Crystal-Vision frozen repo contains a complete 0.13.4 bytecode rescue (spell-checking, audio effects, GUI elements).
- The 0.13.4 extras (SpaceXAI provider, `node.py`, `status.py`, CLI) remain unreconciled in the frozen repo.

**Open questions:**
1. Should 0.13.4 features be integrated into the 0.7.0 fork running in Lumina?
2. Are the 0.13.4 extras valuable or historical?
3. What does the 0.13.4 → 0.7.0 fork represent architecturally?

**Why this matters:** The lineage is historically documented (in frozen repo tags); the current working version is known (0.7.0 fork in Lumina). The reconciliation question is open but not urgent (both states are preserved).

**Tier 2 recommendation:** Document the design intent (was 0.7.0 a deliberate simplification? An architectural choice?). If 0.13.4 features should be ported, that becomes implementation work.

**Related:** [REPOSITORIES.md](REPOSITORIES.md) (frozen repo note), [TIMELINE.md](TIMELINE.md) (version history)

---

## Archive Recovery Status Reconciliation

**Status:** Drift ⚠️ (two contradictory documents, reconciliation needed)

**Question:** What was recovered from the pre-reorg era?

**Current conflict:**
- `archive/2026/local-snapshot-2026-07-17/README-SNAPSHOT.md` lists `status.py` and SpaceXAI provider as "unrecoverable."
- A sibling file, `crystalcore-v0.13/RECOVERY-STATUS.md` (same date), says both were "fully recovered."

**Nobody reconciled the two — a reader who opens only the first file walks away with wrong picture.**

**Tier 3 recommendation:** Reconcile the two documents; mark the stale one with a date and pointer.

**Why this matters:** Historical record should not contradict itself about what was lost and what was found.

**Related:** [TIMELINE.md](TIMELINE.md) (archive checkpoints), [REPOSITORIES.md](REPOSITORIES.md) (frozen provenance repos)

---

## Summary

Six decisions are held open:

| Decision | Gate | Status | Priority |
|---|---|---|---|
| Stage 3: Split core/vision repos | Release cadences diverge OR licensing splits OR external scope OR CI/product separation needed | Vision 🔮 | Stage 3 |
| Stage 3: Extract Framework from Lumina | Second app needs it OR external consumer OR versioning pressure | Vision 🔮 | Stage 3 |
| Stage 3: Frozen repos end-state | Maintainer choice (no explicit gate) | Vision 🔮 | Stage 3 |
| Stage 4: Site content sync | Improve manual process now; CI automation Stage 3–4 | Vision 🔮 | Stage 4 (action: fix drift gap) |
| Stage 4: dbt warehouse | Fix SQL error + wire to JSONL or retire | Vision 🔮 | Stage 4 (Tier 1 action) |
| Tier 2: Component integration | Intentionally separate or integrate? | Vision 🔮 | Tier 2 (weeks) |
| Tier 2: Starline disambiguation | Write taxonomy ADR | Vision 🔮 | Tier 2 (weeks) |
| Tier 2: 0.7.0 vs 0.13.4 fork | Document design intent + port decision | Vision 🔮 | Tier 2 (weeks) |
| Tier 3: Archive recovery conflict | Reconcile two contradictory docs | Drift ⚠️ | Tier 3 (polish) |

None of these are blockers. Each is deliberately held open because it depends on future conditions or architectural judgment that cannot be made from current state alone.

---

**See also:** [ARCHITECTURE.md](ARCHITECTURE.md) (component map), [GOVERNANCE.md](GOVERNANCE.md) (decision process), [TECHNICAL-FINDINGS.md](TECHNICAL-FINDINGS.md) (where decisions touch practice), [TIMELINE.md](TIMELINE.md) (why decisions are needed now)
