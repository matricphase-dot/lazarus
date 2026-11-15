# Post-Spec Hook

**Kiro Feature:** Agent Hooks  
**Trigger:** After the Surgeon agent writes modernization patches (spec sections S1–S6)  
**File:** `/.kiro/hooks/post-spec-hook.md`

---

## Purpose

Ensure the resurrected code actually works before a pull request is created.

## Action

1. Checkout the modernization branch `resurrect/<owner>/<repo>`.
2. Install dependencies from the repo's lockfile (`requirements.txt`, `package.json`, etc.).
3. Run the project's test suite if one exists; otherwise run Lazarus-generated tests (Embalmer output).
4. Capture pass/fail and coverage.

## Enforcement

- **If tests pass:** Proceed to `pr-creation-hook`.
- **If tests fail:** Block PR creation. Notify the Surgeon agent to revise patches. Log: `POST-SPEC-FAIL: <owner>/<repo> — <test_name>`.
- **If no tests exist and Embalmer generated none:** Warning only (not a block), but Embalmer must add at least one smoke test before PR.

## Implementation Note

Implemented as a Kiro hook that spins up a temporary container (or local venv) per resurrection, runs tests, and reports results to the dashboard.
