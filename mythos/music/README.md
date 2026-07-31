# Mythos Music

Audio canon of the TerAustralis Incognita universe. Content licensed
CC BY-NC-ND 4.0 — see [`../content/LICENSE-CONTENT.md`](../content/LICENSE-CONTENT.md).

The lyrics live as text in [`../content/`](../content/), one page per work.
The recordings live here, and also on Suno at
[@m13crystalat](https://suno.com/@m13crystalat).

That second sentence is the reason this directory exists. Until 2026-07-31 the
music was the only kind of work in this portfolio held in exactly one place, by
a third party, with no local copy, no hash and no date — a lapsed subscription
or a changed platform policy was enough to lose it. Every work the canon names
now has a recording here, hashed and covered by
[`../MANIFEST.sha256`](../MANIFEST.sha256).

## Adding a track

1. Export the audio from Suno at the highest quality offered. Keep the
   original filename out of it — name the file after the work, in kebab-case,
   matching the lyric page where one exists: `red-dust-axis.mp3`.
2. Add a row to the catalogue below. Every column is required; "unconfirmed" is an
   acceptable value and a far better one than a guess.
3. Re-run the manifest so the new file is covered by the next timestamp:

   ```sh
   python3 ../tools/provenance.py
   ```

## The catalogue

Four works are named in the canon: the **three ignition songs** written across
the sky in [The First Remembering](../content/THE-FIRST-REMEMBERING.md#the-three-songs),
and [Wire Skull Memory](../content/WIRE-SKULL-MEMORY.md), which its own page
marks as standalone and explicitly *not* one of the three. That distinction is
the canon's, not this file's, and is preserved here rather than flattened into
a single list.

**A work can have more than one recording** — Shooting Star Girl has two,
generated nearly three months apart — so this table has one row per
*recording*, not per song.

Files are named `<work>-<generation date>.mp3` wherever more than one recording
of a work exists. The date is a fact the file carries about itself; a name like
`-final` or `-v2` would be a judgement, and which take is the song is not
something a filename should quietly decide.

| File | Work | Ignition song | Length | Generated | Suno track id | Suno plan |
|---|---|---|---|---|---|---|
| [`red-dust-axis.mp3`](red-dust-axis.mp3) | [Red Dust Axis](../content/RED-DUST-AXIS.md) | yes | 3:35 | 2026-05-02T19:36:19Z | `f8502175-74c7-4cf1-adc0-16c7eb7c8cf3` | **unconfirmed** |
| [`shooting-star-girl-2026-05-04.mp3`](shooting-star-girl-2026-05-04.mp3) | [Shooting Star Girl](../content/SHOOTING-STAR-GIRL.md) | yes | 2:15 | 2026-05-04T03:07:33Z | `3903f9ed-f13b-4d3a-9a6d-bb598760ebd5` | **unconfirmed** |
| [`wire-skull-memory.mp3`](wire-skull-memory.mp3) | [Wire Skull Memory](../content/WIRE-SKULL-MEMORY.md) | no | 2:16 | 2026-05-07T06:21:02Z | `1a194a77-0d9b-4d93-94f7-7a8388b24de0` | **unconfirmed** |
| [`fermis-silent-line.mp3`](fermis-silent-line.mp3) | [Fermi's Silent Line](../content/FERMIS-SILENT-LINE.md) | yes | 4:34 | 2026-05-10T12:53:53Z | `d2563605-d533-4714-98b5-996da3c59cf9` | **unconfirmed** |
| [`shooting-star-girl-2026-07-30.mp3`](shooting-star-girl-2026-07-30.mp3) | [Shooting Star Girl](../content/SHOOTING-STAR-GIRL.md) | yes | 3:34 | 2026-07-30T14:01:06Z | `4a115658-9096-4f23-be27-779e7b3cda63` | **unconfirmed** |

Rows are in generation order, which turns out to describe a single week in May
2026 — the 2nd, 4th, 7th and 10th — and then one return to Shooting Star Girl
almost three months later.

All recordings are MP3, VBR between roughly 179 and 196 kbps, 48 kHz stereo.
Lyrics for every work are credited to the CrystalArchitect and CrystalDreamer
(Grok); the audio is Suno, generator version unrecorded. Every length,
timestamp and track id above was read from the file's own ID3 tag rather than
supplied by hand.

**The catalogue is complete against the canon as it stands** — every work with
a lyric page now has at least one recording here. Whether more exist on the
Suno account than the canon names is not something this file can know.

**Which Shooting Star Girl is the song is an open question**, and this file
does not answer it. Both recordings are kept. If one is later chosen as canon,
say so here in a dated line and leave the other standing — the earlier record
is not wrong about the date it describes.

### What the columns mean

- **Ignition song** — whether the work is one of the three written across the
  sky in The First Remembering, or standalone. The canon draws this line; the
  catalogue records it rather than deciding it.
- **Generated** and **Suno track id** — read from the file's ID3 tag. The id is
  a durable pointer back to the source, worth keeping now rather than
  reconstructing later.
- **Suno plan** — free, Pro, or Premier, *at the time the track was
  generated*. This is not bookkeeping trivia. Suno's free tier grants
  non-commercial use only; paid tiers grant commercial rights. The same audio
  file carries different rights depending on the plan it was made under, and
  the answer cannot be recovered from the file later. Record it while it is
  still knowable.

  **Why every row still says "unconfirmed."** There is circumstantial evidence
  of a paid plan: as part of Warner Music's November 2025 settlement, Suno
  restricted audio downloads to paid accounts, and all five files were
  downloaded after that change. That is evidence, not proof — the restriction's
  exact scope and enforcement are not something this repository can verify.
  Only the account holder can confirm the plan, and until they do the honest
  value is "unconfirmed" rather than a convenient assumption in the direction
  we would prefer.

  **And the answer may differ per track.** Four of the recordings come from one
  week in May 2026; the fifth is from 30 July, nearly three months later. A
  subscription can start, lapse or change tier across a gap that size, so one
  answer for the whole catalogue would be a guess dressed as a fact. That is
  why this column exists per row rather than once at the top of the page.

  Two dates settle all five: whatever plan was active in **early May 2026**,
  and whatever was active on **30 July 2026**.

## Truth labels

The [art README](../art/README.md) carries truth labels where a work needs
one — two pieces there bear a real person's photographic likeness and are
excluded from the Ordinals grant for that reason. The same discipline applies
here. A track needs a truth label if:

- it uses a real person's voice or likeness;
- it was generated on a plan that does not permit commercial use;
- it samples, interpolates or closely models an identifiable existing work;
- its provenance is uncertain in any way that would matter to someone
  licensing it.

## On copyright, plainly

Music generated by a model may attract **no copyright at all** — in Australia
as in the United States, copyright generally requires a human author. The
lyrics here are human-written (with model assistance, credited), and lyrics
are a separate copyright from a recording; the generated audio is the part in
question.

The practical consequence is not that the work is worthless. It is that the
thing being sold may not be exclusivity. What cannot be copied by copying a
file is the canon these songs belong to — the lattice, the lore, the art, one
author's coherent universe.

Two documents are affected by this and should be read alongside it:
[`../../docs/governance/ORDINALS-LICENCE-GRANT.md`](../../docs/governance/ORDINALS-LICENCE-GRANT.md),
which describes the Grantor as sole copyright holder, and
[`../content/LICENSE-CONTENT.md`](../content/LICENSE-CONTENT.md), which is a
copyright licence and therefore only bites where copyright exists.

Neither is wrong to have. Both are worth understanding before money moves.

## Ordinals

The [Ordinals licence grant](../../docs/governance/ORDINALS-LICENCE-GRANT.md)
covers **images in `mythos/art/` as at 2026-07-28**. It does not cover audio,
this directory, or anything added since that date. Extending it takes a dated
amendment to that file — not an assumption made here.

**The project issues no token.** That statement is load-bearing in the grant
and is repeated here so it travels with the music too.
