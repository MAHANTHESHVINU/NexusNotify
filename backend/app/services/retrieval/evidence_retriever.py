from app.models.notification_context import NotificationContext
from app.repositories.dataset_repository import DatasetRepository


class EvidenceRetriever:

    def __init__(self):

        self.repo = DatasetRepository()

    def retrieve(
        self,
        context: NotificationContext,
        limit: int = 3,
    ) -> list[str]:

        current = (
            context.message.message_text or ""
        ).lower()

        words = set(current.split())

        scores = []

        for _, row in self.repo.messages.iterrows():

            if (
                row["message_id"]
                == context.message.message_id
            ):
                continue

            text = (
                str(row["message_text"])
                .lower()
            )

            overlap = len(
                words.intersection(
                    text.split()
                )
            )

            if overlap > 3:
                scores.append(
                    (
                        row["message_id"],
                        overlap,
                    )
                )

        scores.sort(
            key=lambda x: x[1],
            reverse=True,
        )

        return [
            x[0]
            for x in scores[:limit]
        ]