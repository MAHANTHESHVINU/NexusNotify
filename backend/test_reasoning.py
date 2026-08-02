from app.services.context_builder import ContextBuilder
from app.services.scoring.feature_extractor import FeatureExtractor

from app.services.llm.reasoning_service import ReasoningService


builder = ContextBuilder()

extractor = FeatureExtractor()

reasoner = ReasoningService()


context = builder.build("msg_091")

features = extractor.extract(context)

prediction = {
    "action": "SUPPRESS",
    "message_type": "PHISHING",
    "confidence": 0.72,
    "reason": "Rule-based prediction",
}

response = reasoner.review_prediction(
    context=context,
    features=features,
    prediction=prediction,
)

print(response)