from app.models.notification_context import NotificationContext


class MessageClassifier:

    PHISHING_WORDS = {
        "otp",
        "verification code",
        "login code",
        "password",
        "pin",
        "verify",
    }

    PROMOTION_WORDS = {
        "offer",
        "discount",
        "sale",
        "coupon",
        "cashback",
        "limited time",
    }

    TRANSACTION_WORDS = {
        "credited",
        "debited",
        "transaction",
        "payment",
        "upi",
        "bank",
    }

    REMINDER_WORDS = {
        "reminder",
        "meeting",
        "schedule",
        "appointment",
        "tomorrow",
    }

    def classify(
        self,
        context: NotificationContext,
    ) -> str:

        text = (
            context.message.message_text or ""
        ).lower()

        if any(word in text for word in self.PHISHING_WORDS):
            return "PHISHING"

        if any(word in text for word in self.TRANSACTION_WORDS):
            return "TRANSACTION"

        if any(word in text for word in self.PROMOTION_WORDS):
            return "PROMOTION"

        if any(word in text for word in self.REMINDER_WORDS):
            return "REMINDER"

        if context.message.business_id:
            return "BUSINESS"

        if context.message.group_id:
            return "GROUP"

        return "PERSONAL"