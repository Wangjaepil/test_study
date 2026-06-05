# AGENTS.md

## Project Overview

This project is a Python-based in-vehicle occupant safety detection system. It detects whether a child or pet remains inside a vehicle and sends timely alerts to prevent heatstroke, hypothermia, or other safety incidents.

## Development Principles

- Use Python as the primary development language.
- Follow test-driven development (TDD): write a failing test first, implement the minimum code to pass it, then refactor.
- Keep safety-critical behavior explicit, testable, and observable.
- Prefer small, focused modules with clear responsibilities.
- Avoid hidden side effects in detection, notification, and configuration code.
- Treat false negatives as the highest safety risk and design tests accordingly.

## Expected Repository Structure

```text
.
├── src/
│   └── vehicle_guardian/
│       ├── detection/
│       ├── notification/
│       ├── sensors/
│       └── config/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── docs/
│   └── requirements.md
├── releases/
│   └── index.md
├── .github/
│   └── workflows/
│       └── pr-validation.yml
└── agents.md
```

## TDD Workflow

1. Define the expected behavior in a test.
2. Run the test and confirm it fails for the expected reason.
3. Implement the smallest production change that passes the test.
4. Refactor while keeping all tests green.
5. Add edge-case tests for safety-critical logic.

Recommended commands:

```powershell
python -m pytest
python -m pytest --cov=src --cov-report=term-missing
python -m ruff check .
python -m ruff format .
```

## Branch Policy

Use `main` as the protected production branch.

Branch naming:

- `feature/<short-description>` for new features
- `fix/<short-description>` for bug fixes
- `test/<short-description>` for test-only changes
- `docs/<short-description>` for documentation changes
- `release/<version>` for release preparation

Rules:

- Do not commit directly to `main`.
- All changes must be merged through a pull request.
- Each pull request must include tests or explain why tests are not applicable.
- Pull requests must pass GitHub Actions validation before merge.
- Squash merge is recommended to keep history readable.
- Use semantic versioning for releases: `MAJOR.MINOR.PATCH`.

## Pull Request Checklist

- Tests were written before or alongside implementation.
- Unit tests pass locally.
- Integration tests pass when applicable.
- Safety-critical failure modes were considered.
- Documentation was updated when behavior changed.
- No secrets, real phone numbers, API keys, or private sensor data are committed.

## Safety-Critical Coding Guidelines

- Detection code must expose confidence, timestamp, and data source when possible.
- Notification code must be idempotent within a configured cooldown window.
- Sensor adapters must handle unavailable, delayed, malformed, or noisy input.
- Configuration defaults must be conservative for child and pet safety.
- Logs must not expose private user information.

## Agent Instructions

When modifying this repository:

- Read existing tests and requirements before editing implementation.
- Add or update tests first for behavioral changes.
- Keep changes scoped to the requested behavior.
- Do not relax alert thresholds, validation, or safety checks without explicit justification.
- Prefer deterministic tests over time-dependent or network-dependent tests.
- If a CI failure is unrelated to the change, document it clearly instead of hiding it.
