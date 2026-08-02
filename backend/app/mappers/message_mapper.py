from datetime import datetime
from typing import Any

import pandas as pd

from app.models.message import Message


class MessageMapper:
    """
    Converts pandas rows into Message domain models.
    """

    @staticmethod
    def from_series(row: pd.Series) -> Message:
        return Message(
            message_id=str(row["message_id"]),
            user_id=str(row["user_id"]),

            conversation_type=str(row["conversation_type"]),

            group_id=MessageMapper._optional(row.get("group_id")),
            business_id=MessageMapper._optional(row.get("business_id")),
            sender_user_id=MessageMapper._optional(row.get("sender_user_id")),

            created_at=pd.to_datetime(row["created_at"]),

            message_text=MessageMapper._optional(row.get("message_text")),

            media_type=MessageMapper._optional(row.get("media_type")),
            media_id=MessageMapper._optional(row.get("media_id")),

            forwarded_count=int(row["forwarded_count"]),
        )

    @staticmethod
    def _optional(value: Any):
        if pd.isna(value):
            return None

        return value