# Roadmap

A plain status page, not a pitch deck. It tracks the **Built** layer — see
[README.md](README.md#whats-real-vs-whats-vision) for the Built vs. Vision
split. Vision-layer work (the mythos) doesn't move on a software roadmap; see
[CONSTITUTION.md](CONSTITUTION.md) for how that content evolves instead.

For Clementine specifically, [mythos/content/MILESTONES.md](mythos/content/MILESTONES.md)
already tracks a detailed week-by-week build plan — this page doesn't repeat
that detail, it points to it.

## Built and working today

- **Clementine** (`apps/clementine/`) — local-first AI companion, Ollama-backed.
  Terminal, Flask API, Svelte webapp, browser voice. Run it: `cd apps/clementine
  && python3 clementine.py`.
- **The Songline Bus** (`crystal-core/clementine/bridge/`) — multi-AI message
  bus with the Belt-Three law enforced in code, not just convention. Self-test:
  `python3 -m clementine.bridge.selftest`.
- **Starline** (`crystal-core/starline/`) — peer-to-peer consent-gated memory
  exchange over a real Noise Protocol handshake. Self-test: `python3 -m
  starline.selftest`; watch it work: `python3 -m starline.run demo`.
- **CrystalBridge** (`crystalcore/`) — the MCP consent gate. Fail-closed by
  design: every guest-AI call passes approval, permission, scope, and
  provenance checks, with append-only audit logging.

All four have tests you can run yourself — see the Quick Start in
[README.md](README.md#quick-start).

## Demo shells (simulated data, not production)

`apps/crystal-vision/`, `apps/crystal-interface/`, and `apps/vision-web/` run,
but on simulated data with Authority held. They're interface concepts, not
production surfaces, and aren't on a path to becoming one without a separate
decision to build the real data layer underneath them.

## In progress

- **Clementine's reliability and control layer** (MILESTONES.md Month 4) —
  error recovery, full memory export, selective memory deletion, and a
  settings/config file are partially built; hallucination-reduction /
  fact-check-against-memory hasn't started yet.
- **`crystal-core/spec/BLUEPRINT-v0.3.md`** — the protocol pack's architecture
  spec is a live draft, not a frozen v1.

## Not yet started

- **Real P2P transport for the mesh** (`node/mesh/`) — currently an in-process
  stub with the API shape a future libp2p host would need. gossipsub, Noise,
  yamux, and bootstrap/mDNS discovery are all planned but not built; a mainnet
  mesh is explicitly on hold. See `node/mesh/README.md`'s own status table.
- **Multi-instance Clementine** — two companions communicating with each
  other. Design thinking hasn't started (MILESTONES.md Week 19).
- **Phase 2 ("Private Communication")** — named as a future phase in
  MILESTONES.md, shape not yet decided.
- **TypeScript client SDK** (`sdk/typescript/`) — package scaffold exists; no
  consumer wired up against it yet.

## Recently landed

Dated so this section ages honestly — newest first, and it's fine to trim
older entries once they're no longer useful context; the full history is
always in `git log`.

- **2026-07-21** — Implemented CrystalBridge's missing `config.py` and
  `bridge.py` — the consent gate was undocumented and partially broken before.
- **2026-07-21** — Fixed the Codex, Apocryphon, and Clementine site pages,
  which were silently missing from every deploy.
- **2026-07-21** — Added the homepage "What's Built, What's Vision" section and
  fixed several documentation-accuracy bugs (wrong paths, wrong filenames,
  overstated claims).

## Related documents

- [CONTRIBUTING.md](CONTRIBUTING.md) — how to propose changes, the Belt-Three
  truth labels, licensing.
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — expected behavior and how to report
  a problem.
- [SECURITY.md](SECURITY.md) — this repo's safety measures and how to report
  a vulnerability.
- [mythos/content/MILESTONES.md](mythos/content/MILESTONES.md) — Clementine's
  detailed weekly build plan.
- `crystal-core/spec/` — architecture and protocol specs for the Songline Bus
  and Starline.

*Non Solus.*
