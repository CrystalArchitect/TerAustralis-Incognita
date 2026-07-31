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
[`../MANIFEST.sha256`](../MANIFEST.sha256) — along with six recordings the
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

**Six further recordings exist that the canon does not name as songs.** They
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
| [`red-dust-axis.mp3`](red-dust-axis.mp3) | [Red Dust Axis](../content/RED-DUST-AXIS.md) | ignition song | 3:35 | 2026-05-02T19:36:19Z | `f8502175-74c7-4cf1-adc0-16c7eb7c8cf3` | Pro — *subject to start date* |
| [`shooting-star-girl-2026-05-04.mp3`](shooting-star-girl-2026-05-04.mp3) | [Shooting Star Girl](../content/SHOOTING-STAR-GIRL.md) | ignition song | 2:15 | 2026-05-04T03:07:33Z | `3903f9ed-f13b-4d3a-9a6d-bb598760ebd5` | Pro — *subject to start date* |
| [`wire-skull-memory.mp3`](wire-skull-memory.mp3) | [Wire Skull Memory](../content/WIRE-SKULL-MEMORY.md) | standalone, in canon | 2:16 | 2026-05-07T06:21:02Z | `1a194a77-0d9b-4d93-94f7-7a8388b24de0` | Pro — *subject to start date* |
| [`fermis-silent-line.mp3`](fermis-silent-line.mp3) | [Fermi's Silent Line](../content/FERMIS-SILENT-LINE.md) | ignition song | 4:34 | 2026-05-10T12:53:53Z | `d2563605-d533-4714-98b5-996da3c59cf9` | Pro — *subject to start date* |
| [`safari-chains.mp3`](safari-chains.mp3) | Safari Chains | **not in canon** | 3:14 | 2026-05-10T13:35:54Z | `26833d33-83f3-4606-8fcc-fd96d1ae6058` | Pro — *subject to start date* |
| [`different-parts.mp3`](different-parts.mp3) | Different Parts | **not in canon** | 3:39 | 2026-07-17T08:19:25Z | `ac20f017-f30f-4107-843f-e967f9df0d37` | **none — Pro ended 6 June** |
| [`id-lay-it-all-down.mp3`](id-lay-it-all-down.mp3) | I'd Lay It All Down | **not in canon** | 4:15 | 2026-07-21T14:36:40Z | `4b4a881a-653d-440a-a056-29c3b85f6fa3` | **none — Pro ended 6 June** |
| [`look-what-you-made-me-do.mp3`](look-what-you-made-me-do.mp3) | Look What You Made Me Do — *see truth label* | **not in canon** | 3:52 | 2026-07-21T14:47:48Z | `4d875adf-2547-419e-ac4d-66fa53b729c6` | **none — Pro ended 6 June** |
| [`starline-rivers.mp3`](starline-rivers.mp3) | Starline Rivers — *shares its name with canon art* | **not in canon** | 4:24 | 2026-07-21T22:34:18Z | `0e15fcf9-4291-4de8-8418-7b4348c7fc52` | **none — Pro ended 6 June** |
| [`shooting-star-girl-2026-07-30.mp3`](shooting-star-girl-2026-07-30.mp3) | [Shooting Star Girl](../content/SHOOTING-STAR-GIRL.md) | ignition song | 3:34 | 2026-07-30T14:01:06Z | `4a115658-9096-4f23-be27-779e7b3cda63` | **none — Pro ended 6 June** |
| [`dead-but-came-back-to-life.mp3`](dead-but-came-back-to-life.mp3) | Dead But Came Back to Life | **not in canon** | 3:20 | 2026-07-31T04:29:35Z | `834e6d98-dfc7-46da-8cbb-210876379c00` | **none — Pro ended 6 June** |

Rows are in generation order. Two working periods show up in it: **2–10 May
2026**, five recordings in nine days — Safari Chains arriving forty minutes
after Fermi's Silent Line on the same afternoon — and then **17, 21, 30 and 31
July**. The 21st alone produced three: two eleven minutes apart in the
afternoon, one late that evening. The last recording of all was generated on
the morning this directory was created.

All recordings are MP3, VBR between roughly 178 and 196 kbps, 48 kHz stereo.
The audio is Suno, generator version unrecorded. Lyrics for the four canon
works are credited on their pages to the CrystalArchitect and CrystalDreamer
(Grok); for the six uncanonised recordings the lyric credit is not recorded
anywhere and this file does not guess it. Every length, timestamp and track id
above was read from the file's own ID3 tag rather than supplied by hand.

## Uncanonised recordings

`safari-chains.mp3`, `different-parts.mp3`, `id-lay-it-all-down.mp3`,
`look-what-you-made-me-do.mp3`, `starline-rivers.mp3` and
`dead-but-came-back-to-life.mp3` are held here and are **not part of the
canon**. No lyric page exists for them, and they appear in no canon document —
not in
[The First Remembering](../content/THE-FIRST-REMEMBERING.md), not in the track
list in [`../crystalcore-os/crystalcore_os.py`](../crystalcore-os/crystalcore_os.py).

**One of them is a near miss worth naming.** `starline-rivers.mp3` shares its
title with [`starline-rivers.jpeg`](../art/starline-rivers.jpeg), which *is*
canon art — *"the starline rivers, light flowing between crystal cities across
the dark country."* Starline is also one of this project's own coinages rather
than a borrowed word. So the name is canon; the song is not. Those are
different facts and the table keeps them apart, but a later reader should see
the connection rather than have to notice it.

Being in this folder is not what makes a work canon. A work enters the canon by
being written into it — a page in [`../content/`](../content/), a line in a
canon document — and that is the maintainer's decision, not a consequence of a
file being backed up. Until then these are recordings that exist, honestly
labelled as such.

The same applies in reverse: nothing here says they *should not* be canon. The
question is simply open, and open is what it looks like when written down.

**Six recordings are very likely non-commercial.** The July tracks were
generated after the Pro subscription ended on 6 June 2026 — see the plan
column and the note below it. That includes both `starline-rivers.mp3` and the
later Shooting Star Girl take. Nothing about preservation changes; what changes
is what may be done with them.

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
- **Suno plan** — which plan was running *at the time the track was
  generated*. This is not bookkeeping trivia. Suno's free tier grants
  non-commercial use only; paid tiers grant commercial rights. The same audio
  file carries different rights depending on the plan it was made under, and
  the answer cannot be recovered from the file later. Record it while it is
  still knowable.

  **What is now known.** A subscription screenshot dated 2026-07-31 shows a
  **Suno Pro Plan, cancelled, ended 6 June 2026**. That splits the catalogue:

  - The **five May recordings** (2nd to 10th) fall before the cutoff. Whether
    they fall *inside* the Pro period depends on when it started, which the
    screenshot does not show. If billing ran on the 6th, a subscription
    beginning 6 May would leave the 2nd and 4th outside it. Marked
    *subject to start date* rather than resolved.
  - The **six July recordings** (17th onward) were generated with **no Pro
    subscription running**. On the free tier Suno grants non-commercial use
    only. Unless a separate licence covers them, these six should not be sold,
    inscribed or licensed commercially.

  **A retraction.** An earlier version of this file argued that all the
  recordings were probably made on a paid plan, reasoning that Suno restricted
  downloads to paid accounts after Warner Music's November 2025 settlement and
  every file here was downloaded after that change.

  That inference is now falsified by the evidence above: six recordings were
  generated with no Pro subscription and were downloaded anyway. Whatever the
  download restriction actually covers, it is not the clean signal that
  argument treated it as. The conclusion it pointed toward — *probably paid* —
  was also wrong for those six, and in the direction that would have been
  convenient. It is retracted here rather than deleted, because a record that
  quietly loses its own mistakes is not a record.

  **Still unresolved:** the Pro subscription's *start* date, which is the only
  thing standing between the five May recordings and a settled answer. It is
  visible in Apple's subscription history or Suno's billing page.

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
