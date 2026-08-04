from app.models.notification_context import NotificationContext


class MessageClassifier:

    SPAM_WORDS = {
        "spam",
        "junk",
        "unsubscribe",
        "click here",
        "limited offer",
        "free gift",
    }

    SCAM_WORDS = {
        "winner",
        "lottery",
        "prize",
        "account blocked",
        "bank transfer",
        "verify account",
        "urgent payment",
        "password",
        "otp",
    }

    PROMOTION_WORDS = {
        "offer",
        "discount",
        "sale",
        "coupon",
        "cashback",
        "limited time",
        "deal",
    }

    PAYMENT_WORDS = {
        "credited",
        "debited",
        "transaction",
        "payment",
        "upi",
        "bank",
        "invoice",
        "due",
        "paid",
        "amount",
    }

    EVENT_WORDS = {
        "meeting",
        "schedule",
        "appointment",
        "event",
        "party",
        "conference",
        "tomorrow",
        "today",
        "tonight",
    }

    GREETING_WORDS = {
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening",
        "happy birthday",
    }

    URGENT_WORDS = {
        "urgent",
        "asap",
        "immediately",
        "important",
        "deadline",
        "emergency",
    }

    def classify(
        self,
        context: NotificationContext,
    ) -> str:

        text = (
            context.message.message_text or ""
        ).strip().lower()

        if not text:
            return "unknown"

        if context.message.forwarded_count > 0:
            return "forward"

        if any(word in text for word in self.SCAM_WORDS):
            return "scam"

        if any(word in text for word in self.SPAM_WORDS):
            return "spam"

        if any(word in text for word in self.PROMOTION_WORDS):
            return "promotion"

        if any(word in text for word in self.PAYMENT_WORDS):
            return "payment"

        if any(word in text for word in self.EVENT_WORDS):
            return "event"

        if any(word in text for word in self.GREETING_WORDS):
            return "greeting"

        if context.message.business_id or context.message.is_business_message():
            return "business_update"

        if any(word in text for word in self.URGENT_WORDS):
            return "urgent"

        return "personal"
