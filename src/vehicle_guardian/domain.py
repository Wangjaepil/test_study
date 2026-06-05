from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum


class OccupantType(StrEnum):
    NONE = "none"
    CHILD = "child"
    PET = "pet"
    UNKNOWN_LIVING_OCCUPANT = "unknown_living_occupant"


class IgnitionState(StrEnum):
    OFF = "off"
    ACCESSORY = "accessory"
    ON = "on"


class AlertDecision(StrEnum):
    REQUIRED = "required"
    NOT_REQUIRED = "not_required"


@dataclass(frozen=True)
class DetectionResult:
    occupant_type: OccupantType
    confidence: float
    source: str
    detected_at: datetime

    @property
    def requires_attention(self) -> bool:
        return self.occupant_type in {
            OccupantType.CHILD,
            OccupantType.PET,
            OccupantType.UNKNOWN_LIVING_OCCUPANT,
        }


@dataclass(frozen=True)
class VehicleState:
    is_parked: bool
    ignition_state: IgnitionState
    driver_present: bool
    measured_at: datetime

    @property
    def is_unattended(self) -> bool:
        return (
            self.is_parked and self.ignition_state is IgnitionState.OFF and not self.driver_present
        )


def decide_alert(
    *,
    detection: DetectionResult,
    vehicle_state: VehicleState,
) -> AlertDecision:
    if detection.requires_attention and vehicle_state.is_unattended:
        return AlertDecision.REQUIRED

    return AlertDecision.NOT_REQUIRED
