# DECISIONS

Summaries only. The ADR file is the record. Status column in
[`docs/adr/README.md`](../docs/adr/README.md) is authoritative.

**How an ADR becomes Accepted:** maintainer merges the PR that carries it
([`Decision-Records.md`](../docs/governance/Decision-Records.md)). Until
then it is Proposed. Do not treat a draft ADR as law.

**Write-back:** when a new ADR is merged, add a row here and point at the
file. Do not rewrite Accepted ADRs. A reversed decision gets a new ADR.

**Sourced:** 2026-08-28 from the ADR index on
`bdddf0cdf4c2e47f7d517aaf9edbf1a9ba928b08`.

| ADR | Title (from the index) | Status | Memory note |
|---|---|---|---|
| [0001](../docs/adr/ADR-0001.md) | Adopt the CrystalCore OS v1.0 repository architecture | Accepted | Layout: docs / mythos / research / archive. Historical implementer named in the ADR stays as written. |
| [0002](../docs/adr/ADR-0002.md) | Content areas: the mythos stays a top-level peer of docs and src | Accepted | License-area split, not a nesting under `docs/`. |
| [0003](../docs/adr/ADR-0003.md) | Move code into src/ as a uniform shift; keep runtime-coupled files with their code | Accepted | Describes a tree that is **not in this git** (see README status note). |
| [0004](../docs/adr/ADR-0004.md) | Lock the CrystalCore naming taxonomy; ban future CrystalCore-* runtime names | Accepted | Framework / Protocol / CrystalBridge / OS. Collision with the mythos terminal is documented, not silently resolved. |
| [0005](../docs/adr/ADR-0005.md) | AI Orchestrator — consolidate the naming; ship the concept as documentation first | Accepted | Recommend, then a human decides. No autonomous dispatch runtime. |
| [0006](../docs/adr/ADR-0006.md) | Licensing strategy — keep the dual license, record the IP principles, flag trademark as unfinished | Accepted — §1 superseded by ADR-0008 | IP principles in later sections still stand per the index/CHANGELOG. |
| [0007](../docs/adr/ADR-0007.md) | Correct the project name to "TerAustralis Incognita"; rename mythos/teraaustralis/ | Accepted | One *a*. Constitution §1 amended via §8. Historical ADRs 0001/0002 left unedited. |
| [0008](../docs/adr/ADR-0008.md) | Supersede ADR-0006 §1 — adopt CC BY-NC-ND 4.0 for code; reconcile the fallout | Accepted | Code license direction confirmed by the maintainer. |
| [0009](../docs/adr/ADR-0009.md) | Reconcile the licensing chaos — CC BY-NC-ND governs today; packages/ is an in-progress target | Accepted — target question resolved by ADR-0010 | Do not reopen the four-license model without a new ADR. |
| [0010](../docs/adr/ADR-0010.md) | Uniform CC BY-NC-ND 4.0 for the whole repository; differentiated per-package licensing not adopted | Accepted | Terminus of the 2026-07-23 license sequence. |
| [0011](../docs/adr/ADR-0011.md) | Adopt the three-project boundary model — umbrella, Crystal Core, Crystal Vision | Accepted | This git is the umbrella (no main app code). Decided-NOT: no renames, no moves, no new repos in that ADR. |
| [0012](../docs/adr/ADR-0012.md) | Site visual-token layer now; domain restructure deferred behind triggers | **Proposed** | Not law until merged. Palette unchanged; nested layouts / new routes deferred. |
| [0013](../docs/adr/ADR-0013.md) | Extend uniform CC BY-NC-ND 4.0 across the whole portfolio; retire Apache-2.0 and the unlicensed repositories | Accepted | Portfolio-wide, not only this umbrella. |
| [0014](../docs/adr/ADR-0014.md) | Grok Build takes the Repository Engineer seat; Claude retained as history | Accepted (PR #116) | This memory protocol does **not** undo this ADR. Claude returning later needs a new ADR. |
| [0015](../docs/adr/ADR-0015.md) | Stop growing the constellation — no new GitHub repository without an ADR | Accepted (PR #118) | Nineteen repos measured 2026-08-20. Agents do not create repositories. Sandbox is not a repository. |
| [0016](../docs/adr/ADR-0016.md) | Recognize samuelsalmon3/SourceCode as an external peer, not a CrystalCore module | **Proposed** | Neighbor recorded; engines not fused. Becomes Accepted on merge of its PR. |

## Seat and repo-count (load-bearing)

- **Grok Build** = Repository Engineer. **Creative Grok** = separate seat.
  A Grok App Builder sandbox is not a CrystalCore.OS product and is not
  the estate ([ADR-0014](../docs/adr/ADR-0014.md)).
- Next work lands in an existing living repo ([ADR-0015](../docs/adr/ADR-0015.md)
  landing table). Splitting `-Code` into core/vision still requires
  Migration-Plan Stage 3 criteria **and** ADR-0015.

## Not decided here

Starline taxonomy (three meanings) has **no ADR yet**. See
[`OPEN-QUESTIONS.md`](OPEN-QUESTIONS.md). Do not mint component names that
use **Songline**.
