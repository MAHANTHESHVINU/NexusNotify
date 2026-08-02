import pandas as pd

from app.models.message_event import MessageEvent


class MessageEventMapper:
    @staticmethod
    def from_series(row: pd.Series) -> MessageEvent:
        return MessageEvent(
            user_id=str(row["user_id"]),
            message_id=str(row["message_id"]),

            message_opened=bool(row["message_opened"]),
            message_replied=bool(row["message_replied"]),

            reaction_time_minutes=int(
                row["reaction_time_minutes"]
            ),

            notification_dismissed=bool(
                row["notification_dismissed"]
            ),

            muted_after_message=bool(
                row["muted_after_message"]
            ),

            message_reported=bool(
                row["message_reported"]
            ),
        )