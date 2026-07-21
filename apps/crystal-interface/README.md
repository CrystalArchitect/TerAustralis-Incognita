# Crystal Core · Interactive Interface

Local **demo shell** for Crystal Vision / Core / Starline Budapest — the
operator-facing surface.

**Not production.** Every number here is illustrative and client-side: the twin,
mesh, pipeline, economics, receipts and wallet are all **simulated in the
browser**. This shell makes **no backend calls at all**. Authority **HOLD**.

### The three shells, and how they relate

There are three static demo shells in `apps/`, and it's easy to confuse them:

| Shell | Audience | Status |
|-------|----------|--------|
| **`crystal-interface`** (this one) | Operators / builders | **Canonical source** of the operator shell |
| `crystal-vision` | — | A **byte-identical deploy snapshot** of this shell + Vercel packaging. Do not edit it by hand; it mirrors this dir. |
| `vision-web` | Citizens / end users | A **separate, slimmer** citizen surface — not a copy of this one |

## Open

```bash
cd apps/crystal-interface
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

This shell is a static, simulated demo; it does not talk to a backend. The actual
data pipeline is a real, tested package that lives elsewhere in the monorepo and
runs **independently**:

```bash
cd ../../crystal-core
python -m services.selftest      # the real ingest → decode → twin pipeline, with tests
```

Wiring this shell to `crystal-core/services/` is future work, not a current
feature — so treat the panels here as an illustration of *what* the pipeline
produces, not a live view of it.
