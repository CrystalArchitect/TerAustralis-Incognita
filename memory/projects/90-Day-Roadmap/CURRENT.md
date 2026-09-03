# CURRENT — 90-Day Public Roadmap

**As of:** 2026-09-03. Drafts landed for #1, #2, and #5 — none meets its
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
| 5 | First-Principles Systems Thinking | Plain English Explainer | **Drafted** — 275 words, sourced from the real Built architecture doc, no mythic naming; not yet posted publicly |
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
- [`mythos/teraustralis/publish/plain-english-explainer.md`](../../../mythos/teraustralis/publish/plain-english-explainer.md) —
  275-word plain-language translation of the real Built architecture in
  [`docs/architecture/crystal-core/ARCHITECTURE.md`](../../../docs/architecture/crystal-core/ARCHITECTURE.md)
  (Clementine, CrystalBridge's consent gate, the Starline Weaver message
  bus, the decode/ingest/twin data pipeline). Deliberately does not use
  this project's mythic names for the same system ("Sovereign Lattice"
  etc., which live only in `mythos/content/THE-SOVEREIGN-KEY.md` as
  labeled Story/Vision content) — the roadmap's own success metric calls
  for a piece "readable by engineer outside lore."

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

Two gaps require Crystal directly: lodge the real ASA submission (#1),
and either build the kill-switch demo in `-Code` or hand that off (#2).
#5's own success metric ("readable by an engineer outside lore") is met
by the draft itself — publishing it is the only remaining step, and
that's Crystal's own distribution choice, not a drafting task. Per the
plan's own sequencing, #6 (Carrier Story) is next: it's meant to link to
#5 as its technical anchor.
