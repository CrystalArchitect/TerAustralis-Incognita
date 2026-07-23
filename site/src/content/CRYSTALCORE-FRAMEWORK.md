# The CrystalCore Framework — Local-First Reasoning

> **Status: documented and tested in development; not yet published in this
> repository.** The framework’s own development docs report 126 passing tests, but under
> the [status ladder](GOVERNANCE.md) nothing on this page may claim ✅ Built until the code
> is merged to `main` here, where anyone can run those tests themselves. Until then, every
> capability below carries 🟡 at best. This page exists so the design is visible before the
> code lands, not instead of it.
>
> **Naming note:** this is the third thing to carry the CrystalCore name, and the
> [Lexicon](GLOSSARY.md) holds them apart: *CrystalCore.OS* is the interactive mythos
> terminal; `crystalcore/` in this repository is Lumina’s code; **the CrystalCore
> Framework** — this page — is a standalone reasoning stack. They share a root word and
> nothing else.

## One Paragraph

A minimal framework for reasoning that lives entirely on your own device — a Raspberry Pi,
an older laptop, an embedded board. No cloud dependencies, no external APIs, no ML
frameworks; pure Python standard library. Three properties are enforced mechanically rather
than by policy: **consent** (reasoning fails closed if permission is missing), **coherence**
(a conclusion is never more confident than its weakest input), and **provenance** (every
decision traces back to its sources). It is not trying to be the smartest system. It is
trying to be the most honest, the most auditable, and the most locally owned.

## Four Layers

| Layer | Module | Purpose |
| --- | --- | --- |
| **CrystalMemory** | `crystal_memory.py` | Persistent, consent-aware storage: sparse 8-bit quantized tensors, atomic SHA-256-checksummed persistence safe for microSD and power failures, priority-aware pruning under RAM pressure |
| **CrystalFlow** | `crystal_flow.py` | Reasoning: explicit, named, inspectable symbolic rules (no black-box weights) plus a tiny scalar autograd engine; fails closed on consent, propagates coherence, attaches provenance to every step |
| **CrystalEvolve** | `crystal_evolve.py` | Learning: seeded, deterministic evolution of hybrid genomes (numeric parameters + symbolic rules from a closed registry — no arbitrary code can evolve in), with symbolic validity as a hard gate on fitness |
| **CrystalMind** | `crystal_mind.py` + `policy_rules.py` | Four non-autonomous reasoning stances — TruthSeeker (high evidence bar), Guardian (safety veto), Visionary (marked speculative), Creator (synthesis) — with no background loops; agents act only when invoked |

A fifth, optional layer — **CrystalSensor**, the external-input abstraction — has its own
architecture document and will get its own Archive page. Its core line applies to the whole
stack: *it processes the external world only; the mind is inviolable.*

## The Three Guarantees, Concretely

**Consent, fail-closed.** Every value carries a consent bitmask (bit 0 = user, bit 1 =
family, and so on). If a consumer lacks permission for *any* required input, the reasoning
step refuses and logs the denial. A confident conclusion must never be built on forbidden
data.

**Coherence, bounded.** Output confidence = min(input confidences) × rule strength. If the
device state is known at 0.99 but the permission record is an older 0.85, a 0.95-strength
rule yields 0.80 — never more. The system cannot claim certainty its inputs don’t support.

**Provenance, complete.** Conclusions form a directed acyclic graph back to their sources.
“Turn on the kitchen lights” walks back to the user’s command, the device state, the named
rule, and the Guardian’s approval — a chain a human can read.

The Guardian’s veto is the safety mechanism tying these together: it inspects a conclusion’s
*actual* coherence chain (not its self-report), removes unsound conclusions from memory, and
logs every veto for human review.

## What the Development Suite Reports

Per the framework’s own docs — **to be re-verified here when the code lands**: 126 tests
across the stack (33 memory, 22 flow, 24 evolve, 17 mind, 15 policy rules, 8 sensor, 7
property-based invariants), stdlib-only test runner, with cross-cutting properties checked
under randomized inputs: no forbidden data leaks, coherence never exceeds the weakest input,
high-priority data survives pruning, payloads round-trip without corruption, evolution is
deterministic, provenance chains are acyclic. Target envelope: Raspberry Pi 4/5, under
256 MB working set, ARM64, pure Python.

## What It Is NOT

Not a large language model. Not cloud-based. Not a chatbot. Not autonomous — agents act only
when invoked. Not a brain-reading system — it never touches neural signals. Not a replacement
for human judgment — the Guardian and the human can always override. Not magic — pure
mathematics, fully inspectable.

## Planned, Honestly Marked ⬜

A Wisdom Layer (inspectable, consent-flagged knowledge sources — never hardcoded belief),
CrystalAudit (exportable decision reports), CLI and simple web UI, and automated Raspberry Pi
packaging. All Design. None built.

## Path to Publication

- [ ] Framework source merged to this repository through a reviewed pull request
- [ ] Test suite runnable here: `python3 run_tests.py`
- [ ] Per-layer status markers assigned against code on `main`
- [ ] CrystalSensor page published alongside

When those boxes tick, this page’s status line changes. Not before.

---

*See also: [GLOSSARY.md](GLOSSARY.md) (the three CrystalCores, held apart) ·
[GOVERNANCE.md](GOVERNANCE.md) (why this page can’t say Built yet) · [LUMINA.md](LUMINA.md)
(the companion, a separate system)*

*Part of The Crystal Vision · TerAustralis Incognita · Non Solus — Not Alone*
