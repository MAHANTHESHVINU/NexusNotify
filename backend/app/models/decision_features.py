from dataclasses import dataclass


@dataclass(slots=True)
class DecisionFeatures:
    contains_urgency: bool
    contains_otp_request: bool
    contains_credential_request: bool

    user_engagement: float
    notification_fatigue: float

    forwarding_risk: int

    risk_score: float = 0.0