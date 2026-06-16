from datetime import UTC, datetime, timedelta

from vehicle_guardian.domain import (
    AlertDecision,
    AlertLifecyclePolicy,
    AlertRecord,
    AlertStatus,
    DetectionResult,
    IgnitionState,
    OccupantType,
    VehicleState,
    decide_alert,
)

NOW = datetime(2026, 6, 5, tzinfo=UTC)
POLICY = AlertLifecyclePolicy(
    cooldown_duration=timedelta(minutes=10),
    escalation_delay=timedelta(minutes=5),
)


def test_child_detection_requires_attention() -> None:
    result = DetectionResult(
        occupant_type=OccupantType.CHILD,
        confidence=0.91,
        source="simulated_camera",
        detected_at=NOW,
    )

    assert result.requires_attention is True


def test_no_occupant_detection_does_not_require_attention() -> None:
    result = DetectionResult(
        occupant_type=OccupantType.NONE,
        confidence=0.99,
        source="simulated_camera",
        detected_at=NOW,
    )

    assert result.requires_attention is False


def test_parked_vehicle_with_child_requires_alert() -> None:
    detection = DetectionResult(
        occupant_type=OccupantType.CHILD,
        confidence=0.91,
        source="simulated_camera",
        detected_at=NOW,
    )
    vehicle = VehicleState(
        is_parked=True,
        ignition_state=IgnitionState.OFF,
        driver_present=False,
        measured_at=NOW,
    )

    decision = decide_alert(detection=detection, vehicle_state=vehicle)

    assert decision == AlertDecision.REQUIRED


def test_parked_vehicle_with_pet_requires_alert() -> None:
    detection = DetectionResult(
        occupant_type=OccupantType.PET,
        confidence=0.86,
        source="simulated_camera",
        detected_at=NOW,
    )
    vehicle = VehicleState(
        is_parked=True,
        ignition_state=IgnitionState.OFF,
        driver_present=False,
        measured_at=NOW,
    )

    decision = decide_alert(detection=detection, vehicle_state=vehicle)

    assert decision == AlertDecision.REQUIRED


def test_parked_vehicle_with_unknown_living_occupant_requires_alert() -> None:
    detection = DetectionResult(
        occupant_type=OccupantType.UNKNOWN_LIVING_OCCUPANT,
        confidence=0.62,
        source="simulated_camera",
        detected_at=NOW,
    )
    vehicle = VehicleState(
        is_parked=True,
        ignition_state=IgnitionState.OFF,
        driver_present=False,
        measured_at=NOW,
    )

    decision = decide_alert(detection=detection, vehicle_state=vehicle)

    assert decision == AlertDecision.REQUIRED


def test_parked_vehicle_with_no_occupant_does_not_require_alert() -> None:
    detection = DetectionResult(
        occupant_type=OccupantType.NONE,
        confidence=0.98,
        source="simulated_camera",
        detected_at=NOW,
    )
    vehicle = VehicleState(
        is_parked=True,
        ignition_state=IgnitionState.OFF,
        driver_present=False,
        measured_at=NOW,
    )

    decision = decide_alert(detection=detection, vehicle_state=vehicle)

    assert decision == AlertDecision.NOT_REQUIRED


def test_child_detection_does_not_alert_when_driver_is_present() -> None:
    detection = DetectionResult(
        occupant_type=OccupantType.CHILD,
        confidence=0.91,
        source="simulated_camera",
        detected_at=NOW,
    )
    vehicle = VehicleState(
        is_parked=True,
        ignition_state=IgnitionState.OFF,
        driver_present=True,
        measured_at=NOW,
    )

    decision = decide_alert(detection=detection, vehicle_state=vehicle)

    assert decision == AlertDecision.NOT_REQUIRED


def test_child_detection_does_not_alert_when_vehicle_is_not_parked() -> None:
    detection = DetectionResult(
        occupant_type=OccupantType.CHILD,
        confidence=0.91,
        source="simulated_camera",
        detected_at=NOW,
    )
    vehicle = VehicleState(
        is_parked=False,
        ignition_state=IgnitionState.ON,
        driver_present=True,
        measured_at=NOW,
    )

    decision = decide_alert(detection=detection, vehicle_state=vehicle)

    assert decision == AlertDecision.NOT_REQUIRED


def test_alert_record_captures_attempt_audit_information() -> None:
    alert = AlertRecord.create(
        occupant_type=OccupantType.CHILD,
        confidence=0.91,
        channel="sms",
        target="primary_guardian",
        created_at=NOW,
    )

    assert alert.status == AlertStatus.ACTIVE
    assert alert.occupant_type == OccupantType.CHILD
    assert alert.confidence == 0.91
    assert alert.channel == "sms"
    assert alert.target == "primary_guardian"
    assert alert.created_at == NOW
    assert alert.acknowledged_at is None
    assert alert.escalated_at is None


def test_recent_active_alert_blocks_duplicate_within_cooldown() -> None:
    previous_alert = AlertRecord.create(
        occupant_type=OccupantType.PET,
        confidence=0.87,
        channel="sms",
        target="primary_guardian",
        created_at=NOW,
    )

    assert previous_alert.is_duplicate_blocked(
        now=NOW + timedelta(minutes=9),
        policy=POLICY,
    )


def test_active_alert_allows_new_attempt_after_cooldown() -> None:
    previous_alert = AlertRecord.create(
        occupant_type=OccupantType.PET,
        confidence=0.87,
        channel="sms",
        target="primary_guardian",
        created_at=NOW,
    )

    assert not previous_alert.is_duplicate_blocked(
        now=NOW + timedelta(minutes=11),
        policy=POLICY,
    )


def test_acknowledged_alert_does_not_block_duplicate() -> None:
    previous_alert = AlertRecord.create(
        occupant_type=OccupantType.CHILD,
        confidence=0.94,
        channel="sms",
        target="primary_guardian",
        created_at=NOW,
    ).acknowledge(at=NOW + timedelta(minutes=1))

    assert previous_alert.status == AlertStatus.ACKNOWLEDGED
    assert not previous_alert.is_duplicate_blocked(
        now=NOW + timedelta(minutes=2),
        policy=POLICY,
    )


def test_unacknowledged_alert_requires_escalation_after_delay() -> None:
    alert = AlertRecord.create(
        occupant_type=OccupantType.CHILD,
        confidence=0.92,
        channel="sms",
        target="primary_guardian",
        created_at=NOW,
    )

    assert alert.requires_escalation(
        now=NOW + timedelta(minutes=6),
        policy=POLICY,
    )


def test_unacknowledged_alert_does_not_escalate_before_delay() -> None:
    alert = AlertRecord.create(
        occupant_type=OccupantType.CHILD,
        confidence=0.92,
        channel="sms",
        target="primary_guardian",
        created_at=NOW,
    )

    assert not alert.requires_escalation(
        now=NOW + timedelta(minutes=4),
        policy=POLICY,
    )


def test_acknowledged_alert_does_not_require_escalation() -> None:
    alert = AlertRecord.create(
        occupant_type=OccupantType.CHILD,
        confidence=0.92,
        channel="sms",
        target="primary_guardian",
        created_at=NOW,
    ).acknowledge(at=NOW + timedelta(minutes=1))

    assert not alert.requires_escalation(
        now=NOW + timedelta(minutes=6),
        policy=POLICY,
    )


def test_escalated_alert_records_escalation_timestamp() -> None:
    alert = AlertRecord.create(
        occupant_type=OccupantType.PET,
        confidence=0.84,
        channel="sms",
        target="primary_guardian",
        created_at=NOW,
    )

    escalated = alert.escalate(at=NOW + timedelta(minutes=6))

    assert escalated.status == AlertStatus.ESCALATED
    assert escalated.escalated_at == NOW + timedelta(minutes=6)
