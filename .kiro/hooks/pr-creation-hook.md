# PR Creation Hook

**Kiro Feature:** Agent Hooks  
**Trigger:** Before `git push` and pull request creation  
**File:** `/.kiro/hooks/pr-creation-hook.md`

---

## Purpose

Guarantee every resurrection pull request is traceable to the spec and contains the information judges and maintainers need.

## Preconditions (ALL must pass)

1. At least one spec section ID (S1–S6 from `resurrection-spec.md`) is referenced in the PR body.
2. Health-score delta (before → after) is included.
3. No secrets or tokens in the diff (secret scan).
4. `.kiro` directory is present and not gitignored (Kiroween requirement).

## PR Body Template

```
## 🪦 Lazarus Resurrection

This PR resurrects `<owner>/<repo>`, an abandoned GitHub repository, using Kiro Crew agents.

### Cause of Death
- `deprecated_deps`
- `cve`

### Spec Sections Applied
- S1: Dependency upgrade
- S2: Security patch

### Health Score
- Before: 2.1 / 10
- After: 7.8 / 10
- Delta: +5.7

### Kiro Agents Used
Archivist, Mortician, Surgeon, Embalmer (Kiro Crew)

### Built for Kiroween 2026 — Resurrection Category
https://github.com/<you>/lazarus
```

## Action on Pass

Push branch and open PR with the above body.

## Action on Fail

Block push. Return missing precondition(s) to the Surgeon agent.
