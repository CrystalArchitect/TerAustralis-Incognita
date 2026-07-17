# Access & Invite List

**Repo (private):** https://github.com/CrystalArchitect/TeraAustralis-Incognita  
**Local path:** `C:\Users\cryst\.grok\downloads\TeraAustralis-Incognita`  
**Keeper:** Crystal (CrystalArchitect)

---

## How people get in

| Audience | Path | What they get |
|----------|------|----------------|
| **You** | Local disk + Ollama + Bridge | Full house |
| **Guest AIs** | MCP CrystalBridge (gate) | status / recall / teach / messages only |
| **Human collaborators** | GitHub invite (private repo) | Clone/browse lore + code; **not** your private Ollama memory unless shared |
| **Public** | Not yet | Only what you publish |

---

## GitHub collaborator invites (human)

1. Open: https://github.com/CrystalArchitect/TeraAustralis-Incognita/settings/access  
2. **Add people** → enter GitHub username or email  
3. Permission: **Read** (lore readers) or **Write** (builders)

### Invite roster (fill in)

| GitHub user / email | Role | Permission | Invited? | Notes |
|---------------------|------|------------|----------|-------|
| _example: teammate_ | builder | Write | ⬜ | |
| _example: advisor_ | reader | Read | ⬜ | |

**Rule:** only invite people you trust with the private vision stack. Guests of the *meeting-house* are AIs via MCP, not this table.

---

## Grok MCP (guest AI access) — wired

User config `~/.grok/config.toml` and project `.grok/config.toml`:

- Server name: **crystalbridge**
- Guest id: `CRYSTALBRIDGE_GUEST=grok`
- Command: Python `-m crystalcore.bridge --profile default`

**New Grok sessions** pick up MCP after config change (restart CLI if tools missing).

```powershell
grok mcp list
# Tools should include crystalbridge__status, __recall, __teach, etc.
```

---

## Claude / Cursor guests

Same MCP command pattern as Grok; set:

```
CRYSTALBRIDGE_GUEST=claude   # or cursor
PYTHONPATH=C:\Users\cryst\.grok\downloads\TeraAustralis-Incognita
```

Approve them in `profiles/default/bridge_config.json`.

---

## Quick links

- Design: `docs/CRYSTALBRIDGE.md`
- Guest wiring: `docs/MCP-GUEST.md`
- Clementine core: `Clementine/`
- Boot Lattice: `.\scripts\boot-lattice.ps1`
