# IP, Licensing & Naming Debts

This knowledge base documents the CrystalCore.OS architecture **exactly as it exists**, not as it might be redesigned. It is a reconstruction of verified implementation, designed decisions, and remaining open questions — not a proposal for what the system should become.

**Source documents:** ADR-0006, ADR-0008, ADR-0009, ADR-0010 (licensing), ADR-0004, ADR-0007 (naming), Constitution §7, Migration-Plan debts register · **Last verified:** 2026-07-23 (ADR dates) · **Labels:** Science ✅ / Vision 🔮 / Locked / Resolved / Outstanding

---

## Current License: Uniform CC BY-NC-ND 4.0

**Status:** Science ✅ (adopted ADR-0010, 2026-07-23)

**Summary:** All code and documentation in both living repositories are licensed under Creative Commons BY-NC-ND 4.0 — uniform, no differentiation. This resolved three years of uncoordinated licensing attempts.

**Evidence:**
- Repository: TerAustralis-Incognita-Code / LICENSE (top level)
- ADR trail: ADR-0006 → ADR-0008 → ADR-0009 → ADR-0010 (final resolution)
- Date: ADR-0010 adopted 2026-07-23

**Details:**

| Element | License | Status | Source |
|---|---|---|---|
| All `.py` code | CC BY-NC-ND 4.0 | Science ✅ | ADR-0010 (final) |
| Documentation (docs/) | CC BY-NC-ND 4.0 | Science ✅ | ADR-0010 (final) |
| Mythos (mythos/) | CC BY-NC-ND 4.0 | Science ✅ | ADR-0010 (final); own `LICENSE-CONTENT.md` referenced |
| Research (research/) | CC BY-NC-ND 4.0 | Science ✅ | ADR-0010 (final) |

**Evolution:**
- **ADR-0006** (2026): Original decision — Apache-2.0 for code, CC BY-NC-ND for mythos (dual license).
- **ADR-0008** (2026): Supersede ADR-0006 §1 after same-day session conflict — all code to CC BY-NC-ND 4.0.
- **ADR-0009** (2026): Reconcile another same-day collision — three sessions + one direct push landed incompatible per-package licenses within 45 minutes.
- **ADR-0010** (2026-07-23): Final closure — uniform CC BY-NC-ND 4.0 for the whole repository; no differentiated per-package licensing.

**Implications:** The license is single, clear, and immutable without a new ADR. Anyone using the code knows immediately what restrictions apply.

**Related:** ADR-0006, ADR-0008, ADR-0009, ADR-0010 (ADR trail), Constitution §8 (amendment process)

---

## Intellectual Property Principles (ADR-0006 Survivor)

**Status:** Locked (immutable without ADR)

**Summary:** ADR-0006 established IP principles that survive all three licensing updates. These are standalone governance statements, not overridden by ADR-0010's license change.

**Evidence:**
- Repository: TerAustralis-Incognita / docs/adr/ADR-0006.md §IP Principles and Trademark sections
- Date: Established 2026 with ADR-0006; explicitly preserved despite ADR-0008/ADR-0010 license updates

**Details:**

| Principle | Meaning | Status |
|---|---|---|
| **No third-party trademarks** | CrystalCore.OS does not use, claim, or invent third-party marks. All identifiers are original. | Locked ✅ |
| **Attribution required** | Use of the code requires attribution to the project and maintainer (CC BY-NC-ND 4.0 requirement). | Locked ✅ |
| **Non-commercial only** | No commercial redistribution without explicit approval (CC BY-NC-ND 4.0 restriction). | Locked ✅ |
| **No derivative licensing** | Derivatives keep the same CC BY-NC-ND 4.0 license (ND = No Derivatives, so this means no relicensing). | Locked ✅ |

**Implications:** The project's IP stance is consumer-protective and contributor-accessible (non-commercial, open-source, attribution preserved).

---

## The Four-Branch CrystalCore Taxonomy Lock (ADR-0004)

**Status:** Locked (immutable without ADR)

**Summary:** Four branches exhaust all current "CrystalCore" uses. No new component becomes a fifth "CrystalCore." This prevents naming collision and keeps the taxonomy stable.

**Evidence:**
- Repository: TerAustralis-Incognita / docs/adr/ADR-0004.md (2026-07-23)
- Reference: docs/vision/CrystalCore.md (taxonomy source of truth)

**Details:**

| Branch | What | Owner | Status |
|---|---|---|---|
| **CrystalCore Framework** | Lumina's embedded engine (forked 0.7.0 line) | Crystal Vision | Science ✅ |
| **CrystalCore Protocol** | Starline Weaver, RDP, Consent Transport | Crystal Core | Science ✅ |
| **CrystalBridge** | MCP consent gate | Crystal Core | Science ✅ |
| **CrystalCore OS** | Platform/governance architecture | Umbrella | Science ✅ |

**The ban:** No future components get a CrystalCore name. Candidates raised in review (Crystal Runtime, Crystal Nexus, Crystal Coordinator, Crystal Kernel) were all rejected. New components must self-describe their role.

**Open case:** The mythos terminal (`CrystalCore.OS`) nearly collides with the platform name (`CrystalCore OS`). This is documented as the taxonomy's "one open collision" (ADR-0004 §Consequences) rather than silently resolved.

**Implications:** The four branches are locked; future naming is disambiguated at design stage.

---

## Naming Debts & Resolved Issues

**Status:** Science ✅ (verified through git, PyPI checks, and ADR trail)

**Summary:** The project has resolved two major naming debts and carries two outstanding debts with clear stage gates.

**Evidence:**
- Repository: TerAustralis-Incognita / docs/governance/Migration-Plan.md (debts register)
- Verified: 2026-07-23 and 2026-07-24

**Details:**

### Resolved Naming Debts ✅

| Debt | Where | Status | Resolution |
|---|---|---|---|
| GitHub slug `TeraAustralis-Incognita` (double-a) | This repo's URL | ✅ Resolved | GitHub API returned `CrystalArchitect/TerAustralis-Incognita` (one 'a') per ADR-0007 correction, confirmed PR #48 creation 2026-07-23. ADR-0007's "still-unrenamed" line stands as historical record only. |
| PyPI package names `teraaustralis-*` (double-a) | Dormant publish/test workflows | ✅ Resolved | Verified 2026-07-23: zero git tags ever pushed (publish workflow was tag-gated, so never fired). Spot-checked 2 of 7 names on PyPI (`teraaustralis-lumina`, `teraaustralis-bridge`) — both unclaimed (404). Both workflows removed at Stage 2; corrected names (`teraustralis-*`) free to reserve. |

### Outstanding Naming Debts 🔮

| Debt | Where | Constraint | Stage gate |
|---|---|---|---|
| `corpus/` named as a surface of truth | Constitution §7 | Never built; fixing requires §8 amendment | Proposed amendment text (not applied): "§7: mark `corpus/` as designed-but-not-built until export pipeline exists, matching 2026-07-21 pattern." |
| Deeper stale references in `mythos/README.md` (old `src/` links, pre-monorepo framing) | `mythos/` | Vision-layer content — edit requires explicit maintainer sign-off (Stage 0 blurb fix was minimum honest correction) | Vision-layer amendment, Stage 1+ implementation with maintainer approval. |

**Implication:** The two resolved debts are closed by git verification (API response, PyPI check, git log). The two outstanding debts require explicit governance action (Constitution amendment, Vision-layer sign-off) and are deliberately held open until their stage gates.

---

## Licensing Evolution Timeline

**Status:** Science ✅ (documented in ADR trail)

**Summary:** The project experienced real licensing chaos in the same morning. The ADR trail captures how it was resolved, not hidden.

**Evidence:**
- Repository: TerAustralis-Incognita / docs/adr/ (ADR-0006 through ADR-0010)
- Date: Multiple sessions on one day (2026)

**Details:**

### Session 1: Original Decision (ADR-0006)

- **Proposal:** Dual-license — Apache-2.0 for code, CC BY-NC-ND for mythos.
- **Result:** Adopted as ADR-0006.
- **Issue:** Three uncoordinated sessions later in the same day made incompatible choices.

### Session 2: Uncoordinated Code License Change

- **What happened:** One session unilaterally changed code from Apache-2.0 to CC BY-NC-ND 4.0.
- **How it was resolved:** ADR-0008 was written to retroactively adopt this choice, superseding ADR-0006 §1 only (IP principles and trademark sections preserved).

### Session 3: Another Uncoordinated Change

- **What happened:** Another session created per-package differentiated licensing within the already-chaotic tree.
- **How it was resolved:** ADR-0009 reconciled the collision; a dated decision record explaining the root cause and choosing root-license-governs.

### Session 4: Final Closure (ADR-0010)

- **Decision:** Uniform CC BY-NC-ND 4.0 for the entire repository. No per-package differentiation.
- **Supersedes:** ADR-0006 (license part only), ADR-0008 (incorporates its choice), ADR-0009 (final word on per-package question).
- **Keeps:** ADR-0006 IP principles and trademark sections (standalone governance).

**Implications:** The chaos is documented, not hidden. Future contributors can read the trail and understand what went wrong, when, and how it was fixed. The Incognita Rule (Science/Vision/Story labeling) allowed this chaos to be captured honestly rather than papered over.

---

## Trademark Status

**Status:** Locked (immutable without ADR)

**Summary:** The project uses original identifiers only; no third-party trademarks are claimed or embedded.

**Evidence:**
- Repository: TerAustralis-Incognita / docs/adr/ADR-0006.md (trademark section, preserved by ADR-0010)
- Verified: No third-party marks in code, docs, or branding

**Details:**
- **TerAustralis Incognita** — Original mark, associated with maintainer's registered ABN (ADR-0007 spelling correction).
- **CrystalCore** — Original mark (four-branch taxonomy, ADR-0004).
- **CrystalVision** — Original mark (locked name, Constitution §1).
- **Lumina** — Original name.
- **Starline** — Original name.

**Implications:** The project's branding is independent and protected from third-party licensing complications.

---

## Summary

CrystalCore.OS licensing and naming:

**License (Science ✅):**
- Uniform CC BY-NC-ND 4.0 (all code and docs).
- Resolved after same-day chaos documented in ADR trail (ADR-0006 → ADR-0008 → ADR-0009 → ADR-0010).
- IP principles (attribution, non-commercial, no derivatives) locked as separate governance.

**Naming (Mixed Status):**
- Four-branch CrystalCore taxonomy locked (ADR-0004).
- Two major debts resolved (GitHub slug, PyPI names).
- Two outstanding debts with clear stage gates (Constitution §7 amendment for `corpus/`, Vision-layer sign-off for `mythos/` deep references).

**Trademark (Locked):**
- All original identifiers; no third-party marks claimed or embedded.

---

**See also:** [GOVERNANCE.md](GOVERNANCE.md) (locked names, Constitution §8 amendment process), [TECHNICAL-FINDINGS.md](TECHNICAL-FINDINGS.md) (where these principles meet practice), [OPEN-DECISIONS.md](OPEN-DECISIONS.md) (outstanding policy questions)
