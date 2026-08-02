from dataclasses import dataclass


@dataclass(slots=True)
class MessageEvent:
    """
    Represents how a user interacted with a notification.
    Maps directly to one row in message_events.csv.
    """

    user_id: str
    message_id: str

    message_opened: bool
    message_replied: bool

    reaction_time_minutes: int

    notification_dismissed: bool
    muted_after_message: bool
    message_reported: bool

    @property
    def is_engaged(self) -> bool:
        """User interacted with the message."""
        return self.message_opened or self.message_replied

    @property
    def is_negative_feedback(self) -> bool:
        """User gave a negative signal."""
        return (
            self.notification_dismissed
            or self.muted_after_message
            or self.message_reported
        )

    @property
    def response_speed(self) -> str:
        """
        Categorize response time.
        """
        if self.reaction_time_minutes <= 5:
            return "fast"

        if self.reaction_time_minutes <= 30:
            return "normal"

        return "slow"