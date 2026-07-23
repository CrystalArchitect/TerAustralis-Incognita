# CrystalSensor — The External Input Layer

> **Status: documented and designed; implementation pending repository integration.** The architecture PDFs describe a module (crystal_sensor.py, ~200 lines, stdlib-only), test suite (~250 lines, 8 tests), and end-to-end example (~300 lines). Under the [status ladder](GOVERNANCE.md), nothing here may claim ✅ Built until the code is merged to this repository's `src/` directory and the test suite runs as part of the main `run_tests.py`. Until then: ⬜ Design.
>
> **On brain-reading:** This page deliberately and repeatedly states what CrystalSensor is NOT — not a Neuralink simulation, not a brain-reading system, not neural surveillance. Read that section carefully. The framework processes only external data: text, audio, environment, device state. No brain signals, ever.

---

## One Paragraph

An optional abstraction layer for CrystalCore that lets external sensory data — user text input, audio, device state, environmental readings — flow into your reasoning pipeline while keeping three guarantees locked in: **consent** (data can only be reasoned about if permission is granted), **provenance** (every sensor reading is tagged with source, confidence, and timestamp), and **sovereignty** (everything runs locally, on your device). The core principle is stated plainly: *This processes the EXTERNAL WORLD only. The mind is inviolable.*

---

## Architecture (Conceptual)

External data (text input, audio, temperature, battery state) → **SensorInputHandler** → **SensorReading** objects (data + consent + provenance) → **CrystalMemory** (SparseTensor storage with CoherenceMetadata) → **CrystalFlow** (reasoning engine reads permitted data, fails closed on denied access) → **CrystalMind/Guardian** (veto layer inspects every step) → **Action** (decision logged with full audit trail).

The diagram in the architecture PDF shows the full chain. Key:

- Every `SensorReading` is tagged with type (AUDIO, TEXT, DEVICE, ENVIRONMENTAL, MOCK_INTENT), raw data, confidence (0.0–1.0), consent bitmask, provenance note, source ID, device ID, timestamp.
- `SensorInputHandler` registers and captures readings. `MockSensors` provides safe, deterministic test versions of each sensor type.
- Reasoning applies named rules over permitted data; fails immediately if `consent_flags & consumer_bitmask == 0`.
- Guardian inspects for soundness (coherence chain holds, inputs still permitted, rule is documented).

---

## What This Is

A clean abstraction for external inputs — audio, text, environment, device state — integrated with consent and provenance. Edge-friendly (runs locally, offline-capable, no ML frameworks). Testable with mocks (no hardware needed to develop). Honest about its limits (transparent about what it is and isn't).

## What This Is NOT (Emphatically)

- **Not a brain-reading system.** No EEG, no neural signals, no mind-reading.
- **Not a Neuralink simulation.** We don't mock proprietary tech or pretend we're reading your thoughts.
- **Not an autonomous agent.** Requires Guardian approval for every action.
- **Not a chatbot.** Focused on reasoning over *your* data, not LLM responses.
- **Not a replacement for human judgment.** Guardian and human can always override.

---

## Core Concepts

**SensorReading:** Every piece of external data becomes an object with type, raw data, confidence, consent flags, provenance note, source ID, device ID, timestamp.

**SensorInputHandler:** The abstraction managing sensor sources — register sensors, capture readings, query by type.

**MockSensors:** Safe, deterministic simulations: `mock_audio()`, `mock_text_input()`, `mock_environment()`, `mock_device_state()`, `mock_intent_simulation()`. The intent simulation infers intent from deliberately provided user text/voice and visible context (environment, time of day, device state) — all external, auditable, consensual. Never from brain signals.

**Integration with CrystalMemory:** Readings store as SparseTensor nodes with CoherenceMetadata carrying consent_flags and provenance_hash.

**Integration with CrystalFlow:** Reasoning reads permitted sensor inputs from memory; fails closed on denied access; outputs carry provenance chains and coherence scores.

**Guardian Veto:** Inspects every reasoning step for soundness — are inputs still permitted, is the coherence chain valid, is the rule documented? Approved conclusions proceed; vetoed ones are logged and removed from memory.

---

## Why This Design

**Sovereignty:** Everything local, no cloud, no third parties, you own the data.

**Consent:** Every reading tagged with permission flags; reasoning fails closed; consent can be revoked anytime.

**Provenance:** Every reading tagged with source/timestamp/confidence; every reasoning step chains back to its inputs; full audit trail.

**Safety:** Guardian layer can veto unsound reasoning; coherence tracking prevents false confidence; mocks let you test without hardware.

**Privacy:** No brain data ever captured; only external, voluntary inputs processed; you control what flows in.

---

## Planned Integration Path (to Status ✅)

1. ⬜ Code reviewed and merged to `src/crystal_sensor.py` on `main`
2. ⬜ Test suite runs as part of `run_tests.py` (adds 8 tests to the 118 existing)
3. ⬜ End-to-end example added to `examples/example_sensor_to_action.py`
4. ⬜ Integration test written: SensorInput → CrystalMemory → CrystalFlow → Guardian full chain
5. ⬜ Documentation added to main README

Once all five tick, the status line changes. Not before.

---

## Immediate Next Steps (From Your Docs)

**Today:** Run tests to verify everything works (`python3 test_crystal_sensor.py` → 8 passed). Run end-to-end example (`python3 example_sensor_to_action.py` → full sovereignty loop demonstrated).

**This week:** Integrate into CrystalCore module structure, verify all tests still pass, add README section.

**Next week:** Chain the full loop with a test: SensorInput → CrystalMemory → CrystalFlow → Guardian approval/veto. Start sketching real sensor backends (actual microphone, environment API).

**Two weeks:** Swap mock sensors for real ones (pyaudio for audio, Raspberry Pi GPIO for environment). Keep mocks for development.

**On Pi:** When you have target hardware, test the <256 MB RAM envelope and pure Python on ARM64.

---

## What Comes After

Sovereign edge intelligence: reasoning on your device, your data, your control. Family decision workflows: sensors feed data, Guardian enforces "power of three" consent. Transparent AI: every decision auditable, no black boxes. Learning loop: CrystalEvolve optimizing sensor interpretation over time.

---

*See also: [GLOSSARY.md](GLOSSARY.md) (CrystalSensor defined) · [CRYSTALCORE-FRAMEWORK.md](CRYSTALCORE-FRAMEWORK.md) (the reasoning stack it feeds) · [GOVERNANCE.md](GOVERNANCE.md) (why this page is Design, not Built)*

*Part of The Crystal Vision · TerAustralis Incognita · Non Solus — Not Alone*
