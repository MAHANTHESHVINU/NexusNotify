from app.models.notification_context import NotificationContext
from app.models.decision_features import DecisionFeatures


class FeatureExtractor:

    URGENCY_WORDS = {
        "urgent",
        "today",
        "immediately",
        "expire",
        "expired",
        "now",
        "important",
        "action required",
    }

    OTP_WORDS = {
        "otp",
        "verification code",
        "login code",
        "6 digit",
        "one time password",
    }

    CREDENTIAL_WORDS = {
        "password",
        "pin",
        "login code",
        "verification code",
        "otp",
    }

    def extract(self, context: NotificationContext) -> DecisionFeatures:

        text = (context.message.message_text or "").lower()

        contains_urgency = any(
            word in text for word in self.URGENCY_WORDS
        )

        contains_otp = any(
            word in text for word in self.OTP_WORDS
        )

        contains_credentials = any(
            word in text for word in self.CREDENTIAL_WORDS
        )

        engagement = context.user.engagement_score

        dismissed = context.user.notifications_dismissed_30d
        opened = context.user.messages_opened_30d

        total = max(dismissed + opened, 1)
        fatigue = dismissed / total

        features = DecisionFeatures(
            contains_urgency=contains_urgency,
            contains_otp_request=contains_otp,
            contains_credential_request=contains_credentials,
            user_engagement=engagement,
            notification_fatigue=fatigue,
            forwarding_risk=context.message.forwarded_count,
        )

        features.risk_score = self.calculate_risk_score(features)

        return features

    def calculate_risk_score(
        self,
        features: DecisionFeatures,
    ) -> float:

        score = 0.0

        if features.contains_urgency:
            score += 0.25

        if features.contains_otp_request:
            score += 0.35

        if features.contains_credential_request:
            score += 0.25

        if features.forwarding_risk > 3:
            score += 0.15

        return min(score, 1.0)