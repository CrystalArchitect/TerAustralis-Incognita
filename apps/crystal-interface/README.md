# Crystal Core · Interactive Interface

Local **demo shell** for Crystal Vision / Core / Starline Budapest.

**Not production.** Economics are illustrative. Authority **HOLD**.

## Open

```powershell
cd C:\Users\cryst\.grok\downloads\TeraAustralis-Incognita\apps\crystal-interface
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

## Related backend

```powershell
python -m services.pipeline_demo
python -m node.agent.server --port 8787
```
