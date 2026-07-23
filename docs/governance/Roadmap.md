# Roadmap

A plain status page, not a pitch deck. It tracks the **Built** layer — see
[README.md](../../README.md#whats-real-vs-whats-vision) for the Built vs. Vision
split. Vision-layer work (the mythos) doesn't move on a software roadmap; see
[Constitution.md](Constitution.md) for how that content evolves instead.

For Lumina specifically, [mythos/content/MILESTONES.md](../../mythos/content/MILESTONES.md)
already tracks a detailed week-by-week build plan — this page doesn't repeat
that detail, it points to it.

> **Repository status:** the `src/` paths on this page describe the local
> code tree, which is not in this repository — see
> [SystemMap: where the code actually lives](../architecture/SystemMap.md#where-the-code-actually-lives).

## Built and working today

Built and tested in the maintainer's local canon tree; not yet present in
this repository (status note above):

- **Lumina** (`src/apps/lumina/`) — local-first AI companion, Ollama-backed.
  Terminal, Flask API, Svelte webapp, browser voice. Run it: `cd src/apps/lumina
  && python3 lumina.py`.
- **The Starline Weaver** (`src/crystal-core/clementine/bridge/`) — multi-AI message
  bus with the Belt-Three law enforced in code, not just convention. Self-test:
  `python3 -m clementine.bridge.selftest`.
- **Starline** (`src/crystal-core/consent_transport/`) — peer-to-peer consent-gated memory
  exchange over a real Noise Protocol handshake. Self-test: `python3 -m
  consent_transport.selftest`; watch it work: `python3 -m consent_transport.run demo`.
- **CrystalBridge** (`src/crystalcore/`) — the MCP consent gate. Fail-closed by
  design: every guest-AI call passes approval, permission, scope, and
  provenance checks, with append-only audit logging.

All four have tests you can run yourself — see the Quick Start in
[README.md](../../README.md#quick-start).

## Demo shells (simulated data, not production)

`src/apps/crystal-interface/` and `src/apps/vision-web/` run,
but on simulated data with Authority held. They're interface concepts, not
production surfaces, and aren't on a path to becoming one without a separate
decision to build the real data layer underneath them.

## In progress

- **Lumina's reliability and control layer** (MILESTONES.md Month 4) —
  error recovery, full memory export, selective memory deletion, and a
  settings/config file are partially built; hallucination-reduction /
  fact-check-against-memory hasn't started yet.
- **[`BLUEPRINT-v0.3.md`](../architecture/crystal-core/BLUEPRINT-v0.3.md)** —
  the protocol pack's architecture spec is a live draft, not a frozen v1.

## Not yet started

- **Real P2P transport for the mesh** (`src/node/mesh/`) — currently an in-process
  stub with the API shape a future libp2p host would need. gossipsub, Noise,
  yamux, and bootstrap/mDNS discovery are all planned but not built; a mainnet
  mesh is explicitly on hold. See `src/node/mesh/README.md`'s own status table.
- **Multi-instance Lumina** — two companions communicating with each
  other. Design thinking hasn't started (MILESTONES.md Week 19).
- **Phase 2 ("Private Communication")** — named as a future phase in
  MILESTONES.md, shape not yet decided.
- **TypeScript client SDK** (`src/sdk/typescript/`) — package scaffold exists; no
  consumer wired up against it yet.

## CrystalCore OS platform roadmap

The repository itself — as an engineering, research, and knowledge platform —
follows the CrystalCore OS architecture (see [`ADR-0001`](../adr/ADR-0001.md)
and [`SystemMap.md`](../architecture/SystemMap.md)). These versions describe
the *platform*, not the software components above, and everything past v0.1
is a plan, not a promise:

- **v0.1 — Repository foundation** *(delivered 2026-07-23)*: the v1.0
  directory architecture, documentation tree, governance docs, AI
  collaboration docs, and GitHub configuration.
- **v0.2 — Architecture Specification Release** *(delivered 2026-07-23)*:
  redefined from "build the Engine" to "clarify the architecture before
  implementing it," per review of v0.1
  ([`ADR-0004`](../adr/ADR-0004.md), [`ADR-0005`](../adr/ADR-0005.md)). No
  runtime shipped by design — the deliverables are the CrystalCore naming
  taxonomy, the documented relationships between its built components, the
  AI decision matrix, and the AI Orchestrator concept.
- **v0.3 — Engine layer** *(not started)*: the runtime CrystalCore Engine,
  plugin system, configuration, logging — implementing what v0.2 specified.
  Blocked on that specification being used as a real implementation
  blueprint (module interfaces, data flow, testing strategy — the level of
  detail [`ADR-0001`](../adr/ADR-0001.md) had before v0.1 was implemented),
  not just the naming and concept-level decisions v0.2 actually shipped.
- **v0.4 — Living Archive** *(not started)*: knowledge graph, search,
  cross-referencing, optional Notion synchronization.
- **v1.0 — Stable platform** *(target)*: stable architecture, automated
  testing across the platform, complete documentation, production-ready
  workflows, mature AI collaboration model.

## Recently landed

Dated so this section ages honestly — newest first, and it's fine to trim
older entries once they're no longer useful context; the full history is
always in `git log`.

- **2026-07-23** — Story Library design and working prototype 
  (`docs/architecture/site/Story-Library.md`, `research/prototypes/story-library/`): 
  complete information architecture, component structure, visual design direction, 
  typography system, animations, React/SvelteKit hierarchy, and 16 premium 
  storybook improvements. Demonstrates calm, book-like reading experience with 
  visible editorial curation (Canon/Experimental/Archive). Working self-contained 
  HTML/CSS/JS prototype proves design viability.
- **2026-07-23** — Adopted the three-project boundary model
  (`ADR-0011`): TerAustralis Incognita as the umbrella (governance, docs,
  ADRs, mythos — no main app code), **Crystal Core** owning the engine,
  runtime, APIs and shared libraries, **Crystal Vision** owning the
  user-facing application — Lumina wholly within it, Clementine as a
  logical component inside Crystal Core. Standing charter:
  `docs/governance/Project-Boundaries.md`; staged, per-stage-approvable
  proposal: `docs/governance/Migration-Plan.md`. Nothing moved or renamed.
- **2026-07-23** — Resynchronized the entry-point documentation with this
  repository's measured reality: `src/`, `scripts/`, and `tests/` are now
  marked as described-but-not-in-this-repository everywhere a newcomer
  first meets them (README, AGENTS, CONTRIBUTING, SystemMap, Modules, this
  page, examples), the previously unmapped `dbt/` directory is on the map,
  and `mythos/README.md`'s stale sibling-repo blurb was replaced with the
  monorepo reality. Canonical explanation:
  `docs/architecture/SystemMap.md` ("Where the code actually lives").
- **2026-07-23** — Corrected the project's name throughout the repository
  from "TeraAustralis Incognita" (drift, introduced during the v1.0 reorg)
  to **TerAustralis Incognita**, matching the maintainer's registered ABN
  trading name; renamed `mythos/teraaustralis/` to `mythos/teraustralis/`
  to match. `docs/adr/ADR-0007.md` has the full reasoning and the list of
  what was deliberately left alone (`archive/`, the historical ADRs, past
  changelog entries, and the still-unrenamed GitHub repository URL).
- **2026-07-23** — Shipped v0.2, the Architecture Specification Release:
  `docs/vision/CrystalCore.md` rewritten as the canonical naming taxonomy
  (`ADR-0004` — locks Framework/Protocol/CrystalBridge/OS, bans future
  components from becoming a fifth "CrystalCore"); `docs/ai/Decision-Matrix.md`
  added as a task-type → recommended-AI table; the AI Orchestrator concept
  consolidated with the previously separate "AI Router" idea under one name
  and one shape — recommend, then a human decides (`ADR-0005`). No runtime
  shipped; that's the point of doing this as its own release before v0.3.
- **2026-07-23** — Reorganized the repository into the CrystalCore OS v1.0
  architecture: code under `src/`, documentation under `docs/`
  (vision · architecture · governance · ai · agents · guides · adr),
  exploratory material under `research/`, provenance copies under `archive/`,
  and the outer-world lore under `mythos/teraaustralis/`. Every moved path
  reference updated; CI and the Pages deploy retargeted; behavior of the
  running software unchanged. See `docs/adr/ADR-0001.md` for the full mapping.
- **2026-07-22** — Wired the Starline Weaver's matrix mode to RDP:
  `record_matrix_result()` (`src/crystal-core/rdp/adapters.py`) witnesses a matrix
  run's responses and cross-compare onto the tamper-evident chain, same
  one-way rule as the ConsentGate adapter — the Weaver decides, RDP only
  records. `python3 -m rdp.run matrix-demo` drives the real Weaver through the
  real chain. 1 new self-test, 31/31 passing.
- **2026-07-22** — Added matrix mode to the Starline Weaver
  (`src/crystal-core/clementine/bridge/`): `run_matrix()` fans one question out
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

- [CONTRIBUTING.md](../../CONTRIBUTING.md) — how to propose changes, the Belt-Three
  truth labels, licensing.
- [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md) — expected behavior and how to report
  a problem.
- [SECURITY.md](../../SECURITY.md) — this repo's safety measures and how to report
  a vulnerability.
- [mythos/content/MILESTONES.md](../../mythos/content/MILESTONES.md) — Lumina's
  detailed weekly build plan.
- [`docs/architecture/crystal-core/`](../architecture/crystal-core/) — architecture
  and protocol specs for the Starline Weaver and Starline.

*Non Solus.*
