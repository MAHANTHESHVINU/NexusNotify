from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class User:
    """
    Domain model representing a user's notification behaviour.
    This maps directly to one record in users.csv.
    """

    user_id: str

    do_not_disturb_window: Optional[str]

    messages_opened_30d: int
    messages_replied_30d: int
    notifications_dismissed_30d: int
    messages_reported_30d: int

    @property
    def engagement_score(self) -> float:
        """
        Estimate how engaged the user is.
        """
        total = self.messages_opened_30d + self.messages_replied_30d

        if total == 0:
            return 0.0

        return round(
            self.messages_replied_30d / total,
            2
        )

    @property
    def fatigue_score(self) -> int:
        """
        Notification fatigue indicator.
        """
        return self.notifications_dismissed_30d

    @property
    def spam_sensitivity(self) -> int:
        """
        Number of reported messages.
        """
        return self.messages_reported_30d

    @property
    def has_quiet_hours(self) -> bool:
        return self.do_not_disturb_window is not None