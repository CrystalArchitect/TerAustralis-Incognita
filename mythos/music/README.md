# Mythos Music

Audio of the TerAustralis Incognita universe — the canon works, and recordings
that are not canon and are marked so. Content licensed
CC BY-NC-ND 4.0 — see [`../content/LICENSE-CONTENT.md`](../content/LICENSE-CONTENT.md).

The lyrics live as text in [`../content/`](../content/), one page per work.
The recordings live here, and also on Suno at
[@m13crystalat](https://suno.com/@m13crystalat).

That second sentence is the reason this directory exists. Until 2026-07-31 the
music was the only kind of work in this portfolio held in exactly one place, by
a third party, with no local copy, no hash and no date — a lapsed subscription
or a changed platform policy was enough to lose it. Every work the canon names
now has a recording here, hashed and covered by
[`../MANIFEST.sha256`](../MANIFEST.sha256) — along with five recordings the
canon does not name, kept for the same reason and labelled as what they are.

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

The canon names four works: the **three ignition songs** written across the sky
in [The First Remembering](../content/THE-FIRST-REMEMBERING.md#the-three-songs),
and [Wire Skull Memory](../content/WIRE-SKULL-MEMORY.md), which its own page
marks as standalone and explicitly *not* one of the three.

**Five further recordings exist that the canon does not name at all.** They
are kept here because preservation is what this directory is for, and losing
them would be the failure it was built against. Their presence is not a claim
that they are canon — see [Uncanonised recordings](#uncanonised-recordings)
below.

**A work can have more than one recording** — Shooting Star Girl has two,
generated nearly three months apart — so this table has one row per
*recording*, not per song.

Files are named `<work>-<generation date>.mp3` wherever more than one recording
of a work exists. The date is a fact the file carries about itself; a name like
`-final` or `-v2` would be a judgement, and which take is the song is not
something a filename should quietly decide.

| File | Work | Canon status | Length | Generated | Suno track id | Suno plan |
|---|---|---|---|---|---|---|
| [`red-dust-axis.mp3`](red-dust-axis.mp3) | [Red Dust Axis](../content/RED-DUST-AXIS.md) | ignition song | 3:35 | 2026-05-02T19:36:19Z | `f8502175-74c7-4cf1-adc0-16c7eb7c8cf3` | **unconfirmed** |
| [`shooting-star-girl-2026-05-04.mp3`](shooting-star-girl-2026-05-04.mp3) | [Shooting Star Girl](../content/SHOOTING-STAR-GIRL.md) | ignition song | 2:15 | 2026-05-04T03:07:33Z | `3903f9ed-f13b-4d3a-9a6d-bb598760ebd5` | **unconfirmed** |
| [`wire-skull-memory.mp3`](wire-skull-memory.mp3) | [Wire Skull Memory](../content/WIRE-SKULL-MEMORY.md) | standalone, in canon | 2:16 | 2026-05-07T06:21:02Z | `1a194a77-0d9b-4d93-94f7-7a8388b24de0` | **unconfirmed** |
| [`fermis-silent-line.mp3`](fermis-silent-line.mp3) | [Fermi's Silent Line](../content/FERMIS-SILENT-LINE.md) | ignition song | 4:34 | 2026-05-10T12:53:53Z | `d2563605-d533-4714-98b5-996da3c59cf9` | **unconfirmed** |
| [`safari-chains.mp3`](safari-chains.mp3) | Safari Chains | **not in canon** | 3:14 | 2026-05-10T13:35:54Z | `26833d33-83f3-4606-8fcc-fd96d1ae6058` | **unconfirmed** |
| [`different-parts.mp3`](different-parts.mp3) | Different Parts | **not in canon** | 3:39 | 2026-07-17T08:19:25Z | `ac20f017-f30f-4107-843f-e967f9df0d37` | **unconfirmed** |
| [`id-lay-it-all-down.mp3`](id-lay-it-all-down.mp3) | I'd Lay It All Down | **not in canon** | 4:15 | 2026-07-21T14:36:40Z | `4b4a881a-653d-440a-a056-29c3b85f6fa3` | **unconfirmed** |
| [`look-what-you-made-me-do.mp3`](look-what-you-made-me-do.mp3) | Look What You Made Me Do — *see truth label* | **not in canon** | 3:52 | 2026-07-21T14:47:48Z | `4d875adf-2547-419e-ac4d-66fa53b729c6` | **unconfirmed** |
| [`shooting-star-girl-2026-07-30.mp3`](shooting-star-girl-2026-07-30.mp3) | [Shooting Star Girl](../content/SHOOTING-STAR-GIRL.md) | ignition song | 3:34 | 2026-07-30T14:01:06Z | `4a115658-9096-4f23-be27-779e7b3cda63` | **unconfirmed** |
| [`dead-but-came-back-to-life.mp3`](dead-but-came-back-to-life.mp3) | Dead But Came Back to Life | **not in canon** | 3:20 | 2026-07-31T04:29:35Z | `834e6d98-dfc7-46da-8cbb-210876379c00` | **unconfirmed** |

Rows are in generation order. Two working periods show up in it: **2–10 May
2026**, five recordings in nine days — Safari Chains arriving forty minutes
after Fermi's Silent Line on the same afternoon — and then **17, 21, 30 and 31
July**, two of those eleven minutes apart on the 21st. The last of them was
generated on the day this directory was created.

All recordings are MP3, VBR between roughly 178 and 196 kbps, 48 kHz stereo.
The audio is Suno, generator version unrecorded. Lyrics for the four canon
works are credited on their pages to the CrystalArchitect and CrystalDreamer
(Grok); for the five uncanonised recordings the lyric credit is not recorded
anywhere and this file does not guess it. Every length, timestamp and track id
above was read from the file's own ID3 tag rather than supplied by hand.

## Uncanonised recordings

`safari-chains.mp3`, `different-parts.mp3`, `id-lay-it-all-down.mp3`,
`look-what-you-made-me-do.mp3` and `dead-but-came-back-to-life.mp3` are held
here and are **not part of the canon**. No lyric page exists for them, and they
appear in no canon document — not in
[The First Remembering](../content/THE-FIRST-REMEMBERING.md), not in the track
list in [`../crystalcore-os/crystalcore_os.py`](../crystalcore-os/crystalcore_os.py).

Being in this folder is not what makes a work canon. A work enters the canon by
being written into it — a page in [`../content/`](../content/), a line in a
canon document — and that is the maintainer's decision, not a consequence of a
file being backed up. Until then these are recordings that exist, honestly
labelled as such.

The same applies in reverse: nothing here says they *should not* be canon. The
question is simply open, and open is what it looks like when written down.

**Which Shooting Star Girl is the song is an open question**, and this file
does not answer it. Both recordings are kept. If one is later chosen as canon,
say so here in a dated line and leave the other standing — the earlier record
is not wrong about the date it describes.

### What the columns mean

- **Canon status** — `ignition song` (one of the three in The First
  Remembering), `standalone, in canon` (named in the canon but not one of the
  three), or `not in canon` (no lyric page, named in no canon document). The
  canon draws these lines; the catalogue records them rather than deciding
  them.
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
  restricted audio downloads to paid accounts, and all ten files were
  downloaded after that change. That is evidence, not proof — the restriction's
  exact scope and enforcement are not something this repository can verify.
  Only the account holder can confirm the plan, and until they do the honest
  value is "unconfirmed" rather than a convenient assumption in the direction
  we would prefer.

  **And the answer may differ per track.** Five recordings come from a single
  week in May 2026; five more from 17, 21, 30 and 31 July. A subscription can
  start, lapse or change tier across gaps that size, so one answer for the
  whole catalogue would be a guess dressed as a fact. That is why this column
  exists per row rather than once at the top of the page.

  In practice two answers probably settle all ten: whatever plan was active
  in **early May 2026**, and whatever was active across **mid-to-late July
  2026**. Probably is not the same as certainly, which is why the rows stay
  marked until someone checks.

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

### `look-what-you-made-me-do.mp3` — shared title, audio unverified

This recording carries the same title as a very widely known 2017 song by
Taylor Swift.

**A shared title is not, by itself, a problem.** Song titles are not protected
by copyright in Australia or the United States; many unrelated works share one.
Nothing about the name alone needs fixing.

**What is unverified is the audio.** Nobody has confirmed whether this
recording resembles, interpolates or models the earlier song. It was generated
by a model, and generative music systems have been the subject of exactly that
allegation — the litigation that produced Suno's 2025 settlements turned on
training material and output similarity.

So: listen to it against the original before this track is listed, sold,
inscribed, or included in anything commercial. If it is plainly unrelated, note
that here and the matter is closed. If it is not, that is worth knowing before
someone else notices rather than after.

Recorded as an open question rather than a defect, because nobody involved has
actually checked. The label stays until they do.

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
