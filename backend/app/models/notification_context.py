from dataclasses import dataclass, field
from typing import Optional, List

from app.models.message import Message
from app.models.user import User
from app.models.message_event import MessageEvent
from app.models.business import Business
from app.models.group import Group


@dataclass(slots=True)
class NotificationContext:
    """
    Complete AI context for making a notification decision.
    Every decision engine receives this object instead of raw CSV rows.
    """

    message: Message

    user: User

    business: Optional[Business] = None

    group: Optional[Group] = None

    history: List[Message] = field(default_factory=list)

    events: List[MessageEvent] = field(default_factory=list)

    # Derived features (computed later)
    spam_score: float = 0.0

    urgency_score: float = 0.0

    trust_score: float = 0.0

    fatigue_score: float = 0.0

    importance_score: float = 0.0

    explanation: Optional[str] = None