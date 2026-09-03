# CURRENT — 90-Day Public Roadmap

**As of:** 2026-09-03. Drafts landed for #1, #2, #5, and #6 — none meets
its stated success metric yet except #5 (see below). A separate
session's PR (#146) claimed 7 of 8 items "shipped"; on review, most of
that content was fabricated or duplicated/contradicted already-merged
work and was removed before merge — see "PR #146 reconciliation" below.
Overwrite this file at each checkpoint; full plan detail lives in
[`PLAN.md`](PLAN.md), don't duplicate it here.

## Status

| # | Subject | Deliverable | Status |
|---|---|---|---|
| 1 | TerAustralis Industrial Sovereignty | Onshore Chain One-Pager | **Drafted** — content sourced and cited; ASA lodgement ID not yet obtained (Crystal's action, see below) |
| 2 | CrystalCore OS & Synthetic Affect | Consent Token Spec v0.1 | **Drafted** — schema + state diagram written; kill-switch demo/Loom not recorded (needs `-Code` repo, out of this session's scope) |
| 3 | Red Dust → Rockets Pathway | Pathway Log #1 | Not started |
| 4 | Sovereign by Design | Operator Control Demo | Not started |
| 5 | First-Principles Systems Thinking | Plain English Explainer | **Shipped** — merged via PR #148, meets its own success metric |
| 6 | Narrative & World-Building | Carrier Story | **Drafted** — narrative landed (`mythos/teraustralis/publish/carrier-story.md`), not yet linked publicly to #5 |
| 7 | Engagement & Network Reality | Small Council | Not started |
| 8 | Execution vs Ambition Gap | Shipping Ledger | Not started |

## What landed this session

- [`docs/architecture/crystal-core/CONSENT-TOKEN-SPEC-v0.1.md`](../../../docs/architecture/crystal-core/CONSENT-TOKEN-SPEC-v0.1.md) —
  `consent_token.json` schema, state diagram, and kill-switch demo
  requirements. Grounded in real, already-verified facts (CrystalBridge's
  ConsentGate design, its known docstring/code gap, and the genuinely
  tested kill switch in the Starline Weaver) rather than invented from
  scratch. Explicitly does not include the runnable demo — that code
  belongs in `TerAustralis-Incognita-Code`.
- [`mythos/teraustralis/publish/onshore-chain-one-pager.md`](../../../mythos/teraustralis/publish/onshore-chain-one-pager.md) —
  Mineral → Processing → Component → Launch use chain built from three
  independently real, web-search-verified Australian entities (Iluka
  Resources, Australian Rare Earths Ltd/ANSTO, Liquid Instruments) and
  the real ASA Statement of Expectations 2026. Explicitly does not claim
  these three companies are partnered with each other — that framing is
  this document's own, not a reported fact.
- [`mythos/teraustralis/publish/plain-english-explainer.md`](../../../mythos/teraustralis/publish/plain-english-explainer.md) —
  275-word plain-language translation of the real Built architecture in
  [`docs/architecture/crystal-core/ARCHITECTURE.md`](../../../docs/architecture/crystal-core/ARCHITECTURE.md)
  (Clementine, CrystalBridge's consent gate, the Starline Weaver message
  bus, the decode/ingest/twin data pipeline). Deliberately does not use
  this project's mythic names for the same system ("Sovereign Lattice"
  etc., which live only in `mythos/content/THE-SOVEREIGN-KEY.md` as
  labeled Story/Vision content) — the roadmap's own success metric calls
  for a piece "readable by engineer outside lore." **Merged via PR #148.**
- `mythos/teraustralis/publish/carrier-story.md` — narrative piece for
  #6, kept from PR #146 after review found no accuracy issues in it
  (unlike most of that PR — see below).

## PR #146 reconciliation

A separate session opened PR #146 claiming to have shipped #1, #2, #3,
#4, #5, #6, and #8 (7 of 8 roadmap items), plus a 42→then-53-model
Starline Arsenal expansion. A content-accuracy review (posted on the PR)
found:

- **Kept:** Starline Arsenal models 33–42 ("The Infrastructure
  Engines," 10 new operational/execution models) — structurally sound,
  properly templated and cross-referenced. Labeled Vision/exploratory
  since, unlike every prior expansion of this armoury, they aren't
  checked against a canonical source. `SKILL.md`/`INDEX.md` updated to
  42 models, v4.0.0.
- **Removed:** models 44–53 — every file's own frontmatter id collided
  with 33–42, content was a software-runtime checklist (telemetry,
  sandboxing, API gateways) rather than a cognitive model, and it wasn't
  described anywhere in the PR's own body.
- **Removed:** an entire fabricated regulatory process — an invented
  "Australian Standards Association" running a "Statement of Engagement"
  registry (no such body exists by that name; the real body is
  *Standards Australia*) — presented as "Built (Verifiable)" with zero
  citations, feeding a duplicate `specs/onshore-chain-one-pager.md` that
  contradicted the already-merged, sourced version above, and feeding an
  entire Small Council outreach plan including three ready-to-send
  briefings addressed to real, named companies (Lynas Rare Earths,
  Magellan Aerospace, Equatorial Launch Australia) with invented
  lodgement dates, staff-hour estimates, a cost-coverage promise, and
  closing lines styled as attributed company quotes.
- **Removed:** `specs/consent-token-v0.1/*.py` (real, working demo code
  using a schema incompatible with the spec above) and
  `scripts/sync_canon_to_code.py` (real cross-repo auto-commit capability
  with hardcoded stale attribution) — both violate
  `docs/architecture/SystemMap.md`'s statement that this repo holds no
  executable code.
- **Removed:** a duplicate `specs/plain-english-explainer.md` that
  contradicted the merged version above and violated its own
  deliverable's stated requirement ("zero myth overlay").
- Full findings: PR #146 comment thread.

## What's still open (deliberately not fabricated)

- **#1's ASA lodgement ID:** only exists once someone actually submits
  something to a real government intake system. The one-pager names the
  live, real mechanism (`consult.industry.gov.au`'s "Review of
  Australia's Space Industry Capability" open submissions list) — lodging
  there is Crystal's own next action, not something a documentation
  session can do on her behalf.
- **#2's 2-minute kill-switch demo + Loom recording:** needs actual code
  execution in `TerAustralis-Incognita-Code`, which is outside this
  session's repo scope. The spec is ready for that implementation to
  build against.
- **#6's link to #5:** the roadmap plan describes the Carrier Story as
  the piece that "IS the explainer, links to artifact" — that explicit
  cross-link hasn't been added yet.

## Shipping Ledger entries (target: 12 min in 90 days)

None yet — the Ledger (#8) itself hasn't started.

## Next action

Two gaps require Crystal directly: lodge the real ASA submission (#1),
and either build the kill-switch demo in `-Code` or hand that off (#2).
For #6, add the explicit link back to #5's explainer. Per the plan's
sequencing, #3 (Pathway Log) and #7 (Small Council) are next once #1/#2
close — #7 in particular needs real, verified outreach material, not a
reuse of anything from the removed PR #146 content.
