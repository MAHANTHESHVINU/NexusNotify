from dataclasses import dataclass

from app.models.decision_features import DecisionFeatures


@dataclass(slots=True)
class Decision:

    action: str

    confidence: float

    reason: list[str]


class DecisionEngine:

    def decide(
        self,
        features: DecisionFeatures,
    ) -> Decision:

        reasons = []

        if features.contains_otp_request:
            reasons.append(
                "OTP request detected"
            )

        if features.contains_credential_request:
            reasons.append(
                "Credential request detected"
            )

        if features.contains_urgency:
            reasons.append(
                "Urgency language detected"
            )

        if features.notification_fatigue > 0.50:
            reasons.append(
                "User has notification fatigue"
            )

        if features.risk_score >= 0.80:

            return Decision(
                action="SUPPRESS",
                confidence=0.95,
                reason=reasons,
            )

        if features.risk_score >= 0.50:

            return Decision(
                action="SUMMARIZE",
                confidence=0.80,
                reason=reasons,
            )

        return Decision(
            action="NOTIFY",
            confidence=0.70,
            reason=reasons,
        )