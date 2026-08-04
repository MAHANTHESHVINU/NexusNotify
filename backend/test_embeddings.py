from app.services.embeddings.embedding_service import EmbeddingService

service = EmbeddingService()

v1 = service.encode(
    "Your login code is 123456"
)

v2 = service.encode(
    "Verification code: 123456"
)

print(len(v1))
print(v1[:5])