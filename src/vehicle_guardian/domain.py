from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum


class OccupantType(StrEnum):
    NONE = "none"
    CHILD = "child"
    PET = "pet"
    UNKNOWN_LIVING_OCCUPANT = "unknown_living_occupant"


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
