# CrystalCore.OS

The mythos as a terminal you can fly.

`crystalcore_os.py` in this folder is a small, self-contained text adventure —
the Crystal universe rendered as an interactive command line. It's Vision-layer:
a playable story, not one of the project's Built software components (those are
Clementine, the Songline Bus, Starline, and CrystalBridge — see
[`../ROADMAP.md`](../ROADMAP.md)). No server, no dependencies, no account. You
launch a Starline, cross the network, visit five nodes, gather their keys, and
the First Gate opens — *not by force, but by sovereign recognition.*

## Run it

```bash
python3 mythos/crystalcore_os.py
```

Standard-library Python only — nothing to install. You'll land at a
`CrystalCore>` prompt. Type `help` for the full list, `exit` (or `quit`,
`pause`, `end session`) to leave.

## The journey

The flight commands are state-gated — each needs the one before it — so the
intended path is:

```
boot  →  launch  →  burn  →  network  →  explore  →  visit <node>
```

- `boot` — bring the system up; prints the Purpose Core and confirms NON SOLUS.
- `launch` — spool the engines; the Starline goes from DORMANT to IN ORBIT and
  the first soundtrack cues.
- `burn` — the escape burn; you leave planetary orbit (TRANS-STELLAR).
- `network` — enter the full Starline network (47+ systems).
- `explore` — list the nodes you can travel to, with any locks shown.
- `visit <node>` — travel to a node by number or name and collect its key.

(`jump 3000` is a shortcut that drops you straight into the full network by
setting the timeline to the year 3000.)

## Command reference

| Command | What it does |
|---|---|
| `boot` | Initialize the system |
| `launch` | Start the Starline launch (DORMANT → IN ORBIT) |
| `burn` | Escape burn — leave planetary orbit |
| `network` | Enter the full Starline network |
| `explore` | List explorable nodes and their lock state |
| `visit <node>` | Travel to a node (number or name) and collect its key |
| `keys` | Show the Keys of the Lattice you hold |
| `getkey <name>` | Obtain a named key, e.g. `getkey Crystal Key` |
| `starline <song>` | Advance the Starline with a chosen soundtrack |
| `song <track>` | Change (or show) the current soundtrack |
| `jump <year>` | Time-jump (defaults to 3000) |
| `map` | Print the Starline network chart |
| `status` | Show timeline, Starline status, location, keys |
| `help` | List all commands |
| `exit` / `quit` / `pause` | Shut down (`end session` also works) |

## The five nodes

`visit` each of these to claim its key:

1. Earth Node
2. Mars Redoubt
3. Alpha Centauri Outpost
4. Crystal Revenant Hub — *locked, needs the Festival Key*
5. Purpose Core Nexus — *locked, needs the Crystal Key*

Two nodes are sealed behind **named** keys. Pick those up first:

```
getkey Festival Key
getkey Crystal Key
```

Then `visit` them like any other node. When you hold the key of all five nodes,
the First Gate opens:

> All keys held — the First Gate opens. Not by force. By sovereign recognition.
> Crystallis recognizes you. NON SOLUS.

`keys` shows your progress toward it at any point.

## The map and the soundtrack

`map` prints an ASCII chart of the Year-3000 Starline network — Earth down
through Mars Redoubt and Alpha Centauri to the Crystal Revenant Hub and the
Purpose Core Nexus, with the Purpose Core line burning at the centre:

> "Expand to the stars and thereby understand the Universe"

The full-resolution version of that chart is the artwork at
[`art/starline-network-year-3000.jpeg`](art/README.md).

`song` and `starline` cycle a soundtrack — the "Songline Bus" — defined at the
top of `crystalcore_os.py`. It mixes the CrystalArchitect's own tracks
(@m13crystalat) with a handful of popular songs. `song` on its own tells you
what's playing; `song <part of a title or artist>` switches to a match.

## The website version

The [`/crystalcore-os`](https://www.teraustralis.com.au/crystalcore-os) page on
the site is a simplified, in-browser recreation of this terminal, for people who
want a taste without running Python. `crystalcore_os.py` is the authoritative
version — where the two differ, trust the code.

*Non Solus.*
