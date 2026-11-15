# Code Style Steering — Lazarus

**Kiro Feature:** Steering Documents  
**Applies to:** All source code in `app/`, `frontend/`

---

## Python (Backend)

- Follow PEP 8.
- Use type hints on all public functions.
- Docstrings in Google style.
- FastAPI routes use Pydantic models for request/response.
- Error responses follow `{"error": "...", "code": "..."}`.
- All endpoints have corresponding tests in `app/tests/`.

## JavaScript (Frontend)

- Vanilla JS (no build step). ES modules where served via a static server.
- `const`/`let` only; no `var`.
- Event delegation for dynamic elements.
- All DOM updates go through a single `render()` function per component.
- Accessibility: ARIA labels on buttons, focus outlines, `prefers-reduced-motion` respected.

## CSS / Theme

- Gothic palette: `#0b0c10` (background), `#1f2833` (surface), `#66fcf1` (accent), `#c5c6c7` (text).
- Serif headings (`'Playfair Display'` or system serif), sans body.
- Dark mode by default; respect `prefers-color-scheme`.
- WCAG AA contrast minimum 4.5:1 for body text.

## Commit Style

- `feat:`, `fix:`, `docs:`, `chore:` prefixes.
- Every commit references a spec section: `(ref S1)` etc.
