# Technical Audit & Findings

This knowledge base documents the CrystalCore.OS architecture **exactly as it exists**, not as it might be redesigned. It is a reconstruction of verified implementation, designed decisions, and remaining open questions — not a proposal for what the system should become.

**Source documents:** architecture-survey.md (complete 2026-07-23 audit), STATUS.md (component state) · **Last verified:** 2026-07-23 (audit re-run confirmations) · **Labels:** ✅ Verified / 🔮 Vision / ⚠️ Drift / 🔴 Critical

---

## Executive Summary

**Status:** Science ✅ (verified by re-run of all tests this session)

**Summary:** The project is in better shape than its symptoms suggest. Engineering underneath is frequently excellent (real cryptography, property-based testing, disciplined ADR trail), but it was built across a compressed timeline by several uncoordinated hands (human and AI). Seams from that coordination gap are showing. Nothing found is a five-alarm fire; several things are quietly accumulating interest.

**Evidence:**
- Repository: TerAustralis-Incognita / docs/reviews/2026-07-23-architecture-survey.md
- Date: 2026-07-23 (audit date, all tests re-run and confirmed)
- Audit scope: 4 independent research passes (docs, content, core architecture, delivery surface)

**By the numbers:**
- 2 repos, split same-day (2026-07-23) — docs repo still describes repo that no longer exists
- 3 core systems sharing vocabulary, not code — near-zero real integration
- 150+ tests passing across the code repo (re-run and confirmed)
- 7 `packages/` distributables — zero have ever been executed by test or CI
- 5 key findings (detailed below)

**Implications:** The project needs targeted fixes in specific areas (Tier 1–3 recommendations) rather than structural overhaul.

---

## The Five Key Findings

### Finding 1: Docs Repo Describes Repo That No Longer Exists

**Status:** Drift ⚠️ (actionable)

**Summary:** The docs repository's README, ADRs, and agent-instruction files still assume `src/`, `tests/`, and `scripts/` live inside it. Those paths are absent from today's `main` and absent from all locally available git history. GitHub Actions history shows CI successfully exercising `src/` on an *earlier* `main` lineage the same morning; the split was implemented as a same-day history rewrite that no document records.

**Evidence:**
- Repository: TerAustralis-Incognita
- Files: README.md, docs/architecture/SystemMap.md, docs/agents/*.md (all reference `src/`, `tests/`)
- Date: Repo split happened 2026-07-23 as force-push (not documented); CI has been red ever since

**Details:** The code was moved to a new repository (`TerAustralis-Incognita-Code`) as part of the same-day reorganization. The umbrella repo's documents were *not* updated to reflect this move. New readers (human or AI) who read the docs repo alone get a map that doesn't match the territory.

**Related drift:** `mythos/README.md` describes a third, even older arrangement (four separate repositories) — predates both the current two-repo reality and the ADR-0001 monorepo model.

**Tier 1 recommendation:** Add a dated note to `SystemMap.md` and root README explaining the current two-repo split. Reconcile or retire `mythos/README.md`'s older account.

**Status:** Not yet implemented (this knowledge-base project does not cover older docs revisions; they remain open issues).

---

### Finding 2: `packages/` Is Actively Misleading

**Status:** Critical 🔴 (actionable immediately)

**Summary:** Seven `teraaustralis.*` namespace packages exist. Five non-empty ones are byte-for-byte copies of `src/` code with copyright headers stripped — not thin re-export wrappers. Every README describes an API surface that doesn't exist in the shipped code. Nothing in `packages/` has ever been executed by a test, self-test, or even a syntax check.

**Evidence:**
- Repository: TerAustralis-Incognita-Code (legacy)
- Directory: packages/ (inherited from pre-reorg era)
- Verified: diff of five copies shows identical code except copyright header removal
- Test coverage: Zero (check.sh's `compileall` doesn't include packages/)

**Specific issues found:**
- `packages/lumina/__init__.py` carries CrystalBridge's docstring, copied by mistake; declared entry point (`lumina = "teraaustralis.lumina:main"`) points at attribute that doesn't exist → would fail on install.
- `packages/crystalbridge` hardcodes a relative path that worked one level up in original; copied differently, points at directory that doesn't exist in shipped package.
- `packages/starline` imports `teraaustralis.consent_transport` without declaring it as dependency → `pip install` fails.

**Tier 1 recommendation:** Delete `packages/` entirely and ship `src/` directly, OR commit to thin re-export wrappers wired into CI so drift is caught going forward. Leaving it as-is actively misinforms anyone who reads a package README before its code.

**Status:** Not yet implemented (Tier 1, high priority).

---

### Finding 3: Documentation and Code Have Overtaken Each Other

**Status:** Drift ⚠️ (mixed directions)

**Summary:** The runtime exists in code while docs call it unstarted; `packages/` READMEs describe features that were never built. Both are symptoms of the same root: writing and shipping happened faster than anyone had time to reconcile.

**Evidence:**
- Repository: TerAustralis-Incognita + TerAustralis-Incognita-Code
- Examples: Roadmap.md calls Crystal Runtime "not started"; code repo already ships it with 75 passing tests

**Details:**
- Three same-day Crystal Runtime spec documents contradict each other: one says "deferred until review," another says "ready to specify testing," a third says "ready for implementation." Meanwhile `Roadmap.md` calls the whole layer "not started."
- `Roadmap.md` "Recently landed" section is missing the four most recent ADR entries that `CHANGELOG.md` already records.
- Two of three `packages/` licensing plan docs carry "Superseded" banners pointing at ADR-0010; one (`REPO-RESTRUCTURING-PLAN.md`) doesn't, still reading as live.
- `docs/README.md` index omits 9 files that exist under `docs/`, including `ATTRIBUTIONS.md` (heavily cross-referenced).

**Tier 2 recommendation:** Reconcile the Crystal Runtime spec trio's self-contradiction; update `Roadmap.md` to reflect that runtime exists and passes 75 tests.

**Status:** Not yet implemented.

---

### Finding 4: The Emotion-Prediction Warehouse Has No Data Source

**Status:** Critical 🔴 (broken, would fail compilation)

**Summary:** `dbt/crystalcore_emotion_warehouse/` is a real, well-modeled 28-class dbt project with staging views, core marts, active-learning queue, sensible macros. But every staging model is a hardcoded CTE of `null` literals; there is not one `source()` call. Running it produces tables of exactly one null row each. Worse, `stg_emotion_labels.sql` ends with a dangling `union all` immediately before closing paren — a genuine SQL syntax error that would fail `dbt compile`.

**Evidence:**
- Repository: TerAustralis-Incognita-Code (inherited from pre-reorg)
- Directory: dbt/crystalcore_emotion_warehouse/
- File: stg_emotion_labels.sql (syntax error), all staging models (null CTEs, no sources)
- Related: dbt_integration.py in codebase writes JSONL but nothing reads it

**Tier 1 recommendation:** Fix the SQL syntax error; decide whether to wire staging models to the JSONL files `dbt_integration.py` already writes, or retire the project until it's ready.

**Status:** Not yet implemented.

---

### Finding 5: The Governance Discipline Is Real and Rare

**Status:** Verified ✅

**Summary:** The project runs on one rule: always mark which lines are dreamed and which are surveyed, never let a dreamed line pretend it was measured. That rule is operationalized as mandatory Science/Vision/Story labels on every PR. The discipline shows up as real editorial discipline throughout — documents about unbuilt systems say so plainly. That's unusual and valuable.

**Evidence:**
- Repository: TerAustralis-Incognita / docs/governance/The-Incognita-Rule.md
- Verified: Operationalized on every PR (Mode header enforced)
- Audit: "The Incognita Rule produces admirably candid 'not built yet' language throughout the docs repo and the demo apps' own SECURITY.md files."

**Details:** Ten ADRs show the same discipline — numbered sequentially, never reused, supersession always explicit. The licensing chaos (ADRs 0006–0010) is documented clearly, not hidden. Decision records are incomplete for pre-ADR history, but everything in the trail is procedurally sound.

**Implications:** This is the reason a review like this is possible at all — the project tells the truth about what's built vs. dreamed, so an external auditor can actually verify claims.

**Recommendation:** Keep this discipline; apply it to the two weakest spots (the repo split itself — haven't updated docs yet, and `packages/` READMEs — still claiming features that were never built).

---

## Component State Matrix

**Status:** Science ✅ (verified by re-run of all mentioned tests)

**Summary:** Each component is in one of four states: Running (built, tested, in production or daily use), Built-not-running (complete, passes tests, not yet deployed), Designed-not-built (spec exists, not implemented), Concept-only (imagined, no spec).

**Evidence:**
- Repository: TerAustralis-Incognita-Code / STATUS.md (fleet-wide ledger)
- Verified: All test re-runs confirmed this session (2026-07-23)

**Details:**

| Component | State | Evidence | Tests | Notes |
|---|---|---|---|---|
| **Starline Weaver** (P2P transport) | Built-not-running ✅ | Implemented, 9 passing tests | 9 self-tests + crypto | Consent_transport module; real Noise protocol |
| **Decode→Ingest→Twin pipeline** | Built-not-running ✅ | Implemented, 4 passing tests | 4 self-tests | Services module; handles data flow |
| **RDP** (Reverse Decision Pipeline, audit kernel) | Built-not-running ✅ | Implemented, 31 passing tests | 31 self-tests + property-based | Hash-chained audit log, kill-switch, 7 property checks |
| **Clementine** (orchestration) | Built-not-running ✅ | Implemented, 7 passing tests | 7 self-tests | Bridge module; multi-agent comms coordination |
| **CrystalBridge** (MCP consent gate) | Built-not-running ✅ | Implemented, 0 test coverage | 🔴 ZERO | Docstring claims 4 checks; code implements 2. Tier 1: add tests. |
| **Crystal Runtime** | Running ✅ | Built, 75 passing tests | 75 pytest | 7 submodules (coordinator, registry, events, config, plugins, logging, API); heavily mocked. Contradicts Roadmap.md which calls it "not started" |
| **Mesh stub** | Built-not-running ✅ | Implemented, 3 passing tests | 3 pytest | Shared transport library; stub only |
| **TypeScript SDK** | Designed-not-built 🔮 | v0.5.0 source, phase 1, documented as Mainnet HOLD | Type-check only | CrystalClient class exists with error handling; not meant for npm publish yet |
| **Lumina companion** | Running ✅ | Shipped, 16 passing tests | 16 pytest | Svelte/Flask, CORS to localhost, real memory/recall; most complete surface in repo |
| **Voicebox** (MCP TTS server) | Running ✅ | Single file, stdlib-only, complete | No tests | Dependency-free, no stubs; small and honest |
| **Demo shells** (crystal-interface, vision-web) | Built-not-running 🔮 | Self-labeled "static demo only… Authority: HOLD" in SECURITY.md | No tests | Unusually candid about honest scope, stubs named by name |
| **Site** (SvelteKit + static adapter) | Running ✅ | Built, deployed, coherent structure | Type-check only | 9 routes (2 markdown-driven, 7 hardcoded components); gallery 92 entries verified in sync with disk |
| **CrystalCore.OS mythos terminal** | Designed-not-built 🔮 | Half text-adventure game, half real ML research (DistilBERT, Bayesian UQ, cross-attention fusion) | No tests | Half fiction, half research; not wired to anything else |
| **CrystalCore Framework** (embedded in Lumina) | Running ✅ | Forked 0.7.0 line, tested via Lumina | 16 tests (via Lumina) | 0.13.4 extras unreconciled (see OPEN-DECISIONS.md) |
| **CrystalCore Protocol pack** | Running ✅ | Real cryptography, disciplined implementation | 51 self-tests | Strongest engineering in repo |
| **dbt emotion warehouse** | Designed-not-built 🔴 | 28-class model, staging views defined, but staging models contain null CTEs with no data source; SQL syntax error | 0 tests | Would fail `dbt compile`; not wired to dbt_integration.py output |

**Summary by state:**
- Running ✅: 5 components (Lumina, voicebox, site, runtime, protocol pack) + 3 live (Mesh, SDK, demos self-aware of HOLD status)
- Built-not-running ✅: 7 components (protocol pack submodules, runtime, mesh) — pass tests, not deployed to users
- Designed-not-built 🔮: 4 components (TypeScript SDK, demo shells, mythos terminal, Framework lineage) — spec/code exists, marked as not-yet-ready
- Concept-only: None (all design has at least a spec)

**Tier 1 issues from this matrix:**
- 🔴 CrystalBridge zero test coverage (security-relevant boundary).
- 🔴 dbt warehouse SQL syntax error + no data source.

---

## Test Coverage Summary

**Status:** Science ✅ (all tests re-run and confirmed 2026-07-23)

**Summary:** 151+ tests passing across the two living repositories. Coverage is bimodal: hand-written original code is rigorously tested; copied code and reconstructed code have none.

**Evidence:**
- Repository: TerAustralis-Incognita-Code (main code repo)
- Verified: Personal re-run of all test commands this session
- Results: No inference from documentation; all reported passes confirmed by execution

**Details:**

| Area | Mechanism | Result | Run by |
|---|---|---|---|
| crystal-core / clementine | selftest.py | 7 / 7 | direct + check.sh |
| crystal-core / consent_transport | selftest.py, real sockets + crypto | 9 / 9 | direct only |
| crystal-core / rdp | selftest.py, 7 property-based checks | 31 / 31 | direct + check.sh |
| crystal-core / services | selftest.py | 4 / 4 | direct + check.sh |
| runtime (7 submodules) | pytest, heavy mocking | 75 | root `pytest` |
| node/mesh | pytest | 3 | root `pytest` |
| crystalcore-os | — | none found | — |
| apps/lumina | pytest + conftest | 16 | check.sh only |
| **Total confirmed:** | — | **70 passing** | TerAustralis-Incognita-Code repo |

**Umbrella repo:** Legacy repo-level `tests/` directory existed pre-reorg; not re-run post-split. Not included in `-Code` tally.

**Coverage gap:** All seven `packages/` directories carry dead test files that nothing ever runs.

**Bimodal distribution:** 
- Hand-written original (protocol pack, runtime, Lumina): heavily tested.
- Copied code (packages/): zero coverage.
- Reconstructed code (CrystalBridge, crystalcore-os): zero coverage.

**Tier 1 recommendation:** At minimum, add tests to CrystalBridge (security boundary).

---

## Naming Collisions Found

**Status:** Drift ⚠️ (documented, not all resolved)

**Summary:** Several terms name more than one thing across the codebase. ADR-0004 resolved the "CrystalCore" collision with a taxonomy; others remain ambiguous.

**Evidence:**
- Repository: TerAustralis-Incognita-Code (code grep + docs)
- Audit method: Textual search across both repos

**Details:**

| Term | Meaning A | Meaning B | Notes |
|---|---|---|---|
| `crystalcore` | MCP bridge package (src/crystalcore/) | Lumina's internal framework (src/apps/lumina/crystalcore/) | Also: src/crystalcore-os/ (game state), "Crystal Core" (protocol pack). Four meanings total. |
| "bridge" | `crystalcore/bridge.py` — MCP stdio server | `clementine/bridge/` — multi-agent chat bus | Unrelated components, same word. |
| scope / provenance | Named but never implemented in `gate.py` docstring | Fully implemented as `ExecutionContext` fields in `runtime/coordinator.py` | Different resource model entirely. |
| "Starline" | Real P2P transport (consent_transport) | Message bus ("Starline Weaver") *and* fictional game state machine | Three meanings in two similarly-titled docs. |

**Tier 2 recommendation:** Disambiguate "Starline," "bridge," and scope/provenance the way ADR-0004 disambiguated "CrystalCore" — a taxonomy ADR would do it.

**Status:** Not yet resolved.

---

## Recommendations by Tier

**Status:** Science ✅ (verified findings with specific, actionable proposals)

### Tier 1 — Cheap, High-Value (Days, Not Weeks)

1. **Fix the repo-split documentation gap** — Add dated note to `SystemMap.md` and root README explaining current two-repo split; reconcile or retire `mythos/README.md`.
2. **Decide `packages/` fate** — Delete, or commit to thin re-exports wired into CI. Current state actively misinforms.
3. **Add tests to CrystalBridge** — Zero coverage on a consent-gate security boundary. Tier 1 priority.
4. **Fix dbt warehouse** — Syntax error in `stg_emotion_labels.sql`; decide whether to wire staging to existing JSONL export or retire until ready.

### Tier 2 — Important, More Surface Area (Weeks)

1. **Reconcile Crystal Runtime specs** — Three same-day docs contradict each other; update `Roadmap.md` to reflect that runtime exists (75 passing tests).
2. **Decide on `crystalcore` / `crystal-core` / `runtime` integration** — Intentionally separate systems (document why, stop echoing vocabulary) or genuinely integrate (one demo-only cross-import already exists).
3. **Disambiguate "Starline"** — Taxonomy ADR per ADR-0004 pattern.
4. **Reconcile archive recovery-status docs** — Two contradictory documents on what was recovered (spaceXAI provider, node.py, status.py).

### Tier 3 — Polish (Spare Afternoon)

1. **Rebuild `docs/README.md` index** — Lists all nine currently-missing files, including `ATTRIBUTIONS.md`.
2. **Fix dead links** — `Access.md`, `Push.md` reference non-existent scripts/files.
3. **Banner `REPO-RESTRUCTURING-PLAN.md`** — Carry same "Superseded" mark as siblings.
4. **Verify live site** — Current audit couldn't reach it (network policy); screenshot or check from unrestricted environment.

---

## Summary

CrystalCore.OS has:
- ✅ **Verified engineering** — Real cryptography, 150+ passing tests, property-based testing on audit kernel.
- ✅ **Rare governance discipline** — Honest Science/Vision labeling, clean ADR trail.
- ⚠️ **Documentation lag** — Split not documented, Roadmap stale, README indices incomplete.
- 🔴 **Specific actionable issues** — `packages/` misleading, dbt syntax error, CrystalBridge untested.
- 🔮 **Open architectural questions** — repo-count decision, integration choice, Framework extract criteria (see OPEN-DECISIONS.md).

The project doesn't need redesign. It needs targeted fixes, documentation updates, and clarity on specific decision gates.

---

**See also:** [ARCHITECTURE.md](ARCHITECTURE.md) (system boundaries), [GOVERNANCE.md](GOVERNANCE.md) (how fixes are decided), [OPEN-DECISIONS.md](OPEN-DECISIONS.md) (decision gates), [TIMELINE.md](TIMELINE.md) (why the current state exists)
