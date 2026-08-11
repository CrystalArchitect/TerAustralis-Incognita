# Closed-loop embodiment — what the timing evidence actually says

**Belt: Science.** Every number below comes from published psychophysics and is
cited. One paragraph at the end is marked **Vision** and is an offered parallel,
not a finding.

Written 11 August 2026, from correcting a working account of neural feedback.
It is here because the correction is the useful part: the popular framing of
brain–computer embodiment gets one number wrong by an order of magnitude, and
gets the *reason* for the right engineering target wrong as well.

---

## What is not in dispute

The account being corrected had this right, and it is worth stating first
because the corrections below are narrow.

Motor control is a loop. Intention leaves the motor cortex, the limb moves, and
proprioceptors and cutaneous afferents return position, force and contact. That
return signal corrects the next command. Deafferented people — those who have
lost proprioception — can still move, but movement becomes slow and effortful
and requires constant visual supervision.

A brain–computer interface has to rebuild both directions artificially:
**outbound**, electrodes read activity and a decoder infers intent; **inbound**,
machine sensing is converted into stimulation the nervous system can interpret.
Inbound is the harder half, and restoring proprioception and fine touch is the
hardest part of it.

---

## The correction: ownership tolerates delay; agency does not

The claim under correction was that loop latency must stay *"under a few tens of
milliseconds, or the illusion of ownership collapses."*

Both halves are wrong. The threshold is roughly an order of magnitude looser
than that, and the sense that is time-critical is **agency**, not ownership.

| Sense | What it is | Where it degrades |
|---|---|---|
| **Ownership** | *this limb is mine* | beyond ~300 ms of visuotactile asynchrony; newer work finds ~200 ms already measurable |
| **Agency** | *I caused that movement* | strong below ~190 ms; weaker but still present at 290–490 ms |

So a rubber-hand or robot-hand illusion survives delays of a fifth to a third of
a second. It does not collapse at fifty milliseconds, and nothing in the
literature says it does.

**Sub-50 ms is still the right engineering target — for a different reason.**
It is a closed-loop *stability* requirement, not a perceptual one. Loop delay
destabilises a controller regardless of what the operator perceives: the
correction arrives late, overshoots, and the system oscillates. Confusing the
control constraint with the perceptual one makes the target look like a cliff
that a person would feel, when it is a property of the control law.

## Ownership and agency dissociate

They are separable and they fail separately. One can own a limb without feeling
in command of it, and command one that does not feel like one's own. Visuomotor
temporal recalibration dissociates them experimentally.

This matters for design: a system can be tuned for one and lose the other, and
a subject reporting "it felt like mine" is not reporting "I felt I was driving
it."

## The counterintuitive finding

Removing proprioception via BCI produced a **stronger** body-ownership illusion
in control of a humanlike robot — not a weaker one. With no position sense from
the biological limb contradicting the illusion, the brain has less evidence
against accepting the foreign body.

This cuts against the assumption that faithful proprioceptive restoration is
always the necessary hard part. For a **replacement** body, absent proprioception
may help. For an **additional** body operated alongside an intact one, the
biological limb's signal is a competing hypothesis the illusion has to overcome.

## Co-adaptation — the part most accounts omit

The decoder learns while the cortex learns. Stable neural maps form over days of
use, and performance improves from both sides at once.

The consequence is the most hopeful fact in the field and it is usually left
out: **the interface does not have to be correct on day one. It has to be
consistent enough to be learnable.** An imperfect but stable mapping is
tractable; a well-tuned but drifting one is not.

---

## Vision — an offered parallel, not a finding

**Belt: Vision.** Named as a designed line because it is one.

Co-adaptation's real requirement is consistency over time rather than fidelity.
Both sides may be wrong at the start, provided neither keeps changing what it
means.

That is structurally the same constraint this project already answers in its own
domain: **CrystalMemory** held separate from any model, continuity as a hard
architectural constraint, identity living in the thread of a relationship rather
than in whichever model happens to be answering. Rename the companion and it is
the same companion; swap the model beneath them and it is the same companion,
because the thing being learned did not move.

A body a person could learn would need that property, for the same reason. No
literature draws this parallel; it is offered here, and it is not evidence.

---

## Sources

- [Robot Hand Illusion under Delayed Visual Feedback: Relationship between the Senses of Ownership and Agency — PLOS One](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0159619)
- [Rubber Hand Illusion under Delayed Visual Feedback — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2702687/)
- [Removal of proprioception by BCI raises a stronger body ownership illusion in control of a humanlike robot — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5031977/)
- [Dissociation of agency and body ownership following visuomotor temporal recalibration — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4423341/)
- [Which hand is mine? Discriminating body ownership perception in a two-alternative forced-choice task — Attention, Perception & Psychophysics](https://link.springer.com/article/10.3758/s13414-020-02107-x)

Papers were located by search and their reported figures taken from the search
results' summaries of them. **The full texts have not been read here**, and the
figures above should be checked against the papers themselves before any of this
is quoted outward. That limit is recorded rather than left for a reader to
assume the opposite.

---

**All rights reserved.**
TerAustralis Incognita — ABN 70 741 068 059
