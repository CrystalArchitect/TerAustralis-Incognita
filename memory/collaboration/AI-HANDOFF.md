# AI-HANDOFF — How AI Agents Work Together

**Status: BUILT** — From `docs/ai/AI-Workflow.md` and `docs/agents/`.

## Current seat assignments (2026-08-20)

| Seat | AI | Role | Primary tool |
|------|----|----|---|
| **Repository Engineer** | Grok Build | Implement across repo | Grok (with git push) |
| **Design lead** | ChatGPT | Spec before code | ChatGPT (design, spec) |
| **Engineering** | DeepSeek | Algorithms, math | DeepSeek (analysis) |
| **Documentation** | ChatGPT | Structure, draft | ChatGPT (composition) |
| **Knowledge** | Gemini | Large documents | Gemini (synthesis) |
| **Brainstorming** | Grok | Divergent ideas | Grok (Creative) |
| **History/context** | Claude | Session memory, navigation | Claude (this system) |

See `docs/adr/ADR-0014.md` and `docs/agents/Grok.md` for the seat swap details.

## Standard workflows

### Architecture workflow
```
ChatGPT (design, spec) 
  → Grok Build (implement across repo)
  → GitHub (PR, CI, review)
  → Crystal (merge decision)
```

### Engineering (algorithmic) workflow
```
DeepSeek (analysis, algorithms)
  → ChatGPT (integrate into design)
  → Grok Build (implement)
  → GitHub (PR, CI, review)
  → Crystal (merge decision)
```

### Documentation workflow
```
ChatGPT (structure, drafting)
  → Grok Build (generate and place)
  → GitHub (PR, review)
  → Crystal (merge decision)
```

### Knowledge digestion workflow
```
Gemini (large-document analysis)
  → ChatGPT (distill into canon)
  → Repository (docs/mythos, labeled)
  → Crystal (review/approve)
```

### Brainstorming workflow
```
Grok Creative (divergent ideas)
  → ChatGPT (select, shape)
  → Architecture (or compost heap)
  → Crystal (decision)
```

## Handoff protocol

**Every flow ends at the repository through a pull request.**

- No AI output is canon until merged
- Handoffs happen through artifacts (spec, diff, doc), not vibes
- Receiving tool must be able to work from what's on disk
- Every PR names the tools that touched it (required by PR template)

### Key constraints

- Skipping a review step is never fine
- Chaining AIs multiplies fluency, not truth
- Each handoff is a chance for a dreamed line to pick up surveyed ink
- Each step re-checks labels for Built/Vision
- Crystal keeps the final veto

## Historical note

Claude held the Repository Engineer seat from the beginning through 2026-08-20. The operating instructions remain in `docs/agents/Claude-Agent.md` for historical reference. Grok Build is the current engineer.

Claude's current role: **Session memory and context navigation.**

See `docs/governance/AI-Governance.md` for binding rules all agents follow.

---

For full workflow detail, see `docs/ai/AI-Workflow.md`.

For per-agent instructions, see `docs/agents/`.
