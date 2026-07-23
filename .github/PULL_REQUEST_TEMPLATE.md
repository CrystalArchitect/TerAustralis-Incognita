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

<!-- Paste what you ran and the results — claims come with evidence. -->

- [ ] Markdown lint passes (`npx markdownlint-cli2 "**/*.md" "#node_modules" "#archive"`) —
      CI runs the same check with `.markdownlint.jsonc`
- [ ] Link check passes (CI runs `markdown-link-check` with
      `.github/workflows/markdown-link-check-config.json`)
- [ ] No generated files, secrets, or personal data staged

This repository holds governance, architecture docs, ADRs, and the mythos —
no application code (see
[`docs/architecture/SystemMap.md`](../docs/architecture/SystemMap.md#where-the-code-actually-lives)).
For engine/app code changes, see
[`TerAustralis-Incognita-Code`](https://github.com/CrystalArchitect/TerAustralis-Incognita-Code)'s
own PR template.

## For the reviewer

<!-- Anything that needs a second pair of eyes: judgment calls, deviations
     from a spec, an ADR if the change is structural. -->
