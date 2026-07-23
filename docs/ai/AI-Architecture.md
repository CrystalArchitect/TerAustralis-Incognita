# AI architecture — the whole picture

The six pages in this folder each describe one tool. This page is the
assembly instructions: how the roles relate, what connects them today, and
what's proposed but not yet real. Read this first if you're new; read the
individual profiles for depth.

## The roles at a glance

| Tool | Role | One line |
|---|---|---|
| [ChatGPT](ChatGPT.md) | Chief Systems Architect | Turns intent into specs others can build from |
| [Claude](Claude.md) | Repository Engineer | Implements specs across the real tree, through PRs |
| [DeepSeek](DeepSeek.md) | Research & Engineering Specialist | Mathematics, algorithms, analysis with rigor |
| [Gemini](Gemini.md) | Knowledge & Multimodal Specialist | Reads wide — large documents, images, consistency |
| [Grok](Grok.md) | Creative Exploration | Diverges first; ideas and art, filtered later |
| [GitHub](GitHub.md) | Development Platform | Not an AI — where every flow ends and becomes canon |

## How they connect today

Every arrow below is a **working agreement**, not enforced software — the
full flows (which tool feeds which, and in what order per kind of task) are
in [`AI-Workflow.md`](AI-Workflow.md). In outline:

```
   DeepSeek ─┐
             ▼
   Gemini ─▶ ChatGPT ─▶ Claude ─▶ GitHub ─▶ (merged: canon)
             ▲
   Grok ─────┘
```

ChatGPT is the hub every design-shaped flow passes through before Claude
touches the tree; GitHub is the hub every flow passes through before
anything counts. Nothing left of GitHub is canon on its own — see
[`AI-Workflow.md`](AI-Workflow.md#what-the-flows-mean-in-practice).

## What's actually enforced vs. practiced vs. proposed

Three different strengths of rule apply to "AI architecture" here, and
conflating them is the most common way a repo like this drifts into
overclaiming ([`The-Incognita-Rule.md`](../governance/The-Incognita-Rule.md)):

- **Enforced in code** — the Starline Weaver refuses unlabeled messages; the
  CrystalBridge gate fails closed. Detail:
  [`docs/architecture/AI-Weave.md`](../architecture/AI-Weave.md).
- **Practiced by convention** — the roles and flows on this page and in
  `AI-Workflow.md`. Nothing stops a contributor from skipping them; review
  is the only enforcement, per
  [`AI-Governance.md`](../governance/AI-Governance.md).
- **Proposed, not built** — see below.

## Proposed: an AI Orchestrator

Raised in review (ChatGPT, 2026-07-23): rather than each tool being reached
independently, an **orchestrator** could sit in front of the roles and route
a task to whichever tool fits it —

```
CrystalCore
    │
    ▼
AI Orchestrator
 ├── ChatGPT
 ├── Claude
 ├── DeepSeek
 ├── Gemini
 ├── Grok
 └── GitHub
```

This is **Vision, not Built** — an architectural pattern under discussion,
with no design doc, no code, and no ADR yet. It would be a real addition to
the Lattice's designed-but-unbuilt machinery
([`docs/architecture/Lattice.md`](../architecture/Lattice.md)) rather than a
restatement of it: the Lattice's Weave Map registers nodes, but doesn't
route work between them. If it moves forward, the path is the one this repo
already documents for structural change: a concrete spec from ChatGPT, an
ADR recording the decision, then implementation — the same sequence that
produced the v1.0 architecture itself
([`docs/adr/ADR-0001.md`](../adr/ADR-0001.md)).

Until then, routing "which AI for this task" stays a human judgment call,
made by reading [`AI-Workflow.md`](AI-Workflow.md) and picking the matching
flow.
