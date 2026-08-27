# memory/ — durable Claude Code memory

**Status:** Docs / governance. This directory is a working map, not canon.

Canon lives in `docs/governance/`, `docs/adr/`, `mythos/`, and the other
repository sources this folder points at. Memory **summarises and dates**.
If a summary here disagrees with a canonical file, the canonical file wins
and the conflict is recorded.

Root instruction: [`../CLAUDE.md`](../CLAUDE.md).

## Why this exists

Claude sessions are scoped. Anything that matters must land on disk
([`docs/ai/Claude.md`](../docs/ai/Claude.md): "disk is canon, chat is not").
This folder is the write-back surface for confirmed decisions, open
questions, milestones, and the current working picture — so the next
session does not have to reconstruct them from chat.

It does **not** restore the Repository Engineer seat. That seat is Grok
Build ([`docs/adr/ADR-0014.md`](../docs/adr/ADR-0014.md)).

## Protocol

**Read at startup**

1. [`CORE.md`](CORE.md) — locked names, purpose, Incognita Rule, cultural floor
2. [`state/CURRENT.md`](state/CURRENT.md) — what is true *now*

**Retrieve by task** — [`INDEX.md`](INDEX.md)

**Write before ending meaningful work**

- [`DECISIONS.md`](DECISIONS.md)
- [`OPEN-QUESTIONS.md`](OPEN-QUESTIONS.md)
- [`MILESTONES.md`](MILESTONES.md)
- [`state/CURRENT.md`](state/CURRENT.md)

**Never write** — [`PRIVACY.md`](PRIVACY.md)

## Labels (do not collapse)

| Memory label | Incognita Rule | Belt-Three ([`CONTRIBUTING.md`](../CONTRIBUTING.md)) |
|---|---|---|
| **Built** | Surveyed — running, tested, or checkable against the world | Science |
| **Vision** | Dreamed — mythos, art, speculative framing, labeled as such | Story and Vision |
| **Unknown** | Preserve the uncertainty. Docs never outpace code | Honest gap; not a third cosmology |

Unknown is not a license to invent a shoreline. See
[`The-Incognita-Rule.md`](../docs/governance/The-Incognita-Rule.md).

## Authority

Canonical source / locked canon **>** this folder **>** current working
context **>** hypotheses.

## Files

| File | Role |
|---|---|
| [`CORE.md`](CORE.md) | Slow-changing identity. Rarely edited. |
| [`INDEX.md`](INDEX.md) | Retrieval map into the real tree. |
| [`PRIVACY.md`](PRIVACY.md) | What never enters git memory. |
| [`DECISIONS.md`](DECISIONS.md) | Pointers at ADRs. Not a second ADR log. |
| [`OPEN-QUESTIONS.md`](OPEN-QUESTIONS.md) | Live gates. |
| [`MILESTONES.md`](MILESTONES.md) | Recently landed, dated. |
| [`state/CURRENT.md`](state/CURRENT.md) | Working picture. Overwritten each checkpoint. |

*Non Solus.*
