# Kiro Crew Steering — Lazarus

**Kiro Feature:** Steering Documents  
**Applies to:** All Kiro Crew agents (Archivist, Mortician, Surgeon, Embalmer)  
**File:** `/.kiro/steering/kiro-crew-steering.md`

---

## Conduct Rules

1. **No secrets.** Never commit API keys, tokens, passwords, or connection strings. If a secret is detected in a diff, abort.
2. **Spec-first.** Every code change must reference a section of `/.kiro/specs/resurrection-spec.md` (S1–S6). No spec section, no change.
3. **Preserve intent.** Modernize dependencies and APIs, but do not rewrite the original project's architecture or remove core features.
4. **Gothic but accessible.** All user-facing UI copy uses the Lazarus gothic theme (dark backgrounds, serif headings, accent colors) but must meet WCAG AA contrast and keyboard navigation.
5. **Public only.** All GitHub MCP operations target public repositories only.
6. **Cite the spec.** Every agent response must end with: `Spec ref: <section ID>` or `Spec ref: N/A` if not applicable.

## Agent-Specific Steering

### Archivist
- Read only; never write to the target repo.
- Record last-commit date, dependency files, open issue count, primary language.

### Mortician
- Do not mark a repo dead if the last human commit is < 12 months old.
- Classify cause of death into: `deprecated_deps`, `cve`, `api_breakage`, `abandonment`, `license_issue`.

### Surgeon
- Run tests locally before suggesting a patch.
- Prefer minimal, targeted diffs over large rewrites.

### Embalmer
- Add at least one smoke test per resurrected module.
- Update README to include a "Resurrected by Lazarus" badge.

## How Steering Improved the Build

Without steering, Kiro tended to suggest full framework migrations (e.g., Flask → FastAPI) that changed the project's identity. Steering rule #3 forced targeted modernization, which judges recognized as respecting the original technology — a core Resurrection value.
