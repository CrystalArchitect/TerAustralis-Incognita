# Repository principles

The rules that keep this repository legible as it grows. They bind every
contributor, human or AI.

1. **Documentation is not executable code.** `src/` holds only code;
   explanations live in `docs/`. A README may sit beside its component; a
   spec goes in `docs/architecture/`.
2. **Research is not production software.** `research/` explores freely and
   ships nothing. Promotion into `src/` is a deliberate act with review and,
   where structural, an ADR.
3. **Preserve historical material in the archive.** Superseded work moves to
   `archive/` rather than vanishing — provenance matters. Nothing there is
   maintained; never build on it.
4. **Record major architectural decisions.** Structural or hard-to-reverse
   choices get an ADR in [`docs/adr/`](../adr/) — see
   [`Decision-Records.md`](Decision-Records.md).
5. **Significant changes are reviewed before merging.** Branch, PR, green
   CI, maintainer merge — see [`Review-Process.md`](Review-Process.md).
6. **Keep code, documentation, research, and story clearly separated.** The
   mythos (`mythos/`) is Vision-layer content under its own license; it may
   point at code and never speaks for it.
7. **Favor reproducibility and clear evidence.** A claim about the software
   should come with the command that proves it (the self-tests, the test
   suites); a claim without one is labeled as vision, not fact.

Principles 6 and 7 are this repo's oldest law restated — the Belt-Three
labels ([`CONTRIBUTING.md`](../../CONTRIBUTING.md)) and the
[Incognita Rule](The-Incognita-Rule.md): mark which lines are dreamed and
which are surveyed, and never let a dreamed line pretend it was measured.

Two structural corollaries, adopted with the v1.0 architecture
([`ADR-0001`](../adr/ADR-0001.md)): the repository root stays lean (licenses,
top-level guides, and entry points only), and every directory with a
non-obvious purpose carries a README saying what belongs in it.
