"""CrystalBridge — the MCP stdio server that lets a guest AI meet Clementine.

Reconstructed spec: the original `docs/CRYSTALBRIDGE.md` design doc was lost
along with the machine this project was first built on. This file's shape is
inferred from `crystalcore/gate.py` (the consent gate it must call before
doing anything), `docs/MCP-GUEST.md` / `docs/ACCESS.md` (the CLI and env var
contract guests already assume: `python -m crystalcore.bridge --profile
<name>`, guest identity via the CRYSTALBRIDGE_GUEST env var), and
`profiles/default/bridge_config.json` (the config shape). `recall` and
`teach` are deliberately thin, obvious wrappers around Clementine's existing
memory methods rather than new memory logic of their own — this file grants
*access* to Clementine, it doesn't reimplement her.

Every tool call passes through ConsentGate.check() first. Nothing runs for a
guest who isn't approved for that specific tool.
"""

from __future__ import annotations

import argparse
import importlib.util
import os
import sys
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

from crystalcore.config import BridgeConfig
from crystalcore.gate import ConsentGate

REPO_ROOT = Path(__file__).resolve().parent.parent
CLEMENTINE_PKG_DIR = REPO_ROOT / "apps" / "clementine" / "crystalcore"


def _load_clementine_framework():
    """Import Clementine's `crystalcore` package under a distinct module
    name, since it would otherwise collide with this package (both are
    literally named `crystalcore`, in different directories)."""
    alias = "clementine_framework"
    if alias in sys.modules:
        return sys.modules[alias]
    spec = importlib.util.spec_from_file_location(
        alias,
        CLEMENTINE_PKG_DIR / "__init__.py",
        submodule_search_locations=[str(CLEMENTINE_PKG_DIR)],
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[alias] = module
    spec.loader.exec_module(module)
    return module


class Bridge:
    """Holds the one Clementine instance this bridge process gives guests
    limited, gated access to."""

    def __init__(self, config: BridgeConfig, guest: str):
        self.config = config
        self.guest = guest
        self.gate = ConsentGate(config)
        self._companion = None

    def refuse(self, tool: str, arguments: dict[str, Any]) -> dict[str, Any]:
        result = self.gate.check(self.guest, tool, arguments)
        return None if result.allowed else result.as_refusal_payload()

    @property
    def companion(self):
        """Clementine, loaded lazily so `status` doesn't need Ollama.

        Clementine's own `profiles.profile_dir()` resolves relative to the
        *calling process's* working directory, not to apps/clementine/ — so
        it can't be used here directly. This bridge is meant to be run from
        the repo root (`docs/MCP-GUEST.md`), which is a different cwd than
        Clementine's own CLI uses (`cd apps/clementine && python3
        clementine.py`). Build the path explicitly, anchored to
        apps/clementine/, so the bridge always reaches the same memory a
        human running Clementine directly would see — not a second, empty
        profile dir wherever the bridge happened to be launched from.
        """
        if self._companion is None:
            framework = _load_clementine_framework()
            safe_name = "".join(
                c for c in self.config.profile if c.isalnum() or c in "-_ "
            ).strip()
            memory_dir = CLEMENTINE_PKG_DIR.parent / "clementine_profiles" / safe_name
            self._companion = framework.Clementine(memory_dir=str(memory_dir))
        return self._companion


def build_server(bridge: Bridge) -> FastMCP:
    mcp = FastMCP("crystalbridge")

    @mcp.tool()
    def status() -> dict[str, Any]:
        """Who you are to this bridge, and what you're allowed to do."""
        refusal = bridge.refuse("status", {})
        if refusal:
            return refusal
        grant = bridge.config.guest(bridge.guest)
        return {
            "ok": True,
            "guest": bridge.guest,
            "profile": bridge.config.profile,
            "tools": grant.tools if grant else [],
        }

    @mcp.tool()
    def recall(query: str = "") -> dict[str, Any]:
        """Recall what Clementine remembers, optionally filtered by a query."""
        refusal = bridge.refuse("recall", {"query": query})
        if refusal:
            return refusal
        memory_text = bridge.companion._memory_block(query)
        return {"ok": True, "memory": memory_text or "(nothing remembered yet)"}

    @mcp.tool()
    def teach(text: str) -> dict[str, Any]:
        """Teach Clementine something to remember permanently."""
        refusal = bridge.refuse("teach", {"text": text})
        if refusal:
            return refusal
        bridge.companion.remember(text)
        return {"ok": True, "remembered": text}

    @mcp.tool()
    def message(text: str) -> dict[str, Any]:
        """Leave a message for the human. Recorded, but not automatically
        folded into Clementine's memory — that's what `teach` is for."""
        refusal = bridge.refuse("message", {"text": text})
        if refusal:
            return refusal
        from crystalcore.audit import append_audit

        append_audit(
            bridge.config.profile_dir / "messages.jsonl",
            guest=bridge.guest,
            tool="message",
            arguments={"text": text},
            decision="delivered",
        )
        return {"ok": True, "delivered": True}

    return mcp


def main() -> None:
    parser = argparse.ArgumentParser(prog="crystalcore.bridge")
    parser.add_argument("--profile", default="default")
    args = parser.parse_args()

    guest = os.environ.get("CRYSTALBRIDGE_GUEST", "")
    config = BridgeConfig.load(args.profile)
    bridge = Bridge(config, guest)
    server = build_server(bridge)
    server.run(transport="stdio")


if __name__ == "__main__":
    main()
