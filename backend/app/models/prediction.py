from dataclasses import dataclass, field


@dataclass(slots=True)
class Prediction:

    message_id: str

    action: str

    message_type: str

    reason: str

    confidence: float

    evidence_message_ids: list[str] = field(default_factory=list)