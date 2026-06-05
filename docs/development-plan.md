# Development Plan

## Strategy

Development follows TDD and keeps the domain logic independent from hardware, network providers, and UI integrations. The first milestones use simulated inputs so tests can drive behavior before physical sensors or notification providers are selected.

## Milestones

### M0 - Project Foundation

Status: Complete

Scope:

- Repository policy documents
- Requirements document
- Release page
- Pull request validation workflow
- Minimal Python package and unit test scaffold

Exit criteria:

- PR validation workflow exists
- Requirements have stable IDs
- Initial tests can be executed in CI

### M1 - Domain Decision Core

Status: Complete

Scope:

- Detection result model
- Vehicle state model
- Alert decision model
- Rule that combines occupant detection and unattended parked vehicle state
- Unit tests for positive, negative, and uncertain detection cases

Requirement coverage:

- `FR-OD-001`
- `FR-OD-002`
- `FR-OD-003`
- `FR-OD-004`
- `FR-OD-005`
- `FR-VS-001`
- `FR-VS-002`
- `FR-VS-004`
- `FR-AL-001`
- `NFR-SF-001`
- `NFR-SF-002`
- `NFR-PF-003`

### M2 - Alert Lifecycle

Status: Planned

Scope:

- Alert record model
- Cooldown policy
- Acknowledgement state
- Escalation policy
- Unit tests for duplicate prevention and escalation timing

Requirement coverage:

- `FR-AL-003`
- `FR-AL-004`
- `FR-AL-005`
- `FR-AL-006`
- `FR-TS-002`
- `NFR-SF-003`
- `NFR-RL-002`

### M3 - Simulated Sensors And Integration Flow

Status: Planned

Scope:

- Simulated sensor adapter
- Test fixtures for child, pet, no occupant, stale data, and malformed data
- Integration flow from sensor input to alert decision
- Diagnostics for missing or contradictory input

Requirement coverage:

- `FR-OD-006`
- `FR-VS-003`
- `FR-TS-003`
- `FR-TS-004`
- `NFR-RL-001`
- `NFR-RL-003`
- `NFR-PF-002`

### M4 - Configuration And Validation

Status: Planned

Scope:

- Configuration model
- Conservative defaults
- Startup validation
- Safe failure behavior
- Tests for invalid thresholds and missing required settings

Requirement coverage:

- `FR-CF-001`
- `FR-CF-002`
- `FR-CF-003`
- `FR-CF-004`
- `NFR-SC-002`

### M5 - Notification Ports

Status: Planned

Scope:

- Notification interface
- In-memory notification provider for tests
- Webhook provider skeleton
- Retry policy abstraction
- Validation for alert targets

Requirement coverage:

- `FR-AL-002`
- `FR-OB-001`
- `FR-OB-002`
- `NFR-RL-002`
- `NFR-SC-003`

### M6 - Privacy, Security, And Release Readiness

Status: Planned

Scope:

- Log redaction policy
- Secret handling documentation
- Event retention policy
- Release checklist hardening
- Coverage review and CI tuning

Requirement coverage:

- `FR-OB-003`
- `NFR-SC-001`
- `NFR-PR-001`
- `NFR-PR-002`
- `NFR-PR-003`
- `NFR-MT-003`
- `NFR-CP-001`
- `NFR-CP-002`
- `NFR-CP-003`

## TDD Delivery Loop

For each milestone:

1. Add or update traceability rows before implementation.
2. Write failing tests linked to requirement IDs.
3. Implement the smallest domain behavior needed.
4. Refactor without changing behavior.
5. Update traceability status.
6. Update `memory.md` with key decisions.

## Branch Plan

- Use `main` only for validated work.
- Use `feature/domain-decision-core` for M1.
- Use `feature/alert-lifecycle` for M2.
- Use `feature/simulated-sensors` for M3.
- Use `feature/configuration-validation` for M4.
- Use `feature/notification-ports` for M5.
- Use `release/0.1.0` for M6 and release preparation.
