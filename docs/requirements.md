# Requirements

## Product Goal

Build a Python system that detects whether a child or pet remains inside a vehicle and alerts responsible users quickly and reliably.

## Assumptions

- The system may use one or more inputs such as camera frames, cabin sensors, seat sensors, microphone signals, door events, ignition state, GPS state, or mobile app signals.
- The first version should be designed so sensor integrations can be simulated in tests.
- Alerts may be delivered through configurable channels such as mobile push, SMS, email, vehicle horn/lights, or an external webhook.

## Functional Requirements

### Occupant Detection

- `FR-OD-001`: The system shall detect the possible presence of a child inside the vehicle.
- `FR-OD-002`: The system shall detect the possible presence of a pet inside the vehicle.
- `FR-OD-003`: The system shall classify detection results as `none`, `child`, `pet`, or `unknown_living_occupant` when confidence is insufficient for a specific class.
- `FR-OD-004`: The system shall provide a confidence score for each detection result.
- `FR-OD-005`: The system shall include the input source and detection timestamp in each detection result.
- `FR-OD-006`: The system shall support simulated sensor input for tests and demos.

### Vehicle State Awareness

- `FR-VS-001`: The system shall determine whether the vehicle is parked.
- `FR-VS-002`: The system shall determine whether the ignition or drive state indicates the vehicle is unattended.
- `FR-VS-003`: The system shall detect recent door open and close events when available.
- `FR-VS-004`: The system shall combine occupant detection with vehicle state before triggering an alert.

### Alerting

- `FR-AL-001`: The system shall trigger an alert when a child or pet is detected in an unattended parked vehicle.
- `FR-AL-002`: The system shall support configurable alert channels.
- `FR-AL-003`: The system shall escalate alerts when the first alert is not acknowledged within a configured time.
- `FR-AL-004`: The system shall prevent duplicate alerts within a configurable cooldown window.
- `FR-AL-005`: The system shall record alert attempts, acknowledgement state, timestamp, and target channel.
- `FR-AL-006`: The system shall allow alert acknowledgement through a supported interface or simulated test hook.

### Configuration

- `FR-CF-001`: The system shall provide default safety-oriented thresholds.
- `FR-CF-002`: The system shall allow detection threshold, alert delay, escalation delay, and cooldown duration to be configured.
- `FR-CF-003`: The system shall validate configuration values at startup.
- `FR-CF-004`: The system shall fail safely when required configuration is missing or invalid.

### Observability

- `FR-OB-001`: The system shall log detection decisions, alert decisions, and delivery outcomes.
- `FR-OB-002`: The system shall expose enough structured status information for tests and operational diagnostics.
- `FR-OB-003`: The system shall avoid logging personally identifiable information.

### Testing

- `FR-TS-001`: The system shall include unit tests for detection decision logic.
- `FR-TS-002`: The system shall include unit tests for alert cooldown and escalation behavior.
- `FR-TS-003`: The system shall include integration tests for the flow from sensor input to alert decision.
- `FR-TS-004`: The system shall include tests for malformed, missing, stale, and contradictory sensor data.

## Non-Functional Requirements

### Safety

- `NFR-SF-001`: The system shall prioritize reducing false negatives over reducing false positives.
- `NFR-SF-002`: The system shall use conservative defaults when confidence is uncertain.
- `NFR-SF-003`: The system shall preserve an auditable decision trail for safety-critical alerts.

### Reliability

- `NFR-RL-001`: The system shall continue operating when a non-critical sensor source is unavailable.
- `NFR-RL-002`: The system shall handle network failures during alert delivery and retry according to policy.
- `NFR-RL-003`: The system shall avoid crashing on malformed sensor input.

### Performance

- `NFR-PF-001`: The system shall make an alert decision within 5 seconds after receiving all required unattended-vehicle signals.
- `NFR-PF-002`: The system shall support local test execution without requiring physical sensors.
- `NFR-PF-003`: The system shall keep detection and alert decision logic deterministic in tests.

### Security

- `NFR-SC-001`: The system shall not commit secrets, tokens, or private contact information.
- `NFR-SC-002`: The system shall load secrets from environment variables or a secure secret manager.
- `NFR-SC-003`: The system shall validate external webhook URLs and alert targets.

### Privacy

- `NFR-PR-001`: The system shall minimize storage of raw camera, microphone, or location data.
- `NFR-PR-002`: The system shall redact sensitive information from logs.
- `NFR-PR-003`: The system shall provide a configurable retention policy for event records.

### Maintainability

- `NFR-MT-001`: The system shall use modular components for sensors, detection, alerting, and configuration.
- `NFR-MT-002`: The system shall maintain clear boundaries between domain logic and external integrations.
- `NFR-MT-003`: The system shall include documentation for local development, testing, and release preparation.

### Compatibility

- `NFR-CP-001`: The system shall support Python 3.11 and newer.
- `NFR-CP-002`: The system shall run in CI on the latest available Ubuntu GitHub Actions runner.
- `NFR-CP-003`: The system shall be structured so it can later integrate with embedded devices, mobile apps, or cloud services.

## Acceptance Criteria For Initial Version

- Given simulated sensor input indicating a child in a parked unattended vehicle, the system creates an alert decision.
- Given simulated sensor input indicating a pet in a parked unattended vehicle, the system creates an alert decision.
- Given simulated sensor input indicating no occupant, the system does not create an alert.
- Given repeated positive detections within the cooldown window, the system does not create duplicate alerts.
- Given an unacknowledged alert beyond the escalation delay, the system creates an escalation event.
- Given malformed sensor input, the system records a safe diagnostic result and does not crash.
