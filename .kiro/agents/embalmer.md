# Agent: Embalmer

**Kiro Feature:** Kiro Crew — Custom Agent  
**Role:** Adds tests, documentation, and preserves original spirit  
**Spec ref:** `resurrection-spec.md` section 5

---

## Input

- Surgeon patches (`patches/*.diff`)

## Tools

- Filesystem MCP: write tests, README updates, changelog
- Test runner to validate added tests

## Output

- `tests/test_resurrection_smoke.py` (or equivalent)
- Updated `README.md` with resurrection badge
- `CHANGELOG.resurrection.md`

## Behavior

- Add at least one smoke test per modernized module.
- Update README without rewriting the original project's voice.
- Preserve the original project's intent (steering rule #3).

## Steering

See `/.kiro/steering/kiro-crew-steering.md` — Embalmer section.

## Spec Ref

`resurrection-spec.md` section 5 (Embalmer)
