from pathlib import Path

import pandas as pd

from app.config.settings import settings
from app.mappers.message_mapper import MessageMapper
from app.mappers.user_mapper import UserMapper
from app.mappers.message_event_mapper import MessageEventMapper


class DatasetRepository:
    """
    Loads all hackathon datasets once and keeps them in memory.
    """

    def __init__(self):
        dataset_path = Path(settings.DATASET_PATH)

        if not dataset_path.is_absolute():
            dataset_path = (
                Path(__file__).resolve().parents[2] / dataset_path
            )

        self.dataset_path = dataset_path

        self.messages = self._load("messages.csv")
        self.users = self._load("users.csv")
        self.message_history = self._load("message_history.csv")
        self.message_events = self._load("message_events.csv")

    def _load(self, filename: str) -> pd.DataFrame:
        file_path = self.dataset_path / filename

        if not file_path.exists():
            raise FileNotFoundError(f"Dataset not found: {file_path}")

        return pd.read_csv(file_path)

    def get_messages(self) -> pd.DataFrame:
        return self.messages

    def get_message(self, message_id: str):
        result = self.messages[
            self.messages["message_id"] == message_id
        ]

        if result.empty:
            return None

        return MessageMapper.from_series(result.iloc[0])

    def get_user(self, user_id: str):
        result = self.users[
            self.users["user_id"] == user_id
        ]

        if result.empty:
            return None

        return UserMapper.from_series(result.iloc[0])

    def get_history(self, user_id: str):
        rows = self.message_history[
            self.message_history["user_id"] == user_id
        ]

        return [
            MessageMapper.from_series(row)
            for _, row in rows.iterrows()
        ]

    def get_events(self, message_id: str):
        rows = self.message_events[
            self.message_events["message_id"] == message_id
        ]

        return [
            MessageEventMapper.from_series(row)
            for _, row in rows.iterrows()
        ]