# Crystal Vision · Citizen Shell

User-facing demo surface for the Crystal stack.

| Surface | Audience |
|---------|----------|
| **This app** (`apps/vision-web`) | Citizens / end users |
| `apps/crystal-interface` | Operators / builders |
| TerAustralis + Starline | Investor / pilot narrative |

**Not production.** Credits, capabilities, and receipts are client-side demo only. Authority **HOLD**. Cultural metaphors (Seven Sisters / Songline) are collaborative framing only — not ownership claims.

## Open

```powershell
cd apps/vision-web
# from monorepo apps/ so cross-links work:
cd ..
python -m http.server 8090
# → http://127.0.0.1:8090/vision-web/
# → http://127.0.0.1:8090/crystal-interface/
```

## Panels

- **Home** — product map + citizen journey
- **My twin** — personal layer canvas (water / energy / mobility)
- **Consume** — capability grant + spend → receipt
- **Receipts** — local demo table
- **Privacy** — export / erase request stubs (GDPR path)

## Related

- Journeys: `docs/journeys/README.md`
- GDPR: `compliance/GDPR_ROPA.md`
- Operator UI: `apps/crystal-interface/`
- Mesh stub: `node/mesh/`
- Roadmap: `docs/FULL-STACK-v0.5.md`
