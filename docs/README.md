# Documentation

The documentation tree of the CrystalCore OS repository architecture. Each
area answers one kind of question; nothing in here is executable code, and
nothing in here claims to be more built than it is (see
[`governance/The-Incognita-Rule.md`](governance/The-Incognita-Rule.md)).

| Area | Question it answers |
|------|---------------------|
| [`vision/`](vision/) | Why does this project exist, and where is it going? |
| [`architecture/`](architecture/) | How is the system designed — components, relationships, data flow? |
| [`governance/`](governance/) | How are decisions made — review rules, standards, the Constitution? |
| [`ai/`](ai/AI-Architecture.md) | Which AI tools contribute, and how do they fit together? |
| [`agents/`](agents/) | Operating instructions for each AI agent working in this repo |
| [`guides/`](guides/) | How do I do a specific task — commit, push, connect a guest AI? |
| [`adr/`](adr/) | Architecture Decision Records — why the big calls were made |
| [`reviews/`](reviews/) | Point-in-time architectural surveys — dated snapshots, not living docs |

Component-level specs that used to live beside the code are under
[`architecture/crystal-core/`](architecture/crystal-core/); the Lattice
design sketch is under [`architecture/lattice/`](architecture/lattice/).

Start points: new to the project → the root [`README.md`](../README.md);
contributing → [`CONTRIBUTING.md`](../CONTRIBUTING.md) and
[`governance/Review-Process.md`](governance/Review-Process.md); working as an
AI agent → the root [`AGENTS.md`](../AGENTS.md) and your file in
[`agents/`](agents/).
