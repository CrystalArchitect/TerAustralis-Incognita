# Migration plan — from described layout to real boundaries

> **Status: PROPOSAL (Vision layer).** Nothing in this document is
> executed, scheduled, or authorized by its existence. Each stage is
> separately approvable and separately reversible; the maintainer's
> explicit approval, stage by stage, is the gate
> ([`ADR-0011`](../adr/ADR-0011.md)). The *Measured starting point* section
> is Science; everything after it is plan.

Boundaries this plan serves: [`Project-Boundaries.md`](Project-Boundaries.md).

## Measured starting point (Science — verified 2026-07-23)

- `src/`, `scripts/`, `tests/`, `packages/`, `corpus/` exist in **no
  branch of this repository's git history** (`git log --all -- src/` and
  equivalents return nothing).
- The code tree lived in the maintainer's working copy on a laptop; a
  dated snapshot sits in `archive/2026/local-snapshot-2026-07-17/`.

> **Assumptions re-baselined (2026-07-23, maintainer's report):** the
> laptop is gone — **no local working copy exists**. The maintainer
> works from an iPhone 16 Plus, reaching a DigitalOcean droplet over
> SSH (Termius). The canonical tree's current location is
> **unverified**; the droplet is the leading candidate (Stage 1.0
> below). The only git-verified code remains the `archive/` snapshots —
> which hold the earlier app era, **not** the post-reorg v1.0 protocol
> pack. **Nothing in this plan assumes a push from a local machine**:
> any host that has the canon tree and git access qualifies as the
> hand-off origin.
- Drift is provable from history alone: merged commit `1c1e473`'s message
  describes rewriting seven `packages/*/LICENSE.md` files; its diffstat
  contains none of them — the edits existed only on the local disk.
- Workflows: `ci.yml` and `deploy.yml` **fail** (they target the absent
  `src/` and `tests/`); `test-packages.yml` (path-gated on `packages/**`)
  and `publish-packages.yml` (tag-gated) are **dormant**. The root `CNAME`
  (`www.teraustralis.com.au`) points Pages at a site whose source
  (`src/site/`) is not in this repository.
- `TerAustralis-Incognita-Code` exists with one commit and a one-line
  README (its heading carried the double-a spelling ADR-0007 corrected).
- 75 files outside `archive/` reference the absent code paths; 9 of them
  now carry reality banners (the Stage-0 sync commit); the rest are
  cataloged in the appendix below.

## Stage 0 — docs tell the truth (this PR)

The sync commit (reality banners, `dbt/` on the map, the mythos blurb
fix) plus the boundary charter, this plan, and ADR-0011.
**Revert:** `git revert` of the two commits; nothing outside docs changed.

## Stage 1 — land the code into git

> **Stage 1 approved (2026-07-23).** Per this plan's per-stage gate, the
> maintainer (Crystal) selected, in-session: **option 1b** — import into
> `TerAustralis-Incognita-Code` with `core/` and `vision/` top-level
> areas; **hand-off by staging-branch push** (the maintainer pushes; the
> ignore rules keep personal data out); **engine-first scope** — PR 1
> imports `core/` only, `vision/` follows as PR 2, and the site /
> mythos-terminal placements are decided at PR 2. Directory names are
> preserved under the new area roots — no component renames. Options 1a
> and 1c below are retained for the record.
>
> **Amended (2026-07-23):** "from the local canon tree" is superseded —
> no local working copy survives the laptop's retirement. The hand-off
> happens **from whatever host Stage 1.0 identifies as holding the
> canon tree** (the DigitalOcean droplet is the leading candidate); the
> push-from-a-local-machine assumption is dropped entirely.

### Stage 1.0 — locate the canon tree (precedes the import)

Run on the droplet over Termius — one paste, searches the likely homes
and prints matches:

```bash
for d in ~ /root /home/* /opt /srv /var/www; do [ -d "$d" ] && find "$d" -maxdepth 5 -type d \( -iname "*teraustralis*" -o -iname "*teraaustralis*" -o -iname "crystal-core" -o -iname "crystalcore*" -o -iname "lumina" -o -name "consent_transport" \) 2>/dev/null; done | sort -u; echo ---; ls -la ~
```

Outcomes:

- **Found on the droplet** → the droplet is the canon host; the
  hand-off is a staging-branch push run there (`code-import-staging` on
  the `-Code` repo), and the import proceeds per the approved shape.
- **Not found** → recovery checklist, in order: laptop backups
  (Time Machine / iCloud / OneDrive folder sync), any other host or
  remote the tree was ever pushed to, the laptop itself if it
  physically survives.
- **Unrecoverable** → the v1.0 components (protocol pack, Consent
  Transport, RDP, the Weaver bridge) become **rebuild-from-spec** work
  against `docs/architecture/crystal-core/` — the specs are detailed
  enough to rebuild honestly — and this plan gets re-baselined by a new
  dated amendment; the `archive/` snapshots remain the only measured
  code.

**Precondition (amended):** the maintainer confirms the tree Stage 1.0
locates is the canon version to import; the push happens from that
host. Any machine with the tree and git access qualifies — a droplet
driven from a phone over SSH is fine.

| Option | What happens | For | Against |
|---|---|---|---|
| **1a** | Push `src/` (+ `scripts/`, `tests/`) into **this umbrella repo**, as its docs always described | Restores monorepo truth in one step; greens CI unchanged | Contradicts the charter: the umbrella holds no main app code; would be re-split later |
| **1b — recommended** | Import the code tree into **`TerAustralis-Incognita-Code`**, with top-level `core/` and `vision/` areas per the charter | Repo already exists; boundaries clean from day one; umbrella untouched and stays reversible; defers the repo-count question without blocking it | Cross-repo references (docs here, code there) need pointer updates; CI must be built there |
| **1c** | Create separate `crystal-core` and `crystal-vision` repositories now | Cleanest long-term shape | Requires new repos before Stage 3's criteria are even tested; most coordination, least reversible |

**Recommendation: 1b.** Decision belongs to the maintainer at stage
approval. Whatever the option: the import happens as ordinary reviewed
PRs; provenance is noted in commit messages (the tree's pre-git history
can't be grafted honestly — the snapshot in `archive/` remains the dated
record); the importing repo gets a `LICENSE` mirroring
[`ADR-0010`](../adr/ADR-0010.md)'s uniform CC BY-NC-ND 4.0 unless the
maintainer decides otherwise at import time; and every moved path drags
its references with it, verified by grep, per
[`Claude-Agent.md`](../agents/Claude-Agent.md).

## Stage 2 — workflows, Pages, CNAME

The only place workflow changes are proposed; none are made before it.

- **Umbrella:** retire or retarget `ci.yml` to docs-appropriate checks
  (link check, markdown lint). Remove the two dormant `packages/*`
  workflows (their PyPI names also carry the double-a spelling — verify
  nothing was ever published under `teraaustralis-*` before reserving
  corrected names). Move the Pages deploy and `CNAME` to wherever
  `src/site/` lands (Pages must live where the site's source lives).
- **Engineering repo(s):** stand up CI mirroring the old `ci.yml` checks
  against real paths (compileall, the four self-test suites, pytest).

## Stage 3 — repo-count decision point, and Lumina's framework

**Split `-Code` into `core` and `vision` repositories only when at least
one of these is true:** release cadences diverge; a licensing split
becomes real (revisiting ADR-0010); external contributors need scoping to
one side; or CI/product surfaces diverge enough to fight each other.
Until then: one repository, two top-level areas, the dependency rule
enforced in review.

**Lumina framework split — "strong reason" operationalized.** Extract the
CrystalCore Framework from Lumina into Crystal Core only when at least one
of: a second companion app needs the Framework; an external consumer
imports it; independent versioning/release pressure appears. Absent
these, Lumina stays whole in Crystal Vision, per the maintainer's
directive recorded in ADR-0011.

## Stage 4 — remaining placements

- **`dbt/crystalcore_emotion_warehouse/`** — recommendation: Crystal
  Core's data layer, eventually; acceptable to leave in the umbrella as a
  research artifact until the engineering repo is real.
- **Site (`src/site/`)** — recommendation: Crystal Vision (it is the
  public face); its Pages/CNAME mechanics are Stage 2's job.
- **`examples/`** — the index stays in the umbrella; runnable demos live
  with their code.

## Naming and spelling debts register

| Debt | Where | Constraint |
|---|---|---|
| ~~GitHub slug `TeraAustralis-Incognita` (double-a)~~ **Resolved** | This repo's URL | The slug ADR-0007 left unrenamed has since been corrected: the GitHub API returned `CrystalArchitect/TerAustralis-Incognita` (one 'a') when PR #48 was created, 2026-07-23. ADR-0007's "still-unrenamed" line stands as historical record only. |
| PyPI package names `teraaustralis-*` (double-a) | The dormant publish/test workflows | Verify nothing was ever published under them before reserving corrected names (Stage 2) |
| `corpus/` named as a surface of truth | Constitution §7 | Never built; fixing the row requires a §8 amendment. Proposed amendment text, supplied not applied: *"§7: mark the `corpus/` row as designed-but-not-built until an export pipeline exists, matching the 2026-07-21 implementation-note pattern."* |
| Deeper stale references in `mythos/README.md` (old `src/` links, the pre-monorepo "The Crystal Vision" framing) | `mythos/` | Vision-layer content — edit only with explicit maintainer sign-off (the Stage-0 blurb fix was the minimum honest correction) |

## Appendix — stale references deliberately not touched at Stage 0

75 files outside `archive/` reference the absent code paths; Stage 0
banner-fixed the 9 entry-point files. The rest, grouped, with the reason
and the stage that sweeps them:

| Group | Files (representative) | Why left at Stage 0 | Swept by |
|---|---|---|---|
| Workflows + PR template | `.github/workflows/*` (4), `.github/PULL_REQUEST_TEMPLATE.md` | Functional config, excluded from a docs-only change | Stage 2 |
| Historical record | `docs/adr/ADR-0001…0010`, `CHANGELOG.md` past entries | Never rewritten, per ADR-0007's pattern | Never (new entries supersede) |
| Superseded-era docs | `docs/PUBLISHING.md`, `docs/FIRST_RELEASE.md`, `docs/COMMERCIAL_LICENSING_GUIDE.md`, `docs/governance/LICENSING-*`, root `LICENSING.md` | Describe the reverted `packages/` era; already banner-marked or pointed at by ADR-0010 | Stage 2 (banner or retire) |
| Deep architecture/vision specs | `docs/architecture/Overview.md`, `CrystalCore.md`, `CrystalVision.md`, `AI-Weave.md`, `Lattice.md`, `Full-Stack-v0.5.md`, `crystal-core/*`, `docs/vision/*` | Component specs; their paths become true again wherever the code lands | Stage 1 (path sweep with the import) |
| Guides and process docs | `docs/guides/*`, `docs/governance/Review-Process.md`, `Development-Standards.md`, `Repository-Principles.md`, `docs/ai/GitHub.md`, `SECURITY.md`, `assets/README.md`, `dbt/**/README.md` | Reference commands/paths that move with the code | Stages 1–2 |
| Constitution §7 (`corpus/`) | `docs/governance/Constitution.md` | §8 amendment path only | When the maintainer chooses |
| Mythos content | `mythos/COVENANT.md`, content pages with `src/` pointers | Vision-layer area; owner sign-off required | Stage 1+, with sign-off |

## Reversibility

| Stage | Revert mechanism | Blast radius |
|---|---|---|
| 0 | `git revert` two docs commits | None beyond docs |
| 1 | Revert the import PR(s); `-Code` returns to its charter README | Engineering repo only; umbrella untouched |
| 2 | Restore workflows/CNAME from git history | CI/Pages behavior |
| 3 | Re-import while histories are short | Repo topology |
| 4 | `git mv` back within a repo | Paths only |
