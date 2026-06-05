# Project Memory

This file is active project memory. Update it whenever the team makes a durable decision, changes scope, learns an important constraint, or completes a milestone.

## Current Objective

Build a Python-based vehicle safety system that detects children or pets left inside a vehicle and sends timely alerts.

## Active Development Method

- TDD is mandatory for behavior changes.
- Requirements must have stable IDs.
- Bidirectional traceability is required between requirements, tests, implementation, and release evidence.
- Pull requests must pass GitHub Actions validation before merge.

## Key Decisions

| Date | Decision | Reason |
| --- | --- | --- |
| 2026-06-05 | Python 3.11+ is the supported runtime. | Keeps compatibility modern while staying broadly deployable. |
| 2026-06-05 | Domain logic starts independent from physical sensors. | Enables TDD with simulated inputs before hardware integration. |
| 2026-06-05 | False negatives are the highest safety risk. | The product is safety-critical for children and pets. |
| 2026-06-05 | `docs/traceability.md` is the source for requirement evidence mapping. | Ensures bidirectional traceability for review and release validation. |

## Current Milestone

M1 - Domain Decision Core

Next focus:

- Add vehicle state model.
- Add alert decision model.
- Write tests for child, pet, unknown living occupant, and no occupant cases in parked unattended vehicles.

## Working Agreements

- Keep `memory.md` updated in every meaningful planning or implementation PR.
- Keep `docs/requirements.md` as the source of requirement text.
- Keep `docs/traceability.md` as the source of evidence links and coverage status.
- Keep `docs/development-plan.md` as the source of milestone scope and sequencing.
- Avoid committing secrets, real contact details, raw sensor recordings, or personally identifiable information.

## Open Questions

- Which sensor inputs will be used first: camera, seat sensor, microphone, door event, ignition state, or mobile app state?
- Which alert channel should be implemented first: push, SMS, email, webhook, horn/lights, or local demo output?
- What deployment target is expected first: laptop demo, embedded device, cloud service, or mobile-connected prototype?
