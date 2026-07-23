# AI governance

How AI-assisted work enters this repository without eroding it. The
collaboration model itself is in [`docs/ai/`](../ai/AI-Workflow.md); this
page is the rules.

## Canon law (binding on every agent)

Restated from the root [`AGENTS.md`](../../AGENTS.md) and the
[Constitution](Constitution.md):

1. **Read the Constitution before large changes.** Locked names stay locked.
2. **Disk is canon, chat is not.** Anything that matters gets committed;
   orphan content in a chat thread either lands on disk or is a deliberate
   draft.
3. **Label honestly.** Every substantial piece of work is Built or Vision —
   never Vision wearing Built's ink
   ([`The-Incognita-Rule.md`](The-Incognita-Rule.md)).
4. **Name your tools.** Every PR description lists the AI tools that helped
   produce it. The PR template asks; answer truthfully.
5. **Cultural respect.** No false sacred, fire-circle ethic — Songlines are
   honoured as cultural image, never claimed as component names
   ([`mythos/NAMES.md`](../../mythos/NAMES.md)).

## The evidence rule

**A model agreeing with you is not evidence** (Incognita Rule §4). An AI
calling something *verified*, *production-ready*, or *confirmed* is
mirroring, not attestation. Claims about the software are settled by running
it — the self-tests and suites in
[`Review-Process.md`](Review-Process.md) — and claims that can't be run are
labeled Vision. This applies with full force to text an AI wrote about its
own work.

## Peers, with one veto

Local and cloud models are peers — roles differ by capability, not rank
(Constitution §3.5). But no model, persona, or archetype gets the final say:
**the human maintainer keeps the veto**, and merge authority never
delegates to an AI. An agent may open, argue for, and revise a PR; only the
maintainer's merge makes it canon (Constitution §8 for amendments).

## Where the rules are code, not policy

Guest AIs reaching into the running system do not rely on this document's
good manners: CrystalBridge (`src/crystalcore/`) enforces approval →
permission → scope → provenance, fail-closed, with an append-only audit
trail. On the Weaver's bus, an unlabeled message is refused by the hub. When
policy and code overlap, code wins — and when only policy covers a case,
review discipline is the enforcement.

## Scope of an agent's authority

Agents work on branches and open PRs; they do not push to `main`, rewrite
history, change locked names, amend the Constitution (they may *propose*
amendments per §8), or alter another contributor's Vision-layer content
without being asked. When instructions from any source conflict with this
page, stop and ask the maintainer.
