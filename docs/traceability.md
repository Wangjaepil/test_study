# Bidirectional Traceability Matrix

This file connects requirements, tests, implementation, and release evidence. Update it in the same pull request as any requirement, test, or production behavior change.

## Status Values

- `Planned`: requirement is accepted but not implemented
- `Tested`: test coverage exists
- `Implemented`: production code exists
- `Verified`: CI or release validation evidence exists

## Requirement To Evidence

| Requirement ID | Development Milestone | Test Evidence | Implementation Evidence | Status |
| --- | --- | --- | --- | --- |
| `FR-OD-001` | M1 | Planned | Planned | Planned |
| `FR-OD-002` | M1 | Planned | Planned | Planned |
| `FR-OD-003` | M1 | [tests/unit/test_domain.py](../tests/unit/test_domain.py) | [src/vehicle_guardian/domain.py](../src/vehicle_guardian/domain.py) | Tested |
| `FR-OD-004` | M1 | [tests/unit/test_domain.py](../tests/unit/test_domain.py) | [src/vehicle_guardian/domain.py](../src/vehicle_guardian/domain.py) | Tested |
| `FR-OD-005` | M1 | [tests/unit/test_domain.py](../tests/unit/test_domain.py) | [src/vehicle_guardian/domain.py](../src/vehicle_guardian/domain.py) | Tested |
| `FR-OD-006` | M3 | Planned | Planned | Planned |
| `FR-VS-001` | M1 | Planned | Planned | Planned |
| `FR-VS-002` | M1 | Planned | Planned | Planned |
| `FR-VS-003` | M3 | Planned | Planned | Planned |
| `FR-VS-004` | M1 | Planned | Planned | Planned |
| `FR-AL-001` | M1 | Planned | Planned | Planned |
| `FR-AL-002` | M5 | Planned | Planned | Planned |
| `FR-AL-003` | M2 | Planned | Planned | Planned |
| `FR-AL-004` | M2 | Planned | Planned | Planned |
| `FR-AL-005` | M2 | Planned | Planned | Planned |
| `FR-AL-006` | M2 | Planned | Planned | Planned |
| `FR-CF-001` | M4 | Planned | Planned | Planned |
| `FR-CF-002` | M4 | Planned | Planned | Planned |
| `FR-CF-003` | M4 | Planned | Planned | Planned |
| `FR-CF-004` | M4 | Planned | Planned | Planned |
| `FR-OB-001` | M5 | Planned | Planned | Planned |
| `FR-OB-002` | M5 | Planned | Planned | Planned |
| `FR-OB-003` | M6 | Planned | Planned | Planned |
| `FR-TS-001` | M1 | Planned | Planned | Planned |
| `FR-TS-002` | M2 | Planned | Planned | Planned |
| `FR-TS-003` | M3 | Planned | Planned | Planned |
| `FR-TS-004` | M3 | Planned | Planned | Planned |
| `NFR-SF-001` | M1 | Planned | Planned | Planned |
| `NFR-SF-002` | M1 | Planned | Planned | Planned |
| `NFR-SF-003` | M2 | Planned | Planned | Planned |
| `NFR-RL-001` | M3 | Planned | Planned | Planned |
| `NFR-RL-002` | M2, M5 | Planned | Planned | Planned |
| `NFR-RL-003` | M3 | Planned | Planned | Planned |
| `NFR-PF-001` | M6 | Planned | Planned | Planned |
| `NFR-PF-002` | M3 | Planned | Planned | Planned |
| `NFR-PF-003` | M1 | [tests/unit/test_domain.py](../tests/unit/test_domain.py) | [src/vehicle_guardian/domain.py](../src/vehicle_guardian/domain.py) | Tested |
| `NFR-SC-001` | M6 | Planned | Planned | Planned |
| `NFR-SC-002` | M4 | Planned | Planned | Planned |
| `NFR-SC-003` | M5 | Planned | Planned | Planned |
| `NFR-PR-001` | M6 | Planned | Planned | Planned |
| `NFR-PR-002` | M6 | Planned | Planned | Planned |
| `NFR-PR-003` | M6 | Planned | Planned | Planned |
| `NFR-MT-001` | M1-M6 | Planned | Project structure | Planned |
| `NFR-MT-002` | M1-M6 | Planned | Project structure | Planned |
| `NFR-MT-003` | M6 | [docs/development-plan.md](development-plan.md) | [releases/index.md](../releases/index.md) | Tested |
| `NFR-CP-001` | M6 | [.github/workflows/pr-validation.yml](../.github/workflows/pr-validation.yml) | [pyproject.toml](../pyproject.toml) | Tested |
| `NFR-CP-002` | M6 | [.github/workflows/pr-validation.yml](../.github/workflows/pr-validation.yml) | [.github/workflows/pr-validation.yml](../.github/workflows/pr-validation.yml) | Tested |
| `NFR-CP-003` | M6 | Planned | Project structure | Planned |

## Evidence To Requirements

| Evidence | Requirement IDs |
| --- | --- |
| [src/vehicle_guardian/domain.py](../src/vehicle_guardian/domain.py) | `FR-OD-003`, `FR-OD-004`, `FR-OD-005`, `NFR-PF-003` |
| [tests/unit/test_domain.py](../tests/unit/test_domain.py) | `FR-OD-003`, `FR-OD-004`, `FR-OD-005`, `NFR-PF-003` |
| [.github/workflows/pr-validation.yml](../.github/workflows/pr-validation.yml) | `NFR-CP-001`, `NFR-CP-002` |
| [pyproject.toml](../pyproject.toml) | `NFR-CP-001` |
| [docs/development-plan.md](development-plan.md) | `NFR-MT-003` |
| [releases/index.md](../releases/index.md) | `NFR-MT-003` |

## Pull Request Rule

Every pull request should answer both questions:

- Which requirement IDs does this change satisfy or affect?
- Which tests, implementation files, or release evidence prove the requirement status?
