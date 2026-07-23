# Attributions & Third-Party References

This document credits external sources, intellectual property, and third-party work that informed the design of CrystalCore OS and its components.

---

## MemClaw: Governed Shared Memory for AI Agent Fleets

**Source:** https://github.com/caura-ai/caura-memclaw  
**License:** Apache 2.0  
**Maintainers:** eToro and contributors (NASDAQ: ETOR)  
**Production:** Operates at scale with 300+ agents, 26,500+ memories, 1,372+ shared skills

### Concepts Incorporated

The following architectural patterns from MemClaw informed the design of the Crystal Runtime:

#### 1. Multi-Agent Governance Model
MemClaw's approach to governing memory access across agent fleets directly inspired the Crystal Runtime's Registry and Events modules. Specifically:
- **Visibility scopes:** Controlling who (which agent, team, or organization) can see and use which capabilities and data
- **Trust tiers:** Establishing levels of authorization (approval, permission, scope, provenance) similar to CrystalBridge's consent model
- **Fleet-scoped coordination:** Enabling cross-agent collaboration under unified rules, analogous to the runtime's coordination of Lumina, Starline, Weaver, CrystalBridge, and RDP

#### 2. Outcome-Based Learning & Reinforcement
MemClaw's feedback loop (agents report successes/failures to improve what gets stored) informed the Crystal Runtime's:
- **Event-driven architecture:** Events published by components carry outcomes and state changes
- **Logging & audit model:** Distinguishing operational, diagnostic, and audit records to enable post-mortem analysis and improvement
- **Failure behavior documentation:** Explicit categorization (recoverable, retryable, fatal, configuration, external, security) for robust error handling

#### 3. Hybrid Search & Capability Discovery
MemClaw's hybrid search (semantic + keyword) and automatic enrichment (type classification, summaries, importance scoring) informed the Crystal Runtime's:
- **Registry module:** Capability lookup combining explicit (registered) and implicit (inferred) service discovery
- **Event routing:** Matching events to subscribers based on type and context
- **Configuration model:** Multi-source configuration (files, environment, overrides) with validation and schema enforcement

#### 4. Automatic Knowledge Structure Extraction
MemClaw's knowledge graph extraction and entity resolution patterns informed:
- **Component integration contracts:** Explicitly documenting boundaries and interaction patterns between runtime modules and external systems
- **Interface definitions:** Moving from implicit coupling to published, versioned interfaces
- **Extension points:** Structured plugability rather than ad-hoc customization

#### 5. Contradiction Detection
MemClaw's mechanism for flagging conflicting memories informed:
- **Starline Weaver integration:** Belt-Three labeling ensures different truth layers (science/story/vision) don't collapse into each other
- **Audit trail:** RDP's tamper-evident chain preserves all events for later conflict resolution
- **Error model:** Distinguishing recoverable vs. fatal contradictions in configuration or state

### Attribution & Licensing

When using CrystalCore OS or the Crystal Runtime:
- This work is distributed under Apache 2.0, the same permissive license as MemClaw
- Any derivative or redistributed version must:
  1. Retain this ATTRIBUTIONS.md file or equivalent attribution
  2. State that it is derived from CrystalCore OS (and indirectly, from MemClaw)
  3. Preserve the Apache 2.0 license notice and reference the original sources
  4. Not misrepresent authorship or remove attribution notices

---

## Licensing Structure

**CrystalCore OS Code & Specifications:** CC BY-NC-ND 4.0  
**CrystalCore OS Mythos Content:** CC BY-NC-ND 4.0 (see LICENSE-CONTENT.md)  
**MemClaw Concepts (Referenced):** Apache 2.0 (see acknowledgment below)  
**Commercial Use:** Restricted to copyright holder. For commercial licensing, contact the maintainer.

### Key Clarification

CrystalCore OS is **not** open source for commercial reuse. It is licensed under CC BY-NC-ND 4.0:
- ✓ Non-commercial use allowed (research, personal projects, education)
- ✓ Attribution required
- ✗ Commercial use prohibited without explicit permission
- ✗ Derivative works (modified versions) prohibited

MemClaw's architectural patterns are **acknowledged** under Apache 2.0 (their license). The *application* of those patterns in CrystalCore OS is CC BY-NC-ND 4.0.

## Intellectual Property & Reuse Policy

### For Contributors
When proposing changes to CrystalCore OS that draw on external work:
1. **Cite the source.** In your PR, note any external papers, articles, open-source projects, or systems that inspired your design.
2. **Verify licensing.** Ensure the source license is compatible with CC BY-NC-ND 4.0 (no commercial restrictions).
3. **Credit in code.** Add a comment linking to the source in the code, not just in the PR description.
4. **Update this file.** Add an entry to ATTRIBUTIONS.md if the contribution is significant.

### For Users (Non-Commercial)
If you use CrystalCore OS for non-commercial purposes:
1. **Retain attribution.** Keep ATTRIBUTIONS.md and this license notice.
2. **Do not distribute modified versions.** CC BY-NC-ND prohibits derivative redistribution.
3. **Link back.** Reference the original CrystalCore OS repository in your credits.

### For Commercial Users
Commercial use, licensing, or commercial derivative works require:
1. **Written permission** from the copyright holder
2. **Commercial license agreement** (available by negotiation)
3. **Attribution** to CrystalCore OS and MemClaw (for inspired concepts)

### For Redistributors (Non-Commercial)
If you redistribute unmodified CrystalCore OS:
1. **Keep the CC BY-NC-ND 4.0 license.** Do not change the license terms.
2. **Retain all attribution notices.** ATTRIBUTIONS.md, copyright headers, and source links must be preserved.
3. **Never claim exclusive authorship.** You may claim to be a mirror/mirror maintainer, not the original author.
4. **Link back to original.** In your README or documentation, link to the original CrystalCore OS repository.

---

## License Enforcement

### Copyright Notice

```
Copyright (c) 2026 CrystalCore OS Contributors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

This work incorporates concepts and patterns from MemClaw
(https://github.com/caura-ai/caura-memclaw, Apache 2.0),
maintained by eToro and contributors.
```

This notice applies to all code, specifications, and documentation in CrystalCore OS unless otherwise noted.

### Rebranding & Theft Prevention

CrystalCore OS is protected under Apache 2.0. This means:
- **You can use it freely** — for commercial or personal projects, with or without modification.
- **You must attribute it** — any distribution or modification must credit the original work and this license.
- **You cannot rebrand it** — you cannot remove attribution, falsify authorship, or present modified versions as your original work.
- **Derivative works must be disclosed** — if you modify and redistribute, users must know it is derived from CrystalCore OS.

If you discover a violation (rebranding, false attribution, license removal, etc.), report it to the project maintainers or to the Apache Software Foundation.

---

## Related Documents

- [LICENSE](../../LICENSE) — Full Apache 2.0 license text
- [CONTRIBUTING.md](../../CONTRIBUTING.md) — Contribution guidelines (includes attribution requirements)
- [README.md](../../README.md) — Project overview
- [docs/governance/AI-Governance.md](governance/AI-Governance.md) — AI collaboration governance (includes attribution rules for AI-assisted work)

---

## Questions & Policy Updates

If you have questions about attribution, licensing, or are proposing work based on external sources, open an issue or discussion in the repository. This policy is a living document and will be refined as the project grows.

*Last updated: 2026-07-23*
