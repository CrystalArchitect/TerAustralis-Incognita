# AGENTS.md — TeraAustralis-Incognita

## Project

Living vision stack: **TeraAustralis Incognita** · **CrystalVision** · **CrystalCore.Lattice**.

## Canon law

1. Read `CONSTITUTION.md` before large changes.  
2. Disk is canon > chat.  
3. Substantial work → Lattice delta in `CrystalCore.Lattice/memory/deltas/`.  
4. New AI tool used → add to `CrystalCore.Lattice/WEAVE_MAP.md`.  
5. Cultural respect: no false sacred; fire-circle ethic.  

## Layout

- `TeraAustralis/` — outer world lore + publish  
- `CrystalVision/` — lens, journal, banners, personas  
- `CrystalCore.Lattice/` — weave, ontology, activation, Ollama Modelfiles  
- `scripts/` — converge, export-corpus, create-crystal-models  
- `corpus/` — generated; do not hand-edit as source of truth  

## Commands

```powershell
.\scripts\converge.ps1
.\scripts\export-corpus.ps1
.\scripts\create-crystal-models.ps1   # after: ollama pull llama3.2
```
