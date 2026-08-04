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
            reasons.append(
                "High risk score indicates scam or spam"
            )

            return Decision(
                action="mute",
                confidence=0.95,
                reason=reasons,
            )

        if features.risk_score >= 0.50:
            reasons.append(
                "Moderate risk score suggests lower priority"
            )

            return Decision(
                action="digest",
                confidence=0.80,
                reason=reasons,
            )

        if features.contains_otp_request or features.contains_credential_request:
            reasons.append(
                "Sensitive security-related content"
            )

            return Decision(
                action="notify",
                confidence=0.88,
                reason=reasons,
            )

        if features.contains_urgency:
            return Decision(
                action="notify",
                confidence=0.85,
                reason=reasons,
            )

        if features.notification_fatigue > 0.50:
            return Decision(
                action="digest",
                confidence=0.72,
                reason=reasons,
            )

        return Decision(
            action="notify",
            confidence=0.75,
            reason=reasons or ["Standard relevance prediction"],
        )
