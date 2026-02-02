# TL;DR
    I created copilot-instructions.md focusing on building a robust, strongly typed, and tested Python coding environment.
    Based on my research, AI agents work best in typed environments and within test-driven development cycles.
    I also intend to use a separate agent to maintain my documentation (provided below), which is currently just a summary.

What I Did:
    Wrote copilot-instructions.md to enforce strict Python standards (Poetry, Pydantic v2, Mypy).
    Built agent_bench for async benchmarking and model validation to test how the model follows instructions and utilizes the described tools.

What Worked:
    The agent produced code as instructed; it successfully tested, fixed lints, and more.
    Successfully forced the AI to produce high-quality, typed code.

What Didn’t Work:
    Encountered pytest import errors; identified the need for better path management (e.g., PYTHONPATH or pytest.ini).
    I haven't found the time to fix these path issues yet.

Insights Gained:
    The importance of calm, deliberate, and slow prompting and planning—using my own head rather than completely relying on an agent.
    AI agents require explicit, granular rules to maintain consistency and toolchain compliance.


## Here is detailed log made by my agent
```md
## Scope & Goals
- Objective: experiment and establish **best practices** for `copilot-instructions.md` (and related rules files) used to guide AI behaviour.

## First Log Entry — 2026-02-02 (Initial delegation)
- The repository owner delegated documentation duties to the Documentation Agent and requested a `README.md` to capture this process.

## Second Log Entry — 2026-02-02 (Strict Python rules & agent optimization)
- **What I did** — I added `copilot-instructions.md` to enforce strict Python standards (Poetry-only, strict `mypy`, `ruff` formatting, `Pydantic v2`, `pytest` with high coverage) and included `scripts/check_no_any.py` plus CI recommendations.
- **What worked** — CI checks and the `check_no_any` script caught issues early; explicit rules made automation straightforward and reduced inconsistent outputs from agents.
- **Insights gained** — I have learned that AI have to be actualy told in detail, and i have to write my prompts and instruction very slowly and mindfully. 

---

**Entry — 2026-02-02: agent-bench setup**

**What I did**
- I created `src/packages/agent_bench` with `models.py` (Pydantic `InstructionSpec`) and `processor.py` (`async def run_benchmark`).
- I added tests in `src/packages/tests` for model validation and the async benchmark using `pytest` and `pytest-asyncio`.

**What worked**
- The agent produced typed, documented code (Pydantic v2, validators) and async utilities aligned with my rules.
- Tests are well-scoped and validate deterministic behavior.

**What didn’t work**
- Running `poetry run pytest` failed during collection with "attempted relative import with no known parent package" (test import paths issue).
- Workarounds: run tests with `PYTHONPATH=src`, run `python -m pytest`, or install the package in editable mode; consider updating tests to absolute imports or adding `pytest.ini` to set `pythonpath`.

**Insights gained**
- The instruction rules push the agent toward strong typing, test-driven development, and toolchain compliance (ruff, mypy), which matches my intent.
- Packaging and test discovery are fragile points; I should add a CI step that runs tests consistently to catch import/layout issues early.








# Final resust of Agent instruction, also found in copilot-instruction.md inside .github

# Copilot Instructions — Strict Python Project Standards

**Purpose:** Enforce a professional, strongly-typed, test-driven, and well-documented Python codebase using Poetry, ruff, mypy, pytest, and Pydantic v2.

---

## ✅ Mandatory Policies

- **Dependency Management**: Use **Poetry** only. Never use `pip install` or `requirements.txt`. All dependencies and dev-dependencies must be added via `poetry add` / `poetry add --dev` and committed to `pyproject.toml`.

- **Typing**: Use the `typing` module and run **mypy** on every change. **No `Any`** type is allowed unless accompanied by a written justification comment containing the exact token `justification:` (example below). `mypy` must be run in strict mode (see recommended config).

- **Code Style**: Follow **PEP 8**. Use **ruff** for linting and automatic formatting. Configure ruff to fix issues where safe.

- **Data Models**: Prefer **Pydantic v2** for all runtime data validation models. Use typed fields, `ConfigDict`, and `model_validator` for complex validations.

- **Testing**: Use **pytest** for all tests with **pytest-asyncio** for async tests. Aim for high coverage (default: 90%+). Every new feature requires corresponding tests in `tests/` with the same module-level scope.

- **Documentation**: Use **Google-style docstrings** for all public functions and classes. Public APIs must have examples when applicable.

- **Async**: Prefer `asyncio`/`async def` for I/O-bound operations. Use `pytest-asyncio` and `asyncio`-compatible libs for tests and implementation.

---

## 🛠️ Recommended Config Snippets

Refer to the repository-level `pyproject.toml` for the canonical configuration for Poetry, mypy, ruff, and pytest. Keep tool settings aligned with the project's `pyproject.toml`.

---

## ✍️ `Any` Usage Policy

- If `Any` is used it must be explicitly annotated and immediately accompanied by a justification comment. The comment must include the word `justification:` followed by a short reason and an action plan to remove or narrow `Any` later.

Example:


- A repo check script (`scripts/check_no_any.py`) will fail the build if `Any` appears without this comment.

---

## ✅ PR Checklist (must be completed before merging)

- [ ] Added/updated tests for new behavior (`tests/`)
- [ ] All tests pass locally: `poetry run pytest`
- [ ] Type-checks pass: `poetry run mypy .`
- [ ] Linting passes: `poetry run ruff check .` and formatted as needed: `poetry run ruff format .`
- [ ] No stray `Any` without `justification:` (pre-commit and CI enforce this)
- [ ] Google-style docstrings for any public API
- [ ] Pydantic models used for external data and validated with tests

---

## 🔧 CI recommendations

Create a CI workflow that runs:
- `poetry install --no-interaction --no-ansi`
- `poetry run ruff check .`
- `poetry run mypy .`
- `poetry run pytest --cov` (fail if coverage below threshold)
- `python scripts/check_no_any.py`

---

## 🧪 Testing Patterns

- Unit tests for logic and data models.
- Integration tests for major flows (use test containers or fixtures as needed).
- Use `pytest-asyncio` for async tests and mark with `@pytest.mark.asyncio`.
- Keep tests fast and deterministic; avoid real network calls (use mocks or test servers).

---

## 📎 Notes & Conventions

- Use `poetry run <tool>` in CI and locally.
- Keep `dev-dependencies` minimal and scoped to lint/test.
- Encourage small, focused PRs with one behavioral change.
```