#!/usr/bin/env python3
"""
Sync Canon from TerAustralis-Incognita (umbrella) to TerAustralis-Incognita-Code.

Copies markdown content from mythos/ to vision/site/src/content/, tracking the
source commit in .canon-source for future incremental syncs.
"""

import os
import sys
import shutil
import subprocess
import json
from pathlib import Path
from datetime import datetime
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s'
)
logger = logging.getLogger("CanonSync")


class CanonSync:
    def __init__(self):
        self.umbrella_repo = Path("/home/user/TerAustralis-Incognita")
        self.code_repo = Path("/home/user/TerAustralis-Incognita-Code")
        self.mythos_source = self.umbrella_repo / "mythos"
        self.content_target = self.code_repo / "vision" / "site" / "src" / "content"
        self.marker_file = self.content_target / ".canon-source"

    def get_current_commit(self, repo_path):
        """Get the current HEAD commit hash for a repository."""
        try:
            result = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                return result.stdout.strip()
        except Exception as e:
            logger.warning(f"Could not get commit hash: {e}")
        return None

    def get_last_sync_commit(self):
        """Read the last synced commit from .canon-source marker."""
        if self.marker_file.exists():
            try:
                with open(self.marker_file) as f:
                    return f.read().strip()
            except Exception as e:
                logger.warning(f"Could not read marker file: {e}")
        return None

    def get_changed_files(self, last_commit):
        """Get files changed since last commit (if available)."""
        if not last_commit:
            # First sync: get all markdown files
            logger.info("No prior sync marker found. Performing full sync.")
            return self.get_all_markdown_files()

        try:
            result = subprocess.run(
                ["git", "diff", f"{last_commit}..HEAD", "--name-only", "--diff-filter=ACMR"],
                cwd=self.umbrella_repo,
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                changed = result.stdout.strip().split("\n") if result.stdout.strip() else []
                # Filter to mythos/ files only
                mythos_files = [f for f in changed if f.startswith("mythos/") and f.endswith(".md")]
                if mythos_files:
                    logger.info(f"Found {len(mythos_files)} changed files since last sync.")
                    return mythos_files
                else:
                    logger.info("No markdown changes in mythos/ since last sync.")
                    return []
        except Exception as e:
            logger.warning(f"Could not get changed files: {e}. Falling back to full sync.")
            return self.get_all_markdown_files()

    def get_all_markdown_files(self):
        """Get all markdown files in mythos/."""
        result = []
        try:
            git_result = subprocess.run(
                ["git", "ls-files", "mythos/", "--", "*.md"],
                cwd=self.umbrella_repo,
                capture_output=True,
                text=True,
                timeout=5
            )
            if git_result.returncode == 0:
                result = [f for f in git_result.stdout.strip().split("\n") if f]
        except Exception:
            pass

        if not result:
            # Fallback: walk the filesystem
            for root, dirs, files in os.walk(self.mythos_source):
                for f in files:
                    if f.endswith(".md"):
                        rel_path = os.path.relpath(os.path.join(root, f), self.umbrella_repo)
                        result.append(rel_path)

        logger.info(f"Found {len(result)} markdown files in mythos/.")
        return result

    def sync_files(self, file_list):
        """Copy files from mythos/ to content target."""
        if not file_list:
            logger.info("No files to sync.")
            return 0

        self.content_target.mkdir(parents=True, exist_ok=True)
        synced = 0

        for rel_path in file_list:
            source = self.umbrella_repo / rel_path

            if not source.exists():
                logger.warning(f"Source file missing: {rel_path}")
                continue

            # Extract filename and flatten to content root
            # (mythos/content/FOO.md -> content/FOO.md; mythos/teraustralis/BAR.md -> content/BAR.md)
            filename = source.name
            target = self.content_target / filename

            try:
                shutil.copy2(source, target)
                logger.info(f"✓ Synced: {rel_path} → {target.relative_to(self.code_repo)}")
                synced += 1
            except Exception as e:
                logger.error(f"✗ Failed to sync {rel_path}: {e}")

        return synced

    def update_marker(self, new_commit):
        """Write the new commit hash to .canon-source."""
        try:
            with open(self.marker_file, "w") as f:
                f.write(new_commit + "\n")
            logger.info(f"Updated canon source marker to {new_commit}")
        except Exception as e:
            logger.error(f"Failed to update marker: {e}")

    def commit_changes_in_code_repo(self, synced_count):
        """Commit the synced files to the Code repo."""
        if synced_count == 0:
            logger.info("No files synced; skipping commit.")
            return False

        try:
            # Stage changes
            subprocess.run(
                ["git", "add", "-A"],
                cwd=self.code_repo,
                capture_output=True,
                timeout=10
            )

            # Check if there are changes to commit
            status = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=self.code_repo,
                capture_output=True,
                text=True,
                timeout=10
            )

            if not status.stdout.strip():
                logger.info("No changes to commit in Code repo.")
                return False

            # Create commit
            message = f"""Sync canon from TerAustralis-Incognita umbrella ({synced_count} files)

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015E8rd6Jr9RQWLfjqayjXyA
"""
            subprocess.run(
                ["git", "commit", "-m", message],
                cwd=self.code_repo,
                capture_output=True,
                timeout=10
            )
            logger.info("✓ Committed canon sync to Code repo.")
            return True
        except Exception as e:
            logger.error(f"Failed to commit in Code repo: {e}")
            return False

    def run(self, auto_commit=False):
        """Execute the full sync workflow."""
        logger.info("=== CrystalCore Canon Sync Started ===")
        logger.info(f"Source: {self.mythos_source}")
        logger.info(f"Target: {self.content_target}")

        # Get commit hashes
        umbrella_commit = self.get_current_commit(self.umbrella_repo)
        if not umbrella_commit:
            logger.error("Could not determine umbrella repo commit. Aborting.")
            return False

        last_sync_commit = self.get_last_sync_commit()
        logger.info(f"Last sync was at: {last_sync_commit or 'NEVER'}")
        logger.info(f"Current umbrella commit: {umbrella_commit}")

        # Get files to sync
        files_to_sync = self.get_changed_files(last_sync_commit)

        # Sync files
        synced_count = self.sync_files(files_to_sync)

        # Update marker
        if synced_count > 0 or not last_sync_commit:
            self.update_marker(umbrella_commit)

        # Optionally commit
        if auto_commit:
            self.commit_changes_in_code_repo(synced_count)

        logger.info(f"=== Sync Complete: {synced_count} files synced ===")
        return True


if __name__ == "__main__":
    auto_commit = "--commit" in sys.argv
    sync = CanonSync()
    success = sync.run(auto_commit=auto_commit)
    sys.exit(0 if success else 1)
