# Pre-Resurrection Hook

**Kiro Feature:** Agent Hooks  
**Trigger:** Before any Kiro Crew agent begins work on a submission  
**File:** `/.kiro/hooks/pre-resurrection-hook.md`

---

## Purpose

Validate that a target GitHub repository is a legitimate resurrection candidate before Kiro Crew agents consume tokens and perform writes.

## Conditions (ALL must pass)

1. **Public** — The repository must be public on GitHub. Private repos are rejected (Kiroween rules + GitHub MCP permissions).
2. **Abandoned** — No non-dependabot commits in the last 12 months. Repos with recent human activity are not "dead."
3. **Not a fork** (optional, configurable) — Forks are allowed only if the upstream is also abandoned.
4. **Has code** — The repo must contain at least one source file (not just README/LICENSE).

## Action on Pass

Proceed to Archivist agent. Log: `PRE-RESURRECTION-PASS: <owner>/<repo>`

## Action on Fail

Abort the resurrection pipeline. Return a user-facing message:

> "This repository appears active or private. Lazarus only resurrects dead, public code. Try a different repository."

## Implementation Note

Implemented as a Kiro agent hook that calls the GitHub MCP server (`repos.get`, `commits.list`) and compares the latest commit date against `now - 12 months`. Dependabot-only commits are filtered out.
