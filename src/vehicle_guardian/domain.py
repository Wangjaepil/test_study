from dataclasses import dataclass
from datetime import datetime, timedelta
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


class AlertStatus(StrEnum):
    ACTIVE = "active"
    ACKNOWLEDGED = "acknowledged"
    ESCALATED = "escalated"


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


@dataclass(frozen=True)
class AlertLifecyclePolicy:
    cooldown_duration: timedelta
    escalation_delay: timedelta


@dataclass(frozen=True)
class AlertRecord:
    occupant_type: OccupantType
    confidence: float
    channel: str
    target: str
    created_at: datetime
    status: AlertStatus
    acknowledged_at: datetime | None = None
    escalated_at: datetime | None = None

    @classmethod
    def create(
        cls,
        *,
        occupant_type: OccupantType,
        confidence: float,
        channel: str,
        target: str,
        created_at: datetime,
    ) -> "AlertRecord":
        return cls(
            occupant_type=occupant_type,
            confidence=confidence,
            channel=channel,
            target=target,
            created_at=created_at,
            status=AlertStatus.ACTIVE,
        )

    def acknowledge(self, *, at: datetime) -> "AlertRecord":
        return AlertRecord(
            occupant_type=self.occupant_type,
            confidence=self.confidence,
            channel=self.channel,
            target=self.target,
            created_at=self.created_at,
            status=AlertStatus.ACKNOWLEDGED,
            acknowledged_at=at,
            escalated_at=self.escalated_at,
        )

    def escalate(self, *, at: datetime) -> "AlertRecord":
        return AlertRecord(
            occupant_type=self.occupant_type,
            confidence=self.confidence,
            channel=self.channel,
            target=self.target,
            created_at=self.created_at,
            status=AlertStatus.ESCALATED,
            acknowledged_at=self.acknowledged_at,
            escalated_at=at,
        )

    def is_duplicate_blocked(self, *, now: datetime, policy: AlertLifecyclePolicy) -> bool:
        if self.status is not AlertStatus.ACTIVE:
            return False

        return now - self.created_at < policy.cooldown_duration

    def requires_escalation(self, *, now: datetime, policy: AlertLifecyclePolicy) -> bool:
        if self.status is not AlertStatus.ACTIVE:
            return False

        return now - self.created_at >= policy.escalation_delay


def decide_alert(
    *,
    detection: DetectionResult,
    vehicle_state: VehicleState,
) -> AlertDecision:
    if detection.requires_attention and vehicle_state.is_unattended:
        return AlertDecision.REQUIRED

    return AlertDecision.NOT_REQUIRED
