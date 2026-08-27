# OPEN QUESTIONS

Live gates copied from disk. Canonical list:
[`docs/OPEN-DECISIONS.md`](../docs/OPEN-DECISIONS.md)
(last verified there: 2026-07-23, with a 2026-08-26 strike on two
Songline name candidates). Known unknowns also in
[`STATUS.md`](../STATUS.md).

**Label:** Vision unless marked Drift. None of these are blockers per the
source summary.

**Write-back:** when a gate closes, move the resolution to
[`DECISIONS.md`](DECISIONS.md) (with the ADR) and strike the row here.
Do not close a gate from chat.

## Held open (from OPEN-DECISIONS)

| Gate | What is actually open | Label |
|---|---|---|
| Stage 3: split `-Code` into core / vision repos | Only if release cadences, licensing, external scope, or CI/product surfaces actually fight. ADR-0015 still applies. | Vision |
| Stage 3: extract CrystalCore Framework from Clementine | Only if a second app, an external consumer, or independent versioning pressure appears. Clementine stays whole for now (ADR-0011). | Vision |
| Stage 3: frozen provenance repos' end state | GitHub-archive / leave as-is / external cold storage. Maintainer click, not an agent action. | Vision |
| Stage 4: site content sync | Placement of site source in `-Code` `vision/site/` is done. Sync of umbrella `mythos/` → site content is still **manual**. CI automation is a later option. | Vision |
| Stage 4: dbt emotion warehouse | Lives in this umbrella. No warehouse configured. STATUS: not executed. OPEN-DECISIONS: staging models hardcoded null CTEs; SQL syntax error in `stg_emotion_labels.sql` (as of 2026-07-24). Wire to JSONL or retire. | Vision |
| Tier 2: `crystalcore` / `crystal-core` / `runtime` | Three systems share vocabulary but not code. Intentionally separate, or integrate? Decision needed. Paths describe the **code** tree, not this git. | Vision |
| Tier 2: Starline taxonomy | Three meanings, no ADR yet. See below. | Vision |
| Tier 2: 0.7.0 vs 0.13.4 fork | Clementine Framework forked 0.7.0; 0.13.4 extras unreconciled in frozen `The-Crystal-Vision`. | Vision |
| Tier 3: archive recovery contradiction | `archive/2026/local-snapshot-2026-07-17/README-SNAPSHOT.md` vs sibling `crystalcore-v0.13/RECOVERY-STATUS.md` disagree on `status.py` and SpaceXAI provider. Fuller treatment, incl. why this is more a generational-supersession framing gap than a hard factual conflict: [`evidence/CONFLICTS.md`](evidence/CONFLICTS.md). | Drift |

## Starline — three meanings (no taxonomy ADR)

From OPEN-DECISIONS:

| Meaning | What it is on disk |
|---|---|
| A | Real P2P transport (`consent_transport`, Noise protocol) |
| B | Multi-agent message bus ("Starline Weaver") |
| C | Fictional game state machine (mythos terminal, `crystalcore_os.py`) |

Recommendation on disk: disambiguate the way ADR-0004 disambiguated
"CrystalCore" — write a taxonomy ADR, lock the meanings.

**Struck 2026-08-26** (do not revive): "SonglineTransport" (A) and
"Songline Network" (C). Songline is never a component name
([`Indigenous-Data-Sovereignty.md`](../docs/governance/Indigenous-Data-Sovereignty.md),
[`mythos/NAMES.md`](../mythos/NAMES.md)). Replacement names are left to
the maintainer.

## ADRs still Proposed

| ADR | Why it is not law |
|---|---|
| [ADR-0012](../docs/adr/ADR-0012.md) | Site token layer / deferred restructure. Status: Proposed. |
| [ADR-0016](../docs/adr/ADR-0016.md) | SourceCode as external peer. Status: Proposed; becomes Accepted on merge of its PR. |

## STATUS known unknowns (measured or still open)

- This umbrella's Pages job deploys nothing, by design. The public site
  is published from `TerAustralis-Incognita-Code`. **Re-measured 2026-08-20:**
  apex `teraustralis.com.au` GitHub Pages **301** →
  `https://www.teraustralis.com.au/` **200** (SvelteKit). A single
  link-check 404 during a Pages swap is not evidence the site is gone.
- `examples/README.md` commands still target `src/` paths that moved;
  the index awaits re-pointing.
- `teraustralis-final.html` — six-repo search found zero copies
  (corrected 2026-07-24).
- `publish-packages.yml` / `test-packages.yml` were **removed** at
  Stage 2 (not "dormant by drift").

## Designed, not built (from STATUS / Roadmap / Constitution)

- Lattice-delta / Weave-Map / G0–G5 gate board
- `corpus/` (Constitution §7)
- Story Library production components (HTML prototype exists)
- mythos/tools prompt-kit workflows (daily-digest, signal-scanner) — written, wired to nothing
- CrystalCore OS platform v0.3 Engine layer and v0.4 Living Archive
- Real P2P mesh (`src/node/mesh/` stub), multi-instance Clementine, Phase 2 private communication
- TypeScript SDK — scaffold, no consumer

These stay **Unknown** or **Vision** until surveyed ground exists.
