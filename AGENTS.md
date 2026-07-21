# AGENTS.md — TeraAustralis-Incognita

## Project

Living vision stack: **TeraAustralis Incognita** · **CrystalVision** · **CrystalCore.Lattice**.

## Canon law

1. Read `CONSTITUTION.md` before large changes.  
2. Disk is canon > chat.  
3. Substantial work → commit it, honestly labeled (Built/Vision). The
   `CrystalCore.Lattice/memory/deltas/` convention this used to point to was
   never built — see `CONSTITUTION.md`'s implementation note.  
4. New AI tool used → note it in your PR description for now; `WEAVE_MAP.md`
   doesn't exist yet.  
5. Cultural respect: no false sacred; fire-circle ethic.  

## Layout

- `TeraAustralis/` — outer world lore + publish  
- `CrystalVision/` — lens, journal, banners, personas  
- `CrystalCore.Lattice/` — weave, ontology, activation, Ollama Modelfiles  
- `scripts/` — converge, export-corpus, create-crystal-models  
- `corpus/` — generated; do not hand-edit as source of truth  

## Commands

Design intent, not live tooling — `scripts/` doesn't exist in this repo yet,
so none of these run today:

```powershell
.\scripts\converge.ps1
.\scripts\export-corpus.ps1
.\scripts\create-crystal-models.ps1   # after: ollama pull llama3.2
```
