from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

from app.models.notification_context import NotificationContext
from app.repositories.dataset_repository import DatasetRepository
from app.services.embeddings.embedding_service import EmbeddingService


class EvidenceRetriever:

    def __init__(self):

        self.repo = DatasetRepository()

        self.embedding_service = EmbeddingService()

        self.embeddings = {}

        for _, row in self.repo.messages.iterrows():

            text = row["message_text"]

            # Handle missing values
            if pd.isna(text):
                text = ""

            text = str(text)

            self.embeddings[row["message_id"]] = (
                self.embedding_service.encode(text)
            )

    def retrieve(
        self,
        context: NotificationContext,
        limit: int = 3,
    ) -> list[dict]:

        current_text = context.message.message_text

        if current_text is None:
            current_text = ""

        current_text = str(current_text)

        current_embedding = self.embedding_service.encode(
            current_text
        )

        scores = []

        for _, row in self.repo.messages.iterrows():

            if row["message_id"] == context.message.message_id:
                continue

            similarity = cosine_similarity(
                [current_embedding],
                [self.embeddings[row["message_id"]]]
            )[0][0]

            scores.append(
                {
                    "message_id": row["message_id"],
                    "message": "" if pd.isna(row["message_text"]) else str(row["message_text"]),
                    "score": round(float(similarity), 4),
                }
            )

        scores.sort(
            key=lambda x: x["score"],
            reverse=True,
        )

        return scores[:limit]