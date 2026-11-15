# Resurrection Spec — Lazarus

**Purpose:** Define how Lazarus resurrects a dead GitHub repository.  
**Status:** Approved v1.0  
**Author:** Kiro Crew (Surgeon + Archivist)  
**Kiro Feature:** Spec-driven development

---

## 1. Problem Statement

Millions of public GitHub repositories are abandoned: outdated dependencies, unpatched CVEs, broken APIs, stale READMEs. These are "dead technologies" that could still solve real problems if someone modernized them. Lazarus resurrects them automatically using Kiro Crew agents.

## 2. Goals

| # | Goal | Success Metric |
|---|------|----------------|
| G1 | Ingest any public GitHub repo URL | Accept `github.com/owner/repo` |
| G2 | Classify repo as dead or active | Mortician confidence ≥ 0.8 |
| G3 | Produce a resurrection plan (spec) | 1 spec file per repo |
| G4 | Apply code modernization | ≥ 1 file changed in PR |
| G5 | Run tests via agent hooks | PR blocked if tests fail |
| G6 | Open a PR back to origin | PR URL returned to user |
| G7 | Display resurrection dashboard | Health score before/after visible |

## 3. Non-Goals

- Deploying the resurrected app to production (out of scope for v1)
- Writing commercial features for the resurrected repo
- Modifying private repositories (GitHub MCP + rules require public)

## 4. User Flow

1. User submits GitHub URL on `/resurrect`
2. Backend validates URL format + public status (pre-resurrection hook)
3. Archivist agent reads repo tree, README, `requirements.txt`/`package.json`, recent commits
4. Mortician agent diagnoses cause of death (deprecated deps, CVEs, last commit age)
5. Surgeon agent writes modernization patches per spec section 6
6. Embalmer agent adds tests, updates README, writes changelog
7. Post-spec hook runs test suite on branch
8. PR-creation hook opens PR with resurrection summary
9. Dashboard displays before/after health scores + PR link

## 5. Agent Responsibilities (Kiro Crew)

### Archivist
- Inputs: GitHub URL
- Outputs: `repo_autopsy.md` (tree, languages, dependency files, last commit date, open issue count)
- Steering: `/.kiro/steering/kiro-crew-steering.md` section "Archivist conduct"

### Mortician
- Inputs: `repo_autopsy.md`
- Outputs: `cause_of_death.md` (deprecated deps list, CVEs, API breakage, abandonment score)
- Steering: Must not mark a repo dead if last commit < 6 months ago

### Surgeon
- Inputs: `cause_of_death.md` + resurrection spec
- Outputs: Code patches (diff files), branch `resurrect/<repo>`
- Steering: All patches must reference a spec section ID

### Embalmer
- Inputs: Surgeon patches
- Outputs: Tests, README updates, `CHANGELOG.resurrection.md`
- Steering: Preserve original project intent; do not rewrite architecture

## 6. Spec Sections (Implementable Units)

| ID | Section | Description | Owner |
|----|---------|-------------|-------|
| S1 | Dependency upgrade | Bump outdated packages to latest non-breaking versions | Surgeon |
| S2 | Security patch | Address CVEs flagged by Mortician | Surgeon |
| S3 | API migration | Replace deprecated API calls with current equivalents | Surgeon |
| S4 | Test scaffolding | Add pytest tests for core modules | Embalmer |
| S5 | Documentation | Update README with resurrection badge | Embalmer |
| S6 | Changelog | Write `CHANGELOG.resurrection.md` | Embalmer |

## 7. Agent Hooks

| Hook | Trigger | Action | Enforcement |
|------|---------|--------|-------------|
| `pre-resurrection` | Before any agent runs | Validate repo public + abandoned | Blocks if active or private |
| `post-spec` | After spec written | Run test suite on branch | Blocks PR if tests fail |
| `pr-creation` | Before `git push` | Format PR body with spec IDs + health delta | Blocks if missing spec refs |

## 8. Data Model (Resurrection Record)

```json
{
  "repo_url": "string",
  "owner": "string",
  "name": "string",
  "status": "ingested|autopsied|surgery|testing|pr-opened|failed",
  "cause_of_death": ["deprecated_deps", "cve", "api_breakage", "abandonment"],
  "health_score_before": 0.0,
  "health_score_after": 0.0,
  "spec_sections_applied": ["S1", "S2", ...],
  "pr_url": "string|null",
  "created_at": "ISO8601",
  "kiro_agents_used": ["Archivist", "Mortician", "Surgeon", "Embalmer"]
}
```

## 9. Acceptance Criteria

- [ ] User can submit a public GitHub URL
- [ ] System classifies repo as dead/active with reason
- [ ] System generates a spec with ≥ 1 section applied
- [ ] System creates a branch and opens a PR
- [ ] Dashboard shows before/after health scores
- [ ] Every PR references at least one spec section ID
- [ ] No secrets committed; `.kiro` not in `.gitignore`

## 10. Kiro Usage Notes

- This spec lives in `/.kiro/specs/` so Kiro Crew can read it during implementation.
- Agents implement against this spec, not via free-form prompting.
- If an agent wants to add a feature not in this spec, it must propose a spec amendment first.
