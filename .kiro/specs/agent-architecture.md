# Kiro Crew Agent Architecture — Lazarus

**Kiro Feature:** Kiro Crew (multi-agent), Custom Agents  
**Spec reference:** `resurrection-spec.md` section 5

---

## Crew Members

| Agent | Role | Kiro App Used | Tools | Impact on Build |
|-------|------|---------------|-------|-----------------|
| **Archivist** | Reads repo tree, README, dependency files, commit history | Kiro IDE (spec reading), Kiro Web (autopsy preview) | GitHub MCP (repo read), Filesystem MCP (autopsy write) | First agent to touch every submission; determines if resurrection is warranted |
| **Mortician** | Diagnoses cause of death: deprecated deps, CVEs, API breakage, abandonment | Kiro IDE | Safety DB (CVE lookups via MCP), dependency parser | Prevents wasting surgery on active repos; produces `cause_of_death.md` |
| **Surgeon** | Writes code patches, dependency bumps, API migrations | Kiro IDE, Kiro CLI | GitHub MCP (branch + file write), local test runner | Produces the actual resurrection diff; every edit references a spec section ID |
| **Embalmer** | Adds tests, README updates, changelog, preserves original spirit | Kiro IDE, Kiro Web | Filesystem MCP, test runner | Ensures resurrected repo is maintainable and documented |

## Inter-Agent Communication

Agents do not prompt-chain directly. They communicate through **shared spec artifacts** in `/.kiro/specs/` and `/.kiro/agents/state/`:

```
Archivist → writes repo_autopsy.md
Mortician → reads repo_autopsy.md, writes cause_of_death.md
Surgeon   → reads cause_of_death.md + resurrection-spec.md, writes patches/
Embalmer  → reads patches/, writes tests/ + README updates
```

This is spec-driven development: each agent's contract is a file, not a conversation.

## Hooks (Agent Automation)

Defined in `/.kiro/hooks/`:

- `pre-resurrection-hook` — Runs before Archivist. Validates repo is public and inactive (≥ 12 months no commits, or only dependabot commits). Aborts with a clear message if the repo is alive.
- `post-spec-hook` — Runs after Surgeon writes patches. Executes `pytest` on the branch. If any test fails, PR creation is blocked and the Surgeon is notified to revise.
- `pr-creation-hook` — Runs before `git push`. Verifies the PR body references at least one spec section ID (S1–S6) and includes the health-score delta.

## Steering

All agent behavior is constrained by `/.kiro/steering/kiro-crew-steering.md`:

- Never commit secrets, API keys, or tokens.
- Every agent response must cite the spec section it implements.
- All user-facing copy must be gothic-themed but WCAG-AA accessible.
- Do not rewrite the original project's architecture; only modernize.

## How This Differed from Vibe Coding

- **Before Kiro Crew:** We would have written one big prompt, hoped the model figured out the pipeline, and debugged by re-prompting.
- **With Kiro Crew:** Each agent has a defined role, input file, output file, and steering constraints. We debugged by reading the intermediate artifacts (`repo_autopsy.md`, `cause_of_death.md`) rather than re-prompting. The spec is the source of truth.
