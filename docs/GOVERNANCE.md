# Governance Reference

This knowledge base documents the CrystalCore.OS architecture **exactly as it exists**, not as it might be redesigned. It is a reconstruction of verified implementation, designed decisions, and remaining open questions — not a proposal for what the system should become.

**Source documents:** ADR-0001 through ADR-0011, Constitution.md, The-Incognita-Rule.md · **Last verified:** 2026-07-23 (ADR dates) · **Labels:** Science ✅ / Vision 🔮 / Locked (immutable except via Constitution §8)

---

## The Incognita Rule: Honesty Doctrine

**Status:** Science ✅ (operationalized since project inception)

**Summary:** The single governing rule of the project: always mark which lines are dreamed and which are surveyed, and never let a dreamed line pretend it was measured. This is operationalized as mandatory Science/Vision/Story labels on every PR and throughout documentation.

**Evidence:**
- Repository: TerAustralis-Incognita / docs/governance/The-Incognita-Rule.md
- Enforced: Every PR carries a Mode header (Science / Vision / Story)
- Audit finding: "The honesty discipline is the project's best asset" (architecture-survey.md §2)

**Details:**

The rule distinguishes three states:
- **Science:** What exists and is verified — code that runs, tests that pass, git history, measurement.
- **Vision:** What is designed but not yet built — specifications, storytelling, hypothetical futures, "we plan to."
- **Story:** Mythology, cultural narrative, non-engineering knowledge — the Covenant, art, research, lived experience.

Every statement in the repository is labeled with its state. Documentation does not conflate "we built" with "we want to"; code does not pose as design.

**Operationalization:**

Every PR carries a Mode header:

```
Mode: [Science | Vision | Story]

Description of what's changing and why.
```

This forces the author to declare upfront: are you shipping implementation, adding spec, or expanding story?

**Implications:** 
- Readers know immediately whether they're reading executable fact or design speculation.
- Prevents cognitive load of inferring confidence from narrative tone.
- The rule is rarely broken (audit rated "real and rare" discipline).

**Related:** [ARCHITECTURE.md](ARCHITECTURE.md) (Belt-Three model), [TECHNICAL-FINDINGS.md](TECHNICAL-FINDINGS.md) (where Science and Vision diverge today)

---

## Locked Names (Constitution §1)

**Status:** Locked (immutable except via Constitution §8 amendment)

**Summary:** Three names are locked by Constitution §1 and carry specific, narrow meanings. No new component takes a locked name; they are reserved.

**Evidence:**
- Repository: TerAustralis-Incognita / docs/governance/Constitution.md §1
- Enforced by: ADR-0004 (naming taxonomy lock), ADR-0007 (spelling correction)

**Details:**

| Name | Meaning | Use | Status |
|---|---|---|---|
| **TerAustralis Incognita** | Outer civilizational vision — the Unknown Southern Land awakening | Umbrella project, public-facing name, trademark | Locked ✅ |
| **CrystalVision** | Sensing / dreaming / directing interface (Crystal ↔ Lattice) | Interface concept, Vision-layer product name | Locked ✅ |
| **CrystalCore.Lattice** | Substrate — multi-AI weave, memory, ontology, activation | Architecture component (designed, not-built) | Locked ✅ |

**Important:** These names are reserved and cannot be reused. Attempts to name a new component "CrystalCore-Something" require a new ADR (per ADR-0004).

**Related:** ADR-0004, IP-LICENSING.md (naming debts)

---

## The Four-Branch CrystalCore Taxonomy (ADR-0004)

**Status:** Science ✅ (adopted 2026-07-23)

**Summary:** "CrystalCore" already names five different things. To prevent future proliferation, the project adopted a canonical four-branch taxonomy locking those meanings and banning any fifth.

**Evidence:**
- Repository: TerAustralis-Incognita / docs/adr/ADR-0004.md (2026-07-23)
- Reference: docs/vision/CrystalCore.md (taxonomy source of truth)

**Details:**

| Branch | What | Where | Status |
|---|---|---|---|
| **CrystalCore Framework** | Lumina's embedded engine (forked 0.7.0 line) | vision/apps/lumina/crystalcore/ | Science ✅ |
| **CrystalCore Protocol** | The protocol pack (Starline Weaver, RDP, Consent Transport) | core/crystal-core/ | Science ✅ |
| **CrystalBridge** | The MCP consent gate (integration layer) | core/crystalcore/ | Science ✅ |
| **CrystalCore OS** | This repository's platform/governance architecture | Umbrella governance | Science ✅ |

**The collision:** "CrystalCore.OS" (the mythos terminal) nearly collides with "CrystalCore OS" (the platform name). ADR-0004 documents this as the taxonomy's "one open case" rather than papering over it.

**The ban:** No future runtime component becomes a fifth "CrystalCore." Candidates raised in review (Crystal Runtime, Crystal Nexus, Crystal Coordinator, Crystal Kernel) were rejected; new components must describe their role in names like those.

**Implications:** Readers can look up "CrystalCore" and find exactly four meanings. Naming is disambiguated at the design stage, not hidden in implementation.

**Related:** ADR-0004, IP-LICENSING.md (naming debts)

---

## Architecture Decision Records (ADRs 0001–0011)

**Status:** Science ✅ (all adopted, numbered sequentially, procedurally spotless)

**Summary:** Eleven Architecture Decision Records govern the project. Each is a dated decision on a specific topic; supersession is always explicit; the trail is complete and auditable.

**Evidence:**
- Repository: TerAustralis-Incognita / docs/adr/
- Verified: Numbers never reused, status labels match headers exactly, procedural review trail complete

**Details:**

| ADR | Date | Topic | Status | Supersedes |
|---|---|---|---|---|
| **ADR-0001** | 2026 | Adopt monorepo architecture (CrystalCore OS v1.0) | Accepted | — |
| **ADR-0002** | 2026 | Keep `mythos/` as peer of `docs/` and `src/`, not folded | Accepted | — |
| **ADR-0003** | 2026 | Move code into `src/` as uniform one-level shift, preserving `__file__`-relative paths | Accepted | — |
| **ADR-0004** | 2026-07-23 | Lock the four-branch CrystalCore taxonomy; ban future CrystalCore-* names | Accepted | — |
| **ADR-0005** | 2026 | AI Orchestrator as recommend-then-human-decides, never autonomous dispatch; first increment documentation only | Accepted | — |
| **ADR-0006** | 2026 | Dual-license decision (Apache-2.0 code / CC BY-NC-ND mythos); IP principles, trademark sections | Accepted | Superseded by ADR-0008 §1 |
| **ADR-0007** | 2026 | Correct project name to "TerAustralis Incognita" (one 'a') per maintainer's registered ABN | Accepted | — |
| **ADR-0008** | 2026 | Supersede ADR-0006 §1: adopt CC BY-NC-ND 4.0 for all code, after same-day session conflict | Accepted | ADR-0006 §1 only |
| **ADR-0009** | 2026 | Reconcile same-day licensing collision (three uncoordinated sessions + one push in ~45 min) | Accepted | — |
| **ADR-0010** | 2026 | Close differentiated per-package licensing question: uniform CC BY-NC-ND 4.0 for whole repository | Accepted | ADR-0006, ADR-0008, ADR-0009 |
| **ADR-0011** | 2026-07-23 | Adopt three-project boundary model (umbrella / Crystal Core / Crystal Vision) and Stage-gated migration plan with per-stage maintainer approval | Accepted | ADR-0001 (reframes monorepo model in project terms) |

**Key attributes:**
- **Procedural integrity:** Numbers sequential, never reused; supersession explicit; status headers consistent with decisions.
- **Licensing evolution:** ADRs 0006–0010 show real-time conflict resolution (three uncoordinated sessions made incompatible choices; the trail documents how it was resolved, not hidden).
- **Naming governance:** ADR-0004 and ADR-0007 lock critical names and freeze spelling, preventing future churn.
- **Architecture:** ADR-0011 (2026-07-23) establishes the current three-project boundary; it supersedes ADR-0001's monorepo model only in project framing.

**Related:** Individual ADRs in `docs/adr/`, IP-LICENSING.md (ADRs 0006–0010 licensing trail)

---

## Amendment Process (Constitution §8)

**Status:** Science ✅ (established governance process)

**Summary:** Changes to locked names (Constitution §1) require a §8 amendment — a higher gate than a regular ADR. Everything else is amendable by new ADR.

**Evidence:**
- Repository: TerAustralis-Incognita / docs/governance/Constitution.md §8
- Enforced by: Project-Boundaries.md (amendment process noted)

**Details:**

| Type of change | Approval gate | Mechanism | Examples |
|---|---|---|---|
| Locked names (Constitution §1) | §8 amendment (highest gate) | Dated amendment to Constitution with explicit rationale | Renaming TerAustralis Incognita, CrystalVision, CrystalCore.Lattice |
| Architecture decisions | New ADR (standard gate) | Numbered sequentially, dated, procedurally reviewed | ADR-0004 (naming taxonomy), ADR-0011 (three-project boundary) |
| Policy clarifications | PR or amendment (lower gate) | Comments in existing documents if clarification; new ADR if real decision | Re-interpreting existing ADR intent vs. changing direction |
| Documentation corrections | PR (no special gate) | Ordinary code review, Mode header for PR | Fixing broken links, updating stale references, correcting descriptions of current state |

**Implications:** Locked names stay locked. Architecture questions get recorded in the ADR trail so future decisions can reference why earlier choices were made.

**Related:** Constitution.md §8, [OPEN-DECISIONS.md](OPEN-DECISIONS.md) (decisions awaiting future choices)

---

## Decision Audit Trail

**Status:** Science ✅

**Summary:** The 11 ADRs plus the Constitution form a complete, auditable trail of how the project's governance evolved.

**Key findings from architecture-survey.md §2:**
- ✅ "The governance discipline is real and rare." 
- ✅ "A formal Science / Story / Vision labeling rule, honestly applied almost everywhere it counts."
- ✅ "An ADR trail that is procedurally spotless even when its subject matter (licensing) was chaotic."

**Implications:** Future contributors can read the trail and understand not just *what* the project decided, but *why*, in which order, and what the prior state was.

---

## Summary

The CrystalCore.OS governance rests on:
- **The Incognita Rule:** Always mark dreamed lines and surveyed lines; never confuse them.
- **Locked names:** Three names are immutable (TerAustralis Incognita, CrystalVision, CrystalCore.Lattice).
- **CrystalCore taxonomy:** Four branches, one future ban on adding a fifth.
- **Eleven ADRs:** Complete, procedurally clean trail from ADR-0001 to ADR-0011.
- **Constitution §8:** Amendment process for locked names (highest gate); new ADR for architecture decisions.

This governance prevents naming collisions, licensing churn, architectural inversion, and loss of decision history.

---

**See also:** [ARCHITECTURE.md](ARCHITECTURE.md) (Belt-Three model operationalization), [TECHNICAL-FINDINGS.md](TECHNICAL-FINDINGS.md) (where governance rules meet reality), [IP-LICENSING.md](IP-LICENSING.md) (licensing ADR trail), [OPEN-DECISIONS.md](OPEN-DECISIONS.md) (decisions awaiting future conditions)
