# CURRENT — 90-Day Public Roadmap

**As of:** 2026-09-03. Drafts landed for #1 and #2 — neither meets its
stated success metric yet (see below). Overwrite this file at each
checkpoint; full plan detail lives in [`PLAN.md`](PLAN.md), don't
duplicate it here.

## Status

| # | Subject | Deliverable | Status |
|---|---|---|---|
| 1 | TerAustralis Industrial Sovereignty | Onshore Chain One-Pager | **Drafted** — content sourced and cited; ASA lodgement ID not yet obtained (Crystal's action, see below) |
| 2 | CrystalCore OS & Synthetic Affect | Consent Token Spec v0.1 | **Drafted** — schema + state diagram written; kill-switch demo/Loom not recorded (needs `-Code` repo, out of this session's scope) |
| 3 | Red Dust → Rockets Pathway | Pathway Log #1 | Not started |
| 4 | Sovereign by Design | Operator Control Demo | Not started |
| 5 | First-Principles Systems Thinking | Plain English Explainer | Not started |
| 6 | Narrative & World-Building | Carrier Story | Not started |
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

## Shipping Ledger entries (target: 12 min in 90 days)

None yet — the Ledger (#8) itself hasn't started; these two drafts don't
count as Ledger entries on their own per the plan's own distinction
between "shipped" (meets its success metric) and "drafted."

## Next action

Both remaining gaps require Crystal directly: lodge the real ASA
submission (#1), and either build the kill-switch demo in `-Code` or
hand that off (#2). After those two close, per the plan's own
sequencing, move to weeks 3-6: Plain English Explainer (#5) and Carrier
Story (#6).
