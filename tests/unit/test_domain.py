from datetime import UTC, datetime

from vehicle_guardian.domain import (
    AlertDecision,
    DetectionResult,
    IgnitionState,
    OccupantType,
    VehicleState,
    decide_alert,
)

NOW = datetime(2026, 6, 5, tzinfo=UTC)


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
