# Canon Sync Pipeline

## Overview

The CrystalCore canon (mythos content) lives in the umbrella repository (`TerAustralis-Incognita`) and is published through the Code repository (`TerAustralis-Incognita-Code`). This script automates syncing changed files from `mythos/` to the Code repo's `vision/site/src/content/`, eliminating the manual copy bottleneck.

## How It Works

1. **Source Tracking**: The script reads `.canon-source` in the Code repo's content directory to determine the last synced commit.
2. **Change Detection**: It uses `git diff` to identify markdown files in `mythos/` that changed since the last sync commit.
3. **File Copy**: Changed files are copied from `mythos/` to `vision/site/src/content/` (flattened to root).
4. **Marker Update**: The `.canon-source` file is updated with the new umbrella commit hash.
5. **Auto-Commit**: Optionally commits the synced files to the Code repo with attribution.

## Usage

### Manual Sync (no auto-commit)
```bash
python3 scripts/sync_canon_to_code.py
```

### Sync with Auto-Commit
```bash
python3 scripts/sync_canon_to_code.py --commit
```

### First Sync / Full Resync
On first run (or if `.canon-source` is missing), the script performs a full sync of all markdown files in `mythos/`.

## Integration Points

### GitHub Actions (Recommended)
To automate on every commit to the umbrella repo's main branch, add a workflow to `.github/workflows/sync-canon.yml` in the umbrella repo:

```yaml
name: Sync Canon to Code

on:
  push:
    branches: [main]
    paths:
      - 'mythos/**/*.md'

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          repository: CrystalArchitect/TerAustralis-Incognita
          fetch-depth: 2

      - name: Sync canon to Code repo
        run: |
          python3 scripts/sync_canon_to_code.py --commit
        env:
          GIT_AUTHOR_NAME: "Claude Code Bot"
          GIT_AUTHOR_EMAIL: "noreply@anthropic.com"

      - name: Push to Code repo
        run: |
          cd /home/user/TerAustralis-Incognita-Code
          git push origin main
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Local Pre-Commit Hook
To sync before committing changes to the umbrella repo, add to `.git/hooks/pre-commit`:

```bash
#!/bin/bash
python3 scripts/sync_canon_to_code.py --commit
```

### Scheduled Sync (Cron)
To sync daily at a fixed time, add to the system crontab:

```cron
0 09 * * * cd /home/user/TerAustralis-Incognita && python3 scripts/sync_canon_to_code.py --commit
```

## Marker File

The `.canon-source` file in the Code repo's content directory tracks the source commit:

```
d8582a7fd4b4e295e1c102821270d756a042ac91
```

If you need to force a full resync, delete this file and run the script again.

## File Structure

**Source** (umbrella):
```
mythos/
├── crystalcore-os/
│   └── *.py
├── content/
│   ├── APOCRYPHON.md
│   ├── RED-DUST-AXIS.md
│   └── ...
├── teraustralis/
│   ├── publish/
│   └── manifesto.md
└── README.md
```

**Target** (Code repo):
```
vision/site/src/content/
├── .canon-source  (marker)
├── APOCRYPHON.md
├── RED-DUST-AXIS.md
├── manifesto.md
└── ...
```

All files are flattened to the content root (directory structure from mythos/ is not preserved).

## Notes

- **Incremental Sync**: After the first run, only changed files are synced, reducing copy overhead.
- **Git Integration**: Uses `git ls-files` and `git diff` for accurate change detection.
- **Flatten Structure**: Content files lose their subdirectory hierarchy on sync (intentional, for site simplicity).
- **Marker Tracking**: The commit hash in `.canon-source` is the source commit from the umbrella repo, not the synced commit in the Code repo.
