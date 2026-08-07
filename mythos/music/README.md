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
| [`red-dust-axis.mp3`](red-dust-axis.mp3) | [Red Dust Axis](../content/RED-DUST-AXIS.md) | ignition song | 3:35 | 2026-05-02T19:36:19Z | `f8502175-74c7-4cf1-adc0-16c7eb7c8cf3` | **none — before Pro began 7 May** |
| [`shooting-star-girl-2026-05-04.mp3`](shooting-star-girl-2026-05-04.mp3) | [Shooting Star Girl](../content/SHOOTING-STAR-GIRL.md) | ignition song | 2:15 | 2026-05-04T03:07:33Z | `3903f9ed-f13b-4d3a-9a6d-bb598760ebd5` | **none — before Pro began 7 May** |
| [`wire-skull-memory.mp3`](wire-skull-memory.mp3) | [Wire Skull Memory](../content/WIRE-SKULL-MEMORY.md) | standalone, in canon | 2:16 | 2026-05-07T06:21:02Z | `1a194a77-0d9b-4d93-94f7-7a8388b24de0` | Pro — same day as the 7 May charge |
| [`fermis-silent-line.mp3`](fermis-silent-line.mp3) | [Fermi's Silent Line](../content/FERMIS-SILENT-LINE.md) | ignition song | 4:34 | 2026-05-10T12:53:53Z | `d2563605-d533-4714-98b5-996da3c59cf9` | **Pro** |
| [`safari-chains.mp3`](safari-chains.mp3) | Safari Chains | **not in canon** | 3:14 | 2026-05-10T13:35:54Z | `26833d33-83f3-4606-8fcc-fd96d1ae6058` | **Pro** |
| [`different-parts.mp3`](different-parts.mp3) | Different Parts | **not in canon** | 3:39 | 2026-07-17T08:19:25Z | `ac20f017-f30f-4107-843f-e967f9df0d37` | **none — Pro ended 6 June** |
| [`id-lay-it-all-down.mp3`](id-lay-it-all-down.mp3) | I'd Lay It All Down | **not in canon** | 4:15 | 2026-07-21T14:36:40Z | `4b4a881a-653d-440a-a056-29c3b85f6fa3` | **none — Pro ended 6 June** |
| *removed 2026-07-31* | Look What You Made Me Do — *see truth label* | **not in canon** | 3:52 | 2026-07-21T14:47:48Z | `4d875adf-2547-419e-ac4d-66fa53b729c6` | **none — Pro ended 6 June** |
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
`starline-rivers.mp3` and `dead-but-came-back-to-life.mp3` are held here and
are **not part of the canon**. A sixth, `look-what-you-made-me-do.mp3`, was
also uncanonised and has since been removed — see its truth label. No lyric
page exists for any of them, and they appear in no canon document — not in
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

**Eight recordings are non-commercial.** The six July tracks were generated
after the Pro subscription ended on 6 June 2026, and Red Dust Axis and the
first Shooting Star Girl take were generated before it began on 7 May — see
the plan column and the note below it. Nothing about preservation changes;
what changes is what may be done with them.

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

  **What the records show.** Three screenshots, order-detail receipts pulled
  directly from Apple's purchase history:

  - A subscription page (2026-07-31): **Suno Pro Plan, cancelled, ended
    6 June 2026**.
  - Order `MS2QMWQ5BD`, **7 May 2026, 4:52pm**: Suno Pro Plan, **"Init.
    Subscription"**, $15.00.
  - Order `MS2S00Y490`, **8 Aug 2026, 6:06am**: Suno Pro Plan, "Subscription
    Renewal", $15.00 — the subscription resumed and is renewing monthly as of
    this writing.

  **What that settles.** "Init. Subscription" is Apple's own label for a
  plan's *first* charge, not a renewal — this is not an inference from a time
  window, it is what the receipt itself says. The Pro period therefore began
  on 7 May 2026 and ended 6 June 2026, thirty days later, matching the
  cancellation record. Everything generated in that window was made on a paid
  plan: Wire Skull Memory, Fermi's Silent Line, Safari Chains. Everything
  outside it was not: Red Dust Axis and the first Shooting Star Girl take (both
  before 7 May), and all six July recordings (after 6 June). All five rows in
  the table are resolved; none remain open.

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

### `look-what-you-made-me-do.mp3` — removed 2026-07-31

**The audio has been removed from this repository.** The catalogue row above is
kept, because the recording existed and a record that loses its own history is
not a record.

**What was found.** This file was filed on 2026-07-31 with an open truth label:
it shared its title with a very widely known 2017 song by Taylor Swift, and
nobody had listened to both. A shared title is not itself a problem — titles
carry no copyright, and unrelated works share them constantly. The audio was
the unverified part.

The maintainer listened, the same day, and **confirmed the recording does
relate to the earlier song**. That answers the question the label was raised
to hold open.

**Why removal rather than relabelling.** This repository is public and asserts
CC BY-NC-ND 4.0 over its audio. A Creative Commons licence is a *grant* — it
tells the world it may redistribute the file. Where a recording relates to
someone else's composition, that grant is not the maintainer's to make. The
copyright in *Look What You Made Me Do* sits with its writers, who include the
writers of *I'm Too Sexy* through its interpolation.

That reasoning is independent of any question about whether model-generated
audio attracts copyright of its own. The problem was never what the file is; it
was what publishing it under this licence claimed.

**What was not done.** The file remains in git history, and this repository has
not been rewritten to erase it. Rewriting public history to remove one track
would break the commit the Bitcoin anchor was made against, and would be a
larger act than the situation calls for. Anyone determined can still find the
blob; nothing at `main` serves it, and nothing here licenses it.

**What the anchor says now.** `MANIFEST.sha256.ots` attests the state of this
work on 2026-07-31, when the file was present. That attestation stays true
about that date. The manifest has been regenerated without the file and will be
stamped again; the two proofs sit beside each other, which is what a dated
record is supposed to look like.

**For anything measured rather than heard.** Objective features of the removed
file, for the record: 3:52, roughly 74 BPM, reading as D major. Those diverge
from the earlier song on every axis, which is a useful reminder that tempo and
key comparison cannot detect interpolation. Listening could and did.

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
