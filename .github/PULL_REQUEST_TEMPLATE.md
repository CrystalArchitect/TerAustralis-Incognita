# What changed

<!-- Plain description of the change and why. -->

## Belt-Three label

<!-- Which layer does this change live on? Keep the labels honest
     (CONTRIBUTING.md, docs/governance/The-Incognita-Rule.md). -->

- [ ] **Science / Built** — running code, tests, checkable facts
- [ ] **Story / Vision** — mythos, art, speculative framing (labeled as such)
- [ ] **Docs / governance / process**

## AI tools used

<!-- Canon law: every PR names the AI tools that helped produce it
     (docs/governance/AI-Governance.md). "None" is a fine answer. -->

## Checks run

<!-- Paste what you ran and the results — claims come with evidence.
     `scripts/maintenance/check.sh` runs the same checks CI runs. -->

- [ ] `python -m compileall -q src tests archive`
- [ ] crystal-core self-tests (`clementine.bridge` / `services` / `starline` / `rdp`)
- [ ] `pytest src/apps/lumina/tests` and `pytest tests`
- [ ] site builds (`cd src/site && npm run build`) — if the site changed
- [ ] No generated files, secrets, or personal data staged

## For the reviewer

<!-- Anything that needs a second pair of eyes: judgment calls, deviations
     from a spec, an ADR if the change is structural. -->
