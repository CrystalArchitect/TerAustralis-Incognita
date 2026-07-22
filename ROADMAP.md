# Roadmap

A plain status page, not a pitch deck. It tracks the **Built** layer — see
[README.md](README.md#whats-real-vs-whats-vision) for the Built vs. Vision
split. Vision-layer work (the mythos) doesn't move on a software roadmap; see
[CONSTITUTION.md](CONSTITUTION.md) for how that content evolves instead.

For Lumina specifically, [mythos/content/MILESTONES.md](mythos/content/MILESTONES.md)
already tracks a detailed week-by-week build plan — this page doesn't repeat
that detail, it points to it.

## Built and working today

- **Lumina** (`apps/lumina/`) — local-first AI companion, Ollama-backed.
  Terminal, Flask API, Svelte webapp, browser voice. Run it: `cd apps/lumina
  && python3 lumina.py`.
- **The Starline Weaver** (`crystal-core/clementine/bridge/`) — multi-AI message
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

`apps/crystal-interface/` and `apps/vision-web/` run,
but on simulated data with Authority held. They're interface concepts, not
production surfaces, and aren't on a path to becoming one without a separate
decision to build the real data layer underneath them.

## In progress

- **Lumina's reliability and control layer** (MILESTONES.md Month 4) —
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
- **Multi-instance Lumina** — two companions communicating with each
  other. Design thinking hasn't started (MILESTONES.md Week 19).
- **Phase 2 ("Private Communication")** — named as a future phase in
  MILESTONES.md, shape not yet decided.
- **TypeScript client SDK** (`sdk/typescript/`) — package scaffold exists; no
  consumer wired up against it yet.

## Recently landed

Dated so this section ages honestly — newest first, and it's fine to trim
older entries once they're no longer useful context; the full history is
always in `git log`.

- **2026-07-22** — Wired the Starline Weaver's matrix mode to RDP:
  `record_matrix_result()` (`crystal-core/rdp/adapters.py`) witnesses a matrix
  run's responses and cross-compare onto the tamper-evident chain, same
  one-way rule as the ConsentGate adapter — the Weaver decides, RDP only
  records. `python3 -m rdp.run matrix-demo` drives the real Weaver through the
  real chain. 1 new self-test, 31/31 passing.
- **2026-07-22** — Added matrix mode to the Starline Weaver
  (`crystal-core/clementine/bridge/`): `run_matrix()` fans one question out
  to every agent independently (none sees another's reply) and
  `cross_compare()` counts delivery and truth-label agreement — a count, not
  a verdict. `--mode matrix` on the existing CLI. 4 new self-tests, 7/7
  passing.
- **2026-07-22** — Fixed `CODEX.md`'s dead `assets/codex-cover.jpeg` link (the
  `assets/` folder didn't exist) and added a matching cover to
  `APOCRYPHON.md`, which had none. Both AI-generated with Grok on X.
- **2026-07-22** — Added the first four rendered stills from the boot-visual
  prompt (`mythos/art/lattice-ignition-wide.jpeg` and three others,
  AI-generated with Grok on X) to the art gallery. A full video hasn't been
  made yet.
- **2026-07-21** — Added a Vision-layer video-generation prompt for the
  CrystalCore.OS boot sequence (`mythos/tools/boot-visual-prompt.md`) — a
  paste-able prompt for an external generator, not rendered output or a
  software change.
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
- [mythos/content/MILESTONES.md](mythos/content/MILESTONES.md) — Lumina's
  detailed weekly build plan.
- `crystal-core/spec/` — architecture and protocol specs for the Starline Weaver
  and Starline.

*Non Solus.*
