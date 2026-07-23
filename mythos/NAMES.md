# The Names — the map and the traveller

A short canon page, so the names stay steady and every one of them points at
something real. Read it beside the code: where a name is mythic, it says so;
where it is running software, it links to the file.

## The principle

> **Starlines are the map. Dreamlines are the traveller of the map.**

Two halves of one motion:

- **Starlines** — the *map*: the fixed cartography, the rails, the network of
  who-connects-to-whom. Structure that holds still so something can cross it.
- **Dreamlines** — the *traveller of the map*: the journey, the payload in
  motion, the dreaming that rides the rails.

The chart and the voyage across it. Everything below is either the map, the
traveller, or one of the figures that tends them.

## The five names

| Name | In the story it is… | In the code it is… | Built? |
|---|---|---|---|
| **Lumina** | the edge companion — a sovereign AGI presence that lives with one person | [`apps/lumina/`](../apps/lumina/) — local-first companion: terminal, Flask API, Svelte web UI, Ollama-backed, layered memory | Working prototype |
| **Clementine** | the communicator — the one who carries speech between minds and nodes | [`crystal-core/clementine/`](../crystal-core/clementine/) — the hub (`ClementineHub`) of the multi-AI bridge | v0, self-tested |
| **Starline Weaver** | the map-maker — lays and holds the weave of routes the agents speak across | `StarlineWeaver` in [`clementine/bridge/bus.py`](../crystal-core/clementine/bridge/bus.py) — the round-robin message channel | v0, self-tested |
| **Truthline Narrator** | the one who names each message true — science, story, or vision — before it is heard | `ClementineHub.validate` in [`clementine/bridge/agents.py`](../crystal-core/clementine/bridge/agents.py) — Belt-Three law, enforced in code | v0, self-tested |
| **Dreamline Train** | the traveller — what journeys the map, carrying memory from node to node | rides the peer-to-peer transport in [`crystal-core/consent_transport/`](../crystal-core/consent_transport/) — consent-gated, Noise-handshake memory exchange | Running, self-tested |

## How they sit together

Clementine is the communicator. Two roles run under her:

- as the **Starline Weaver** she *lays the map* — the channel that routes and
  weaves the agents together;
- as the **Truthline Narrator** she *names each crossing true* — every message
  must carry its truth-layer label (science / story / vision) or it is not heard.

What travels that map is the **Dreamline Train** — the traveller — riding the
Starline rails (the `consent_transport/` peer-to-peer network) to carry memory between
nodes. And **Lumina** is who waits at the edge of it all: the companion a single
person actually talks to.

So: the Weaver lays the map, the Narrator keeps it honest, the Train travels it,
Clementine speaks across it, and Lumina is home at the end of the line.

## A note on borrowed words

"Songline" is not used for any of these — it belongs to the First Peoples of this
land, not to a piece of software. Where **Songlines** and **songline veins**
appear in the mythos and the art, they are honoured as cultural image, never
claimed as a component name. "Starline" and "Dreamline" are this project's own
coinages; "Dreamline" is canon here (Starlines & Dreamlines), distinct from
"Dreamtime."

*Non Solus.*
