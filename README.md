## Scope & Goals
- Objective: experiment and establish **best practices** for `copilot-instructions.md` (and related rules files) used to guide AI behaviour.

## First Log Entry — 2026-02-02 (Initial delegation)
- The repository owner delegated documentation duties to the Documentation Agent and requested a `README.md` to capture this process.

## Second Log Entry — 2026-02-02 (Strict Python rules & agent optimization)
- **What I did** — I added `copilot-instructions.md` to enforce strict Python standards (Poetry-only, strict `mypy`, `ruff` formatting, `Pydantic v2`, `pytest` with high coverage) and included `scripts/check_no_any.py` plus CI recommendations.
- **What worked** — CI checks and the `check_no_any` script caught issues early; explicit rules made automation straightforward and reduced inconsistent outputs from agents.
- **Insights gained** — I have learned that AI have to be actualy told in detail, and i have to write my prompts and instruction very slowly and mindfully. 