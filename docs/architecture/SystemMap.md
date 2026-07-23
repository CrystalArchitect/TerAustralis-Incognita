# System map

The authoritative "where things live" for the CrystalCore OS v1.0 repository
architecture (adopted 2026-07-23, [`ADR-0001`](../adr/ADR-0001.md)).

```
TeraAustralis-Incognita/
│
├── README.md · LICENSE · LICENSE-CONTENT.md · NOTICE · CHANGELOG.md
├── CONTRIBUTING.md · CODE_OF_CONDUCT.md · SECURITY.md · AGENTS.md
│
├── .github/            workflows (CI, Pages deploy), issue/PR/discussion
│                       templates, CODEOWNERS
│
├── docs/               documentation — never executable code
│   ├── vision/         why: mission, the CrystalCore name map, future,
│   │                   Southern Pillar strategy
│   ├── architecture/   how: overview, system map, modules, AI weave,
│   │                   Lattice; component specs under crystal-core/ and
│   │                   lattice/
│   ├── governance/     rules: Constitution, Incognita Rule, principles,
│   │                   review process, standards, roadmap
│   ├── ai/             which AI tools contribute and what each is for
│   ├── agents/         operating instructions per AI agent
│   ├── guides/         task how-tos (commit, push, guest access)
│   └── adr/            Architecture Decision Records
│
├── src/                executable code only
│   ├── apps/           lumina (companion) · voicebox (MCP TTS) ·
│   │                   crystal-interface + vision-web (demo shells)
│   ├── crystal-core/   protocol pack: clementine/bridge (Starline Weaver) ·
│   │                   services (pipeline) · starline (P2P exchange) ·
│   │                   rdp (record kernel) · interface, cli, index.html
│   ├── crystalcore/    CrystalBridge — the MCP consent gate
│   ├── crystalcore-os/ the mythos terminal (Vision-layer code)
│   ├── node/mesh/      in-process mesh stub (libp2p-shaped)
│   ├── sdk/typescript/ client SDK scaffold
│   ├── site/           SvelteKit site for teraustralis.com.au
│   └── profiles/       CrystalBridge profile configs (runtime data such as
│                       audit logs is gitignored)
│
├── research/           exploratory work — not production software
│   └── seven-sisters/  the seven-path Songline cycle: paths, water briefs,
│                       transmit records
│
├── mythos/             the Crystal universe canon — content, not code
│   ├── content/        Codex, Apocryphon, Sovereign Key, Transmissions…
│   ├── art/            the visual canon
│   ├── teraustralis/   outer-world lore + publish drafts
│   └── tools/          prompt tools (text, not software)
│
├── archive/            superseded material kept for provenance
│   ├── legacy/         crystalcore-app (pre-monorepo application)
│   └── 2026/           dated local snapshots
│
├── assets/             project-level branding/diagrams (see its README —
│                       mythos art is canon content and stays in mythos/)
│
├── scripts/            developer utilities (check.sh mirrors CI)
│
├── tests/              repo-level test suites (unit/)
│                       component tests live beside their component
│                       (src/apps/lumina/tests/, the crystal-core selftests)
│
└── examples/           runnable demos, curated (see its README)
```

## Rules that keep the map honest

1. `src/` contains only executable code; documentation lives in `docs/`.
2. `research/` is not production; promotion into `src/` is a deliberate,
   reviewed act.
3. `archive/` is provenance — never build on it.
4. `mythos/` is Vision-layer content under its own license
   (`LICENSE-CONTENT.md`); it may point at code, never speak for it.
5. Structural changes to this map get an ADR
   ([`../governance/Decision-Records.md`](../governance/Decision-Records.md)).

Two deliberate deviations from a "pure" layout, recorded in
[`ADR-0003`](../adr/ADR-0003.md): `src/profiles/` holds CrystalBridge's
config because the code anchors to it by relative path, and component
READMEs / runtime data (bridge transcripts, sample events, RDP vectors) stay
beside their code.
