# GitHub Commit Instructions

A short quick-reference for getting a change committed cleanly. The full rules
live in [`CONTRIBUTING.md`](CONTRIBUTING.md) — read that first; this page just
collects the commands.

This is a single monorepo (`CrystalArchitect/teraaustralis-incognita`), not a
flat collection of files. Everything below runs from the repo root.

## One-time setup

```bash
git clone https://github.com/CrystalArchitect/TeraAustralis-Incognita.git
cd TeraAustralis-Incognita
```

## Before you push: run the checks CI runs

CI (`.github/workflows/ci.yml`) runs on every push and pull request, and its
"Python syntax + self-tests" job must pass. Run the same checks locally first:

```bash
# Python syntax across the source tree
python -m compileall -q apps/clementine crystal-core crystalcore node tests _archive

# Self-tests (from crystal-core/)
cd crystal-core
python -m clementine.bridge.selftest      # Starline Weaver
python -m services.selftest               # Decode → Ingest → Twin pipeline
pip install -r requirements-consenttransport.txt
python -m consent_transport.selftest      # Consent Transport
cd ..
```

If you changed the website, build it too:

```bash
cd site && npm install && npm run build && cd ..
```

## Commit and open a PR

Direct pushes to `main` are the maintainer's; everyone else works on a branch
and opens a pull request (see [`CONTRIBUTING.md`](CONTRIBUTING.md)):

```bash
git checkout -b your-feature-branch
git add path/to/changed/files          # stage specifically, not `git add -A`
git commit -m "Clear, present-tense summary of the change"
git push -u origin your-feature-branch
```

Then open a pull request against `main` on GitHub. CI runs automatically — get
it green before merging.

## Never commit

Enforced by `.gitignore`, but worth knowing (the full list is in
[`CONTRIBUTING.md`](CONTRIBUTING.md)):

- **Generated output** — `.svelte-kit/`, `site/build/`, `dist/`, `node_modules/`,
  `__pycache__/`
- **Personal data** — Lumina memory and profiles, Consent Transport identity/keys,
  CrystalBridge audit logs
- **Secrets** — API keys, `.env` files

*Non Solus.*
