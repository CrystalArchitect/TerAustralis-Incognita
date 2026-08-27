# CONFLICTS — Where Sources Disagree

**Status: BUILT** — Process for handling conflicts between authoritative sources.

## Currently escalated

None.

## How to handle conflicts

When two repository sources disagree:

1. **Identify the conflict:** Which files say different things?
2. **Determine authority:** Which source is authoritative for this topic?
   - Governance matters: `docs/governance/Constitution.md` is authoritative
   - Project state: `STATUS.md` is authoritative (over README, CHANGELOG)
   - Architecture: `docs/architecture/` specs are authoritative (over comments)
   - AI workflow: `docs/ai/AI-Workflow.md` is authoritative (over agent notes)
3. **Record it:** Add to this file with format below
4. **Resolve it:** Update the non-authoritative source or open an issue
5. **Document the fix:** Update this file when resolution is complete

## Format for recording a conflict

```
**Topic: [area of disagreement]**
- Conflict: [Source A says X; Source B says Y]
- Authority: [Which source is canonical]
- Status: [Unresolved | Proposed fix | Fixed | Deferred]
- Next: [What should happen next]
```

## Example (template)

```
**Topic: Repository structure (example)**
- Conflict: README.md says "code in src/"; STATUS.md says "code moved to separate repos"
- Authority: STATUS.md (reflects current state, regularly updated)
- Status: Needs resolution — README.md examples reference old structure
- Next: Update README.md examples to point to separate repos, or link to SystemMap.md
```

---

**Report conflicts to Crystal via PR or issue. Never silently "fix" a source you think is wrong—write it down first.**
