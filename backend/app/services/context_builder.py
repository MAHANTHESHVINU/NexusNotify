from app.models.notification_context import NotificationContext
from app.repositories.dataset_repository import DatasetRepository


class ContextBuilder:
    """
    Builds a complete NotificationContext from repository data.
    """

    def __init__(self):
        self.repo = DatasetRepository()

    def build(self, message_id: str):

        message = self.repo.get_message(message_id)

        if message is None:
            return None

        user = self.repo.get_user(message.user_id)

        history = self.repo.get_history(message.user_id)

        events = self.repo.get_events(message.message_id)

        return NotificationContext(
            message=message,
            user=user,
            history=[],
            events=events,
        )