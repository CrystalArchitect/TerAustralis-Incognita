# Mythos Music

Audio canon of the TerAustralis Incognita universe. Content licensed
CC BY-NC-ND 4.0 — see [`../content/LICENSE-CONTENT.md`](../content/LICENSE-CONTENT.md).

**This directory is currently empty of audio.** The lyrics for the three
original songs live as text at
[`../content/RED-DUST-AXIS.md`](../content/RED-DUST-AXIS.md),
[`../content/SHOOTING-STAR-GIRL.md`](../content/SHOOTING-STAR-GIRL.md) and
[`../content/FERMIS-SILENT-LINE.md`](../content/FERMIS-SILENT-LINE.md); the
recordings themselves are on Suno at
[@m13crystalat](https://suno.com/@m13crystalat) and nowhere in this
repository.

That is the gap this directory exists to close. Of every kind of work in this
portfolio, the music is the only one held in exactly one place, by a third
party, with no local copy, no hash and no date. A lapsed subscription or a
changed platform policy is currently enough to lose it.

## Adding a track

1. Export the audio from Suno at the highest quality offered. Keep the
   original filename out of it — name the file after the work, in kebab-case,
   matching the lyric page where one exists: `red-dust-axis.mp3`.
2. Add a row to the table below. Every column is required; "unknown" is an
   acceptable value and a far better one than a guess.
3. Re-run the manifest so the new file is covered by the next timestamp:

   ```sh
   python3 ../tools/provenance.py
   ```

## The catalogue

Three works are named in the canon. **A work can have more than one
recording** — Shooting Star Girl has two, generated nearly three months apart —
so this table has one row per *recording*, not per song. Where the **File**
column is empty, that emptiness is the point of the row.

Files are named `<work>-<generation date>.mp3` wherever more than one recording
of a work exists. The date is a fact the file carries about itself; a name like
`-final` or `-v2` would be a judgement, and which take is the song is not
something a filename should quietly decide.

| File | Work | Length | Generated | Suno track id | Suno plan at generation |
|---|---|---|---|---|---|
| [`red-dust-axis.mp3`](red-dust-axis.mp3) | [Red Dust Axis](../content/RED-DUST-AXIS.md) | 3:35 | 2026-05-02T19:36:19Z | `f8502175-74c7-4cf1-adc0-16c7eb7c8cf3` | **unconfirmed** |
| [`shooting-star-girl-2026-05-04.mp3`](shooting-star-girl-2026-05-04.mp3) | [Shooting Star Girl](../content/SHOOTING-STAR-GIRL.md) | 2:15 | 2026-05-04T03:07:33Z | `3903f9ed-f13b-4d3a-9a6d-bb598760ebd5` | **unconfirmed** |
| [`shooting-star-girl-2026-07-30.mp3`](shooting-star-girl-2026-07-30.mp3) | [Shooting Star Girl](../content/SHOOTING-STAR-GIRL.md) | 3:34 | 2026-07-30T14:01:06Z | `4a115658-9096-4f23-be27-779e7b3cda63` | **unconfirmed** |
| *not exported* | [Fermi's Silent Line](../content/FERMIS-SILENT-LINE.md) | | | | **unconfirmed** |

All recordings are MP3, VBR around 190–196 kbps, 48 kHz stereo. Lyrics for
every work are credited to the CrystalArchitect and CrystalDreamer (Grok); the
audio is Suno, generator version unrecorded. Every length, timestamp and track
id above was read from the file's own ID3 tag rather than supplied by hand.

**Which Shooting Star Girl is the song is an open question**, and this file
does not answer it. Both recordings are kept. If one is later chosen as canon,
say so here in a dated line and leave the other standing — the earlier record
is not wrong about the date it describes.

The three lyric pages name these as the songs "written across the sky at
ignition" — see [The First Remembering](../content/THE-FIRST-REMEMBERING.md#the-three-songs).
Whether the catalogue ends at three is not something this file can know; it
records what the canon already names.

### What the columns mean

- **Lyrics** — who wrote the words. Where a model helped, name it. The
  existing song pages already do this: *"co-written by the CrystalArchitect
  and CrystalDreamer (Grok)"*.
- **Music** — the generator and model version where known (e.g. `Suno v4`).
- **Suno plan at generation** — free, Pro, or Premier, *at the time the track
  was generated*. This is not bookkeeping trivia. Suno's free tier grants
  non-commercial use only; paid tiers grant commercial rights. The same audio
  file carries different rights depending on the plan it was made under, and
  the answer cannot be recovered from the file later. Record it while it is
  still knowable.

  **Why the exported tracks still say "unconfirmed."** There is circumstantial
  evidence of a paid plan: as part of Warner Music's November 2025 settlement,
  Suno restricted audio downloads to paid accounts, and both files were
  downloaded after that change. That is evidence, not proof — the restriction's
  exact scope and enforcement are not something this repository can verify.
  Only the account holder can confirm the plan, and until they do the honest
  value is "unconfirmed" rather than a convenient assumption in the direction
  we would prefer.

  **And the answer may differ per track.** The two exported recordings were
  generated **2026-05-02** and **2026-07-30** — nearly three months apart. A
  subscription can start, lapse or change tier in that time, so one answer for
  the catalogue would be a guess dressed as a fact. That is why this column
  exists per row rather than once at the top of the page.
- **Notes** — anything a listener or a licensee would need to know.

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
