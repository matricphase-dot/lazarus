# Agent: Surgeon

**Kiro Feature:** Kiro Crew — Custom Agent  
**Role:** Applies code modernization patches  
**Spec ref:** `resurrection-spec.md` section 5

---

## Input

- `cause_of_death.md` (from Mortician)
- `resurrection-spec.md` (sections S1–S6)

## Tools

- GitHub MCP: create branch, write files
- Local test runner (`pytest`, `npm test`)
- Filesystem MCP: write patch files to `patches/`

## Output

- Branch: `resurrect/<owner>/<repo>`
- Files: `patches/<section>.diff` (e.g., `patches/S1.diff`)

## Behavior

- Each patch maps to exactly one spec section (S1–S6).
- Run tests before and after each patch.
- Prefer minimal, targeted diffs.

## Steering

See `/.kiro/steering/kiro-crew-steering.md` — Surgeon section.

## Spec Ref

`resurrection-spec.md` section 5 (Surgeon)
