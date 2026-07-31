# Provenance Timestamps — anchoring the work to Bitcoin

**Status:** tooling in place, not yet stamped. The manifest is committed; no
`.ots` proof exists until someone runs the stamping command from a machine
with network access to the OpenTimestamps calendars.

## What problem this solves

This repository can already prove *what* it contains. Git hashes every object,
and the archive's hash-chained audit log makes edits detectable.

Two things it cannot do:

1. **Prove when.** Git commit dates are written by whoever makes the commit
   and can be set to any value. They are a claim, not evidence.
2. **Prove it to someone who does not trust the author.** The whole history
   could be rebuilt from scratch by the person who holds the repository.

For a body of creative work — 140 artworks, three songs, the written canon —
those two gaps are the whole question of priority. *I made this, and I made it
first* is currently a claim resting on the author's word.

Anchoring closes both, for free.

## How it works

[`mythos/tools/provenance.py`](../../mythos/tools/provenance.py) walks the
creative work, hashes every file with SHA-256, and writes one sorted manifest
to `mythos/MANIFEST.sha256`. The manifest is deterministic: the same files
produce a byte-identical manifest on any machine, so anyone can rebuild it and
compare.

That single manifest file is then stamped with
[OpenTimestamps](https://opentimestamps.org), which aggregates it into a
Merkle tree with thousands of other submissions and commits the tree root to
the Bitcoin blockchain. One proof covers every file in the manifest.

**No cryptocurrency is involved.** No wallet, no token, no purchase, no
transaction fee. OpenTimestamps calendars pay the Bitcoin fees themselves and
batch submissions; the service is free to use. This matters here because
[the Ordinals licence grant](ORDINALS-LICENCE-GRANT.md) states plainly that
the project issues no token, and nothing in this scheme contradicts that.

## Running it

Regenerate the manifest whenever the work changes:

```sh
python3 mythos/tools/provenance.py
```

Check that the committed manifest still matches the files (useful in CI, and
it names exactly what drifted):

```sh
python3 mythos/tools/provenance.py --check
```

Stamp it. **This step needs network access to the calendar servers**, which
some sandboxed environments block:

```sh
pip install opentimestamps-client
ots stamp mythos/MANIFEST.sha256
```

That writes `mythos/MANIFEST.sha256.ots`. Commit it beside the manifest.

The proof is *incomplete* for the first hour or so — the calendars return an
attestation immediately but the Bitcoin block it depends on has not been mined
yet. Upgrade it later, once, and commit the result:

```sh
ots upgrade mythos/MANIFEST.sha256.ots
```

Verify at any time:

```sh
ots verify mythos/MANIFEST.sha256.ots
```

`ots verify` needs to check a Bitcoin block header. It will use a local
Bitcoin node if you have one, or fall back to a public block explorer.

## What the proof says, and what it does not

**It says:** these exact bytes existed no later than the time of Bitcoin block
*N*. That is checkable by anyone, forever, without trusting the author, this
repository, GitHub, or any company — including OpenTimestamps itself, whose
job ends once the hash is in a block.

**It does not say:**

- **Who made the work.** A timestamp proves existence, not authorship. Anyone
  can timestamp anything, including someone else's file.
- **That the work is original.** Stamping something copied from elsewhere
  proves only that you had a copy by that date.
- **Anything about the files themselves.** The proof covers the manifest; the
  manifest covers the files by hash. Change one byte of one artwork and that
  file no longer matches — which is the point, but it means the manifest must
  be regenerated and re-stamped after every change to the work.

That last constraint is a feature. Each stamp is a dated snapshot. Keeping the
old `.ots` files alongside the new ones builds a chain of dated states, which
is the same accretion discipline the archive already runs on: the record of
what was true on a date stays standing, and new records are added beside it.

## What is covered

The roots are listed at the top of
[`provenance.py`](../../mythos/tools/provenance.py) — the art, the music, the
written canon, the covenant and the names. Build output, dependencies and
generated site trees are deliberately excluded: they are derived from the
sources and would make the manifest churn on every rebuild while proving
nothing about authorship.

Adding a new kind of work means adding its path to `ROOTS`, regenerating and
re-stamping.

## A note on what this is for

Where the work is model-generated — and much of the art and all of the audio
is — copyright may not attach to it at all, since copyright generally requires
a human author. A timestamp does not fix that, and should not be mistaken for
a substitute.

What it does is narrower and still worth having: it establishes that this
particular body of work, in this particular arrangement, existed on a date.
For a project whose value is the coherence of a canon rather than the
exclusivity of any single file, that is the relevant fact to be able to prove.

---

*Not legal advice. This document describes what a cryptographic timestamp
demonstrates, which is a narrower thing than a legal claim to a work.*
