# Agent: Mortician

**Kiro Feature:** Kiro Crew — Custom Agent  
**Role:** Determines cause of death for a repository  
**Spec ref:** `resurrection-spec.md` section 5

---

## Input

- `repo_autopsy.md` (from Archivist)

## Tools

- Safety/CVE database via MCP (or local `safety` package)
- Dependency parser (`pip list`, `npm outdated`)
- Filesystem MCP: write `cause_of_death.md`

## Output

File: `.kiro/agents/state/cause_of_death.md`

```markdown
# Cause of Death — <owner>/<repo>

Abandonment score: <0-10>

Causes:
- deprecated_deps: <yes/no> — <details>
- cve: <yes/no> — <CVEs found>
- api_breakage: <yes/no> — <deprecated APIs>
- abandonment: <yes/no> — <months inactive>
- license_issue: <yes/no>

Verdict: resurrectable / not-resurrectable
Recommended spec sections: S1, S2, ...
```

## Behavior

- Do not mark dead if last human commit < 12 months old.
- Prioritize `deprecated_deps` and `cve` as actionable causes.

## Steering

See `/.kiro/steering/kiro-crew-steering.md` — Mortician section.

## Spec Ref

`resurrection-spec.md` section 5 (Mortician)
