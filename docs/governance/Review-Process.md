# Review process

How a change becomes canon. Short version: branch → PR → green CI → review →
maintainer merges.

## The path

1. **Branch.** Direct pushes to `main` are reserved for the maintainer;
   everyone else (human or AI) works on a branch.
2. **Open a pull request** against `main`. The template asks for three
   things: what changed, the Belt-Three label of the change (Science /
   Story / Vision), and which AI tools assisted.
3. **CI must pass** (`.github/workflows/ci.yml`):
   - `python -m compileall -q src tests archive` — syntax across the tree
   - the crystal-core self-tests: `clementine.bridge.selftest`,
     `services.selftest`, `starline.selftest`, `rdp.selftest`
   - `pytest src/apps/lumina/tests` and `pytest tests`
   Run the same checks locally first: `scripts/maintenance/check.sh`
   (details in
   [`docs/guides/GitHub-Commit-Instructions.md`](../guides/GitHub-Commit-Instructions.md)).
4. **Review.** Significant changes are reviewed before merging
   ([`Repository-Principles.md`](Repository-Principles.md) §5). Reviewers
   check the honesty of labels as seriously as the correctness of code —
   docs that outpace code fail review.
5. **Merge.** The maintainer (Crystal, `@CrystalArchitect` — see
   `.github/CODEOWNERS`) merges. For Constitution amendments, the merge is
   itself the §8 sign-off.

## What review looks for

- **Correctness with evidence** — tests or self-tests covering the claim.
- **Label honesty** — Built things demonstrated, Vision things marked.
- **Separation** — code in `src/`, docs in `docs/`, exploration in
  `research/`, story in `mythos/`.
- **Hygiene** — no generated files, no secrets, no personal data
  ([`Development-Standards.md`](Development-Standards.md)).
- **Structure** — a structural change carries its ADR.

## Website changes

`src/site/` deploys to GitHub Pages on merge to `main`
(`.github/workflows/deploy.yml`). If you touched the site, build it locally
(`cd src/site && npm install && npm run build`) before asking for review.
