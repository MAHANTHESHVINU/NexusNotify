from app.services.context_builder import ContextBuilder
from app.services.retrieval.evidence_retriever import EvidenceRetriever

builder = ContextBuilder()
retriever = EvidenceRetriever()

context = builder.build("msg_091")

results = retriever.retrieve(context)

for item in results:
    print(item)