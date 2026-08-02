from typing import Any

import pandas as pd

from app.models.user import User


class UserMapper:
    """
    Converts pandas rows into User domain models.
    """

    @staticmethod
    def from_series(row: pd.Series) -> User:
        return User(
            user_id=str(row["user_id"]),

            do_not_disturb_window=UserMapper._optional(
                row.get("do_not_disturb_window")
            ),

            messages_opened_30d=int(row["messages_opened_30d"]),
            messages_replied_30d=int(row["messages_replied_30d"]),
            notifications_dismissed_30d=int(
                row["notifications_dismissed_30d"]
            ),
            messages_reported_30d=int(
                row["messages_reported_30d"]
            ),
        )

    @staticmethod
    def _optional(value: Any):
        if pd.isna(value):
            return None

        return value