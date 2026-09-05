# CURRENT — TerAustralis-Incognita-Code state snapshot

**As of:** 2026-09-05  
**Source:** Umbrella memory active; cross-repo sessions

## What's running (production)

- **Public site (www.teraustralis.com.au):** SvelteKit frontend serving mythos content to live domain. Status: 200 OK. GitHub Pages → Domain apex 301 → www.
- **Clementine:** Companion AI (local-first, Ollama-backed). Code here; memory architecture in umbrella `mythos/content/MEMORY.md`.
- **Starline Weaver:** Decision interface. Code here; specs in umbrella docs/architecture/.
- **RDP kernel:** Record/Decide/Persist core. Documented in umbrella architecture.
- **Vision Framework Site:** Small Council Phase 2 integration. ObservatoryMap navigation, TunnelingMonitor interactive component (Svelte 5.1.0), theme-aware CSS. Merged PR #134.

## What's Built, not currently exercised

- CrystalBridge (consensus layer)
- Supporting infrastructure (tests, CI)

## What's not built yet

- Full Lattice runtime (designed, not implemented)
- Emotion Warehouse integration (dbt models exist, no warehouse configured)

## Open blockers

See umbrella [`../../OPEN-QUESTIONS.md`](../../OPEN-QUESTIONS.md). Repo-specific blockers TBD.

## Next steps for sessions

Add repo-specific DECISIONS.md, PLAN.md, OPEN-QUESTIONS.md as needed when working on substantial tasks.
