# Connecting a guest to CrystalBridge

## Run the meeting-house (stdio)

```powershell
cd C:\Users\cryst\.grok\downloads\TeraAustralis-Incognita
$env:CRYSTALBRIDGE_GUEST = "grok"
$env:PYTHONPATH = (Get-Location).Path
& "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe" -m crystalcore.bridge --profile default
```

Or: `.\scripts\run-bridge.ps1 -Guest grok`

## Grok CLI MCP config

Configured in `~/.grok/config.toml` as server `crystalbridge` with `CRYSTALBRIDGE_GUEST=grok`.

## Approve / restrict guests

Edit `profiles/<name>/bridge_config.json`.

## Tests

```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe" -m pytest tests -v
```
