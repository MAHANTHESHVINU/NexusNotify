from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(slots=True)
class Message:
    """
    Domain model representing a single incoming message.
    This maps directly to one record in messages.csv.
    """

    message_id: str
    user_id: str

    conversation_type: str

    group_id: Optional[str]
    business_id: Optional[str]
    sender_user_id: Optional[str]

    created_at: datetime

    message_text: Optional[str]

    media_type: Optional[str]
    media_id: Optional[str]

    forwarded_count: int

    @property
    def has_media(self) -> bool:
        return self.media_type is not None

    @property
    def is_group_message(self) -> bool:
        return self.conversation_type == "group"

    @property
    def is_business_message(self) -> bool:
        return self.conversation_type == "business"

    @property
    def is_forwarded(self) -> bool:
        return self.forwarded_count > 0