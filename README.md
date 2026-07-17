# TerAustralis Incognita · Crystal Core — Full Stack

**Tagline:** Collective intelligence with individual sovereignty.  
**Mainnet / deploy:** **PROHIBITED** until audit. Economic modules are design + simulation only.

**🔭 Crystal universe — which repo is this?**  
This is **TerAustralis Incognita** — narrative + full-stack monorepo + CrystalBridge MCP consent gate.  
Siblings: **crystalcore** = Crystal Core (protocol pack) · **the-crystal-vision** = The Crystal Vision (codex site + Clementine sovereign companion app) · **crystal-vision** = Crystal Vision Interface (static demo shell).  
**License:** Code Apache-2.0 (`LICENSE`) · Content CC BY-NC-ND 4.0 (`LICENSE-CONTENT.md`)

```
TerAustralis Incognita  →  frontier
Crystal Vision          →  lens
CrystalCore             →  reactor
Clementine              →  local core mind
CrystalBridge           →  consent meeting-house (MCP)
```

## Monorepo map

| Path | Role | Status |
|------|------|--------|
| `docs/` | Architecture, universe brand, exec summary, images | ✅ |
| `spec/` | ARCHITECTURE + RFCs + fixtures | ✅ draft |
| `sim/` | Burn-mint Monte Carlo (5 scenarios) | ✅ |
| `packages/crypto` | DID + sign helpers | ✅ scaffold |
| `packages/receipts` | Receipt validate + hash | ✅ |
| `services/decode` | DECODE raw → twin candidate | ✅ v0.2 |
| `services/ingest` | INGEST policy → twin store | ✅ v0.2 |
| `services/receipt_engine` | Twin → ServiceReceipt | ✅ v0.2 |
| `services/upgrade` | Evidence → HOLD/LOCAL_READY report | ✅ v0.2 |
| `hubs/starline_budapest` | Reference physical hub | ✅ template |
| `node/agent` | HTTP node: identity, receipts, CRDT, twin | ✅ MVP |
| `node/mesh` | libp2p-shaped mesh stub (in-process) | ✅ v0.5 |
| `apps/crystal-interface` | Operator demo UI (twin/mesh/pipeline/econ) | ✅ |
| `apps/vision-web` | Citizen Vision shell (credits/capability) | ✅ v0.5 |
| `sdk/typescript` | TS client for local agent | ✅ v0.5 |
| `docs/FULL-STACK-v0.5.md` | Surfaces + mesh roadmap | ✅ |
| `twin/` | Energy kWh layered control POC | ✅ |
| `contracts/` | ReceiptAnchor.sol | ⬜ no deploy |
| `crystalcore/` | CrystalBridge MCP consent gate | ✅ tested |
| `Clementine/` | Core identity + Ollama Modelfile | ✅ |
| `CrystalVision/` | Visual suite | ✅ |
| `TeraAustralis/` | Lore + publish | ✅ |
| `profiles/` | Bridge gate config | ✅ |
| `security/` | Threat model Z0–Z4 | ✅ v0.3 |
| `compliance/` | GDPR outline, licensing checklist | ✅ draft |
| `integrations/` | Energy/mobility adapters → decode | ✅ scaffold |
| `deploy/` | Helm region chart + Budapest charter | ✅ scaffold |
| `courts/` | Dispute docket templates | ✅ |
| `docs/FULL-STACK-v0.3.md` | Operable company skeleton | ✅ |

## Quick start (full stack v0.5)

```powershell
cd C:\Users\cryst\.grok\downloads\TeraAustralis-Incognita
$env:PYTHONPATH = (Get-Location).Path

# Decode → Ingest → Twin → Receipt → Upgrade (Starline Budapest sample)
python -m services.pipeline_demo

# All tests + sim + demo
.\scripts\run-full-stack.ps1

# Node agent (HTTP)
python -m node.agent.server --port 8787

# Demo UIs (Vision + Core)
cd apps
python -m http.server 8090
# Vision:  http://127.0.0.1:8090/vision-web/
# Core UI: http://127.0.0.1:8090/crystal-interface/

# Happy paths over HTTP
curl -X POST http://127.0.0.1:8787/demo/pipeline -H "Content-Type: application/json" -d "{}"
curl -X POST http://127.0.0.1:8787/demo/flow -H "Content-Type: application/json" -d "{}"
curl http://127.0.0.1:8787/layers
curl http://127.0.0.1:8787/health
```

**Pipeline doc:** [`docs/pipelines/DECODE-INGEST-UPGRADE.md`](docs/pipelines/DECODE-INGEST-UPGRADE.md)

### Clementine + Bridge

```powershell
ollama run clementine
.\scripts\run-bridge.ps1 -Guest grok
python -m pytest tests -q
```

### Token simulation

```powershell
python sim/model_cadcad.py --all
# reports: sim/outputs/full_report.md
```

## Architecture phases

| Phase | Scope |
|-------|--------|
| 0 | Spec, sim, RFCs — **here** |
| 1 | Mesh MVP (local node agent + CRDT) — **scaffold live** |
| 2 | Twin & metering (energy POC) — **scaffold live** |
| 3 | On-chain economics — **contracts stub only** |
| 4 | HSM, formal verify, audit — **not started** |

## Key docs

- [`docs/FULL-STACK-v0.3.md`](docs/FULL-STACK-v0.3.md) — gap fill (security, payments, journeys, SRE)  
- [`docs/pipelines/DECODE-INGEST-UPGRADE.md`](docs/pipelines/DECODE-INGEST-UPGRADE.md)  
- [`docs/CRYSTAL-CORE-ARCHITECTURE.md`](docs/CRYSTAL-CORE-ARCHITECTURE.md)  
- [`docs/CRYSTAL-UNIVERSE.md`](docs/CRYSTAL-UNIVERSE.md)  
- [`docs/EXEC-SUMMARY.md`](docs/EXEC-SUMMARY.md)  
- [`docs/CULTURAL_PROTOCOL.md`](docs/CULTURAL_PROTOCOL.md)  
- [`security/THREAT_MODEL.md`](security/THREAT_MODEL.md)  
- [`spec/rfc/RFC-001-identity-receipts.md`](spec/rfc/RFC-001-identity-receipts.md)  
- [`spec/rfc/RFC-003-federation-dispute.md`](spec/rfc/RFC-003-federation-dispute.md)  
- [`deploy/regions/budapest-starline/charter.yaml`](deploy/regions/budapest-starline/charter.yaml)  
- [`docs/CRYSTALBRIDGE.md`](docs/CRYSTALBRIDGE.md)  
- [`docs/ACCESS.md`](docs/ACCESS.md)  

```text
make test | make sim | make pipeline | make agent
```  

## Diagrams

- `docs/images/four-layers.jpg`  
- `docs/images/token-flow.jpg`  
- `docs/images/sovereign-mesh.jpg`  

## 90-day milestone

Mesh MVP + twin POC + token simulation **in repo** · **no mainnet until audit**.

## License

**Code**: Apache-2.0 — see `LICENSE`. Token/mainnet rights not granted by default.

**Content** (TerAustralis lore, CrystalVision suite, universe/brand docs, imagery):
[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) — see
`LICENSE-CONTENT.md`. Share with credit; no commercial use, no derivatives.
