from datetime import UTC, datetime

from vehicle_guardian.domain import DetectionResult, OccupantType


def test_child_detection_requires_attention() -> None:
    result = DetectionResult(
        occupant_type=OccupantType.CHILD,
        confidence=0.91,
        source="simulated_camera",
        detected_at=datetime(2026, 6, 5, tzinfo=UTC),
    )

    assert result.requires_attention is True


def test_no_occupant_detection_does_not_require_attention() -> None:
    result = DetectionResult(
        occupant_type=OccupantType.NONE,
        confidence=0.99,
        source="simulated_camera",
        detected_at=datetime(2026, 6, 5, tzinfo=UTC),
    )

    assert result.requires_attention is False
