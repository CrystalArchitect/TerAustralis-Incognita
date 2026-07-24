# Repository Portfolio Guide

This knowledge base documents the CrystalCore.OS architecture **exactly as it exists**, not as it might be redesigned. It is a reconstruction of verified implementation, designed decisions, and remaining open questions — not a proposal for what the system should become.

**Source documents:** Project-Boundaries.md §Repositories, architecture-survey.md §1 · **Last verified:** 2026-07-24 · **Labels:** Science ✅ / Vision 🔮 / Drift ⚠️ / Critical 🔴

---

## The Six-Repository Constellation

**Status:** Science ✅ (verified 2026-07-24)

**Summary:** The system spans six repositories: three living (active, in use), three frozen (provenance only, never edited). The three living repos form the complete canonical system today.

**Evidence:**
- Repository: TerAustralis-Incognita / docs/governance/Project-Boundaries.md (rewritten 2026-07-24 from same-day survey of all six)
- Verified: direct inspection of code trees + ls-remote
- Date: Two-repo split implemented as same-day history rewrite 2026-07-23 (per architecture-survey.md §1)

**Details:** See [ARCHITECTURE.md](ARCHITECTURE.md) for the three-project boundary model these repos implement.

---

## Living Repositories

### 1. TerAustralis-Incognita (The Umbrella)

**Status:** Science ✅

**URL:** `https://github.com/CrystalArchitect/TerAustralis-Incognita`

**Role:** Canon and law — the umbrella holds governance, ADRs, architecture documentation, research, the mythos, and mirrors of pre-reorganization code.

**Contents:**
- `docs/` — architecture specs, governance, guides, process documentation (this file is here)
- `docs/adr/` — 11 Architecture Decision Records (ADR-0001 through ADR-0011)
- `docs/governance/` — Constitution, The-Incognita-Rule, Amendment process, Project-Boundaries, Migration-Plan
- `docs/reviews/` — Architecture audit and field surveys
- `mythos/` — The Covenant, The First Remembering, story, art, music, published research on Seven Sisters
- `research/` — Design exploration, seven-sisters cycle, specifications not yet implemented
- `archive/` — Provenance mirrors: frozen repos (tagged snapshots), local-snapshot from pre-reorg era
- `assets/`, `examples/` — Shared assets and demo index

**CI/CD:**
- Markdown lint (`markdownlint-cli2`, lenient config to permit legacy violations)
- External link check (`markdown-link-check`, scope: https?:// links only, local links excluded due to known tool bug)
- Status: green as of 2026-07-24

**What it does NOT contain:** Main application code. `src/`, `tests/`, `scripts/`, `packages/` do not live here (despite older architecture docs incorrectly describing them — see [TECHNICAL-FINDINGS.md](TECHNICAL-FINDINGS.md) drift finding #1).

**Known issues:**
- Drift ⚠️: README.md and docs describe `src/` and `tests/` as if they exist here; they don't (removed as part of same-day 2026-07-23 reorganization, not documented).
- Drift ⚠️: `docs/README.md` index omits 9 files that physically exist in `docs/` (audit Tier 3, not resolved).

**Related:** [ARCHITECTURE.md](ARCHITECTURE.md) (what lives where), [GOVERNANCE.md](GOVERNANCE.md) (how decisions are made), [TIMELINE.md](TIMELINE.md) (why the split happened)

---

### 2. TerAustralis-Incognita-Code (The Engineering Repository)

**Status:** Science ✅ (Stages 1–2 complete, Stage 3–4 deferred)

**URL:** `https://github.com/CrystalArchitect/TerAustralis-Incognita-Code` (private)

**Role:** The complete working software — Crystal Core (engine) and Crystal Vision (application), per Migration-Plan implementation.

**Contents (current structure after Stage 1–2):**

| Area | What | Status | CI/CD |
|---|---|---|---|
| `core/` | Crystal Core: protocol pack (Starline, RDP, consent_transport, services), Clementine orchestration, CrystalBridge, mesh stub, TypeScript SDK | Science ✅ | compileall, 4 self-test suites (51 tests passing) |
| `core/crystal-core/` | Protocol pack: Starline Weaver, Decode→Ingest→Twin pipeline, Consent Transport, RDP (Reverse Decision Pipeline), audit kernel | Science ✅ | 51 self-tests, property-based testing |
| `core/crystalcore/` | CrystalBridge: fail-closed MCP consent gate, profile configurations | Science ✅ | Zero test coverage (Tier 1 recommendation: add tests) |
| `core/profiles/` | Configuration profiles for CrystalBridge | Science ✅ | — |
| `core/node/mesh/` | Mesh stub: shared transport library | Science ✅ | 3 pytest |
| `core/sdk/typescript/` | TypeScript client API scaffold (v0.5.0, Phase 1 / Mainnet HOLD) | Science ✅ | Type-check only |
| `vision/` | Crystal Vision: Lumina companion, demo shells, voicebox, site source | Science ✅ | Lumina pytest (16 tests), voicebox (no tests), shells (self-labeled HOLD) |
| `vision/apps/lumina/` | Sovereign companion + embedded CrystalCore Framework | Science ✅ | 16 tests via check.sh (excluded from root pytest) |
| `vision/apps/lumina/crystalcore/` | Embedded Framework (forked 0.7.0 line; 0.13.4 rescue unreconciled) | Science ✅ | Tested via Lumina suite |
| `vision/apps/voicebox/` | Local MCP text-to-speech server, stdlib-only, single file | Science ✅ | — |
| `vision/apps/crystal-interface/` | Static demo shell (operator interface), Authority HOLD | Science ✅ | — |
| `vision/apps/vision-web/` | Static demo shell (citizen interface), honest scope callouts | Science ✅ | — |
| `vision/site/` | Public site source (SvelteKit + static adapter, 9 routes through markdown + hardcoded components) | Science ✅ | Type-check only |
| `vision/site/src/content/` | Markdown-driven content (22 files auto-loaded at build time) | Science ✅ | Part of site typecheck |
| `LICENSE` | CC BY-NC-ND 4.0 (per ADR-0010, 2026-07-23) | Science ✅ | — |
| `CNAME` | teraustralis.com.au (moved from umbrella Stage 2, 2026-07-23) | Science ✅ | — |
| `.github/workflows/` | CI workflows (moved from umbrella Stage 2): deploy.yml (Pages), GitHub Actions checks | Science ✅ | All green |

**Test coverage (all re-run and confirmed 2026-07-23):**
- Core protocol pack: 51 self-tests (clementine 7, consent_transport 9, rdp 31, services 4)
- Core mesh: 3 pytest
- Vision Lumina: 16 tests
- **Total in `-Code` repo: 70 tests passing**
- Additional umbrella tests: mesh stub 3 + (legacy repo-level tests not re-run)

**CI/CD pipeline (as of 2026-07-24):**
- `compileall` — verify all .py files compile
- `clementine.bridge.selftest` — run 7 integration tests on orchestration layer
- `consent_transport.selftest` — run 9 crypto + socket tests on P2P transport
- `rdp.selftest` — run 31 property-based tests on audit kernel
- `services.selftest` — run 4 tests on decode/ingest pipeline
- `Lumina pytest` — run 16 tests on companion app
- `mesh pytest` — run 3 tests on transport stub
- **Pages deploy** — build and publish site to GitHub Pages

**Known issues:**
- Drift ⚠️: The repo contains a top-level `dbt/` directory inherited from umbrella; unclear if it belongs here or Stage 4 defers it (see [OPEN-DECISIONS.md](OPEN-DECISIONS.md))
- Drift ⚠️: No repo-level `scripts/` or `tests/` directories (Stage 2 decision: skip until CI matures)

**Stage 1–2 implementation:**
- PR #1 (Stages 1–2): Charter README + imported core/ (crystal-core, crystalcore, profiles, node/mesh, sdk/typescript) + LICENSE
- PR #2 (Stage 1–2): Imported vision/ (apps, site) + Pages deploy moved from umbrella
- Status: both merged, main in working order

**Stage 3–4 open decisions:** See [OPEN-DECISIONS.md](OPEN-DECISIONS.md) (repo-count split, Framework extract, site/dbt placement)

**Related:** [ARCHITECTURE.md](ARCHITECTURE.md) (three-project boundary), [TECHNICAL-FINDINGS.md](TECHNICAL-FINDINGS.md) (component integration findings)

---

### 3. CrystalCore.OS-the-Crystal-Architecture-Archive (The Ledger)

**Status:** Science ✅

**URL:** `https://github.com/CrystalArchitect/CrystalCore.OS-the-Crystal-Architecture-Archive`

**Role:** System ledger — one canonical STATUS.md tracking state, receipts, and known unknowns across all repositories.

**Contents:**
- `STATUS.md` — fleet-wide state matrix (Running / Built-not-running / Designed-not-built / Concept-only)
- Intentionally small; aggregation only, no data duplication

**CI/CD:** None (ledger only)

**Purpose:** Single source of truth for component state across all six repos, preventing drift between repo-local documentation and fleet-wide awareness.

**Related:** [TECHNICAL-FINDINGS.md](TECHNICAL-FINDINGS.md) (component state details with evidence)

---

## Frozen Provenance Repositories

**Status:** Science ✅ (frozen as of 2026-07-17, verified via tag)

**Summary:** Three repositories are deliberately preserved as checkpoints, unedited and read-only, to preserve code provenance before the 2026-07-23 reorganization.

**Policy:** Frozen repos are never edited. Code has been salvaged into living repos where applicable. These repos answer the question: "Where did this code come from, and what changed when it was moved?"

**Note:** End-state of these repos (GitHub archive as read-only flag vs. leave as-is) is a Stage 3 decision (see [OPEN-DECISIONS.md](OPEN-DECISIONS.md)).

---

### The-Crystal-Vision

**Status:** Frozen ✅

**Tag:** `vision-safe-2026-07-17`

**URL:** `https://github.com/CrystalArchitect/The-Crystal-Vision`

**Captured:** Codex site + Clementine companion; complete **crystalcore v0.13.4 bytecode rescue**

**Code lives on as:**
- Ancestor of Lumina's embedded framework (which forked the 0.7.0 branch — the 0.13.4 extras, SpaceXAI provider, `node.py`, `status.py`, CLI remain unreconciled in this frozen repo; see [OPEN-DECISIONS.md](OPEN-DECISIONS.md))

**Use case:** If questions arise about original implementation details, design intent, or pre-reorg behavior, this is the archive to consult.

---

### crystalcore

**Status:** Frozen ✅

**Tag:** `crystalcore-safe-2026-07-17`

**URL:** `https://github.com/CrystalArchitect/crystalcore`

**Captured:** The Songline protocol pack (SonglineBus, original architecture before Starline Weaver)

**Code lives on as:**
- Direct ancestor of `core/crystal-core` (SonglineBus → Starline Weaver, architectural evolution preserved in commit history)

**Use case:** Trace the evolution of the protocol pack from Songline to Starline; understand pre-reorg design.

---

### crystal-vision

**Status:** Frozen ✅

**Tag:** `crystal-vision-safe-2026-07-17` (if used; not confirmed in this session)

**URL:** `https://github.com/CrystalArchitect/crystal-vision`

**Captured:** Static demo shell (Grok build)

**Code lives on as:**
- Direct ancestor of `vision/apps/crystal-interface` (operator interface)

**Use case:** Compare original vs. migrated demo shell; understand design evolution of operator interface.

---

## Cross-Repository Dependencies

**Status:** Science ✅ (one documented pipeline)

**Summary:** The only automated cross-repo dependency is the public site pipeline: mythology content flows from umbrella to application repo to Pages.

**Evidence:**
- Repository: both living code repos
- File: vision/site/src/content/, mythos/ (umbrella)
- Date: Established Stage 2 (2026-07-23)

**Pipeline:**

```
mythos/ (umbrella, canonical)
   ↓ (manual copy)
vision/site/src/content/ (-Code)
   ↓ (SvelteKit build)
.github/workflows/deploy.yml (-Code Pages)
   ↓ (Pages)
www.teraustralis.com.au (live)
```

**Known gap:** The First Remembering (canonical in umbrella as of 2026-07-24) has not yet been copied into site content. This is a known drift risk: not-yet-published content.

**Implication:** Site renders *copies*, not canon directly. Publishing delay is acceptable design for small team; CI/CD automation of this copy would be Stage 3–4 enhancement.

**Related:** [ARCHITECTURE.md](ARCHITECTURE.md) (three-project boundary), [OPEN-DECISIONS.md](OPEN-DECISIONS.md) (site sync decision)

---

## Summary Matrix

| Repository | Type | Role | Main Audience | Status | CI/CD |
|---|---|---|---|---|---|
| TerAustralis-Incognita | Living | Umbrella (canon) | Maintainers, contributors, researchers | Science ✅ | Lint + link check |
| TerAustralis-Incognita-Code | Living | Engineering (Stages 1–2) | Developers, deployers | Science ✅ | 70 tests passing |
| CrystalCore.OS-the-Crystal-Architecture-Archive | Living | Ledger | All repos | Science ✅ | — |
| The-Crystal-Vision | Frozen | Provenance (v0.13.4 rescue) | Archaeology | Science ✅ | — |
| crystalcore | Frozen | Provenance (Songline pack) | Archaeology | Science ✅ | — |
| crystal-vision | Frozen | Provenance (demo shell) | Archaeology | Science ✅ | — |

---

**See also:** [ARCHITECTURE.md](ARCHITECTURE.md) (three-project boundary model), [TECHNICAL-FINDINGS.md](TECHNICAL-FINDINGS.md) (what's working, what's broken in each repo), [TIMELINE.md](TIMELINE.md) (why the constellation looks like this)
