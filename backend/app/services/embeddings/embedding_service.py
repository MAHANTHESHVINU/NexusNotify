from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def encode(self, text: str):

        if text is None:
            text = ""

        text = str(text).strip()

        return self.model.encode(
            text,
            normalize_embeddings=True,
        )