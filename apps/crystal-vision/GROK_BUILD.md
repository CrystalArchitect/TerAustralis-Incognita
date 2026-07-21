# Grok Build — Crystal Interface / Crystal Vision

**Sync phrase:** Sync Crystal Vision from `GROK_BUILD.md` and `BUILD_MANIFEST.json` — bump version, update CHANGELOG, redeploy Vercel full UI.

## What this tree is

Operator-facing demo shell (and Vision-linked brand surface):

| File | Role |
|------|------|
| `index.html` | Panels, wallet modal, nav |
| `app.js` | Mesh, pipeline, receipts, econ, init |
| `styles.css` | Obsidian / cyan / gold theme |
| `README.md` | Local open instructions |
| `BUILD_MANIFEST.json` | Version + deploy URLs |
| `GROK_BUILD.md` | This handoff |
| `CHANGELOG.md` | Ship notes |
| `vercel.json` | Static SPA rewrite |

**Authority: HOLD.** Not production. Not mainnet.

## Local serve

```powershell
cd apps/crystal-vision
python -m http.server 8090
# http://127.0.0.1:8090
```

Citizen shell (sibling): `../vision-web/`

## After each Grok Build session

1. Bump `version` in `BUILD_MANIFEST.json`
2. Append `CHANGELOG.md`
3. Ensure all 8 files are present
4. Push to GitHub `CrystalArchitect/crystal-vision`
5. Redeploy Vercel project `crystal-vision` (full UI, not single-file)

## Linked services (2026-07-17)

- **GitHub:** https://github.com/CrystalArchitect/crystal-vision (deploy tree on `main` — 8 files; repo is no longer empty after push; resync all 8 after each Build)
- **Vercel preview:** https://crystal-vision-ter-australis-incognita.vercel.app (redeploy full UI after each sync)

### Redeploy command for Grok

> Deploy all files in `crystal-vision/` to Vercel project `crystal-vision` (preview).
