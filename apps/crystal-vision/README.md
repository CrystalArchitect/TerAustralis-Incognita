# Crystal Vision — the operator shell

The operator-facing **demo shell** for Crystal Vision / Core / Starline Budapest,
and the Vercel deploy package (`vercel.json`, `BUILD_MANIFEST.json`). This is the
single canonical copy — a byte-identical duplicate (`crystal-interface`) used to
live beside it and has been removed. The citizen-facing surface is the separate,
slimmer [`../vision-web`](../vision-web).

**🔭 Crystal universe — which repo is this?**  
Siblings: **crystalcore** = Crystal Core (protocol pack) · **the-crystal-vision** = The Crystal Vision (codex site + Lumina sovereign companion app) · **teraaustralis-incognita** = TeraAustralis Incognita (narrative + CrystalBridge).  
**License:** Apache-2.0 — see `LICENSE`

**Not production.** Every number is illustrative and **simulated in the browser**;
this shell makes **no backend calls**. Authority **HOLD**.

## Open

```bash
cd apps/crystal-vision
# any static server, or:
python -m http.server 8090
# → http://127.0.0.1:8090
```

Or open `index.html` directly in a browser.

## Panels

| Panel | Content |
|-------|---------|
| Home | Product map + stats |
| Twin | Layered canvas (water / energy / data / mobility) |
| Mesh | Sovereign nodes SVG |
| Pipeline | DECODE→…→UPGRADE interactive steps |
| Economics | Burn rate R, α, wallet demo |
| Starline | Corridor cards VIE/BTS/BER |
| Wallet | Citizen journey |
| Event log | Client-side activity |

## The real pipeline (separate — not wired to this shell)

This shell is static and simulated; it does not call a backend. The actual data
pipeline is a real, tested package in the monorepo and runs independently:

```bash
cd ../../crystal-core
python -m services.selftest      # the real ingest → decode → twin pipeline, with tests
```
