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

```py
from typing import Any

# justification: third-party library returns untyped JSON; will add typed wrappers in follow-up ticket
untyped_obj: Any
```

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

## 📚 Pydantic v2 Example

```py
from pydantic import BaseModel, ConfigDict

class Item(BaseModel):
    name: str
    quantity: int

    model_config = ConfigDict(extra='forbid')
```

---

## 📎 Notes & Conventions

- Use `poetry run <tool>` in CI and locally.
- Keep `dev-dependencies` minimal and scoped to lint/test.
- Encourage small, focused PRs with one behavioral change.

---

If you want, I can also generate a sample `pyproject.toml` and a CI workflow to enforce all checks. 🙌
