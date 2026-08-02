import pandas as pd

from app.models.prediction import Prediction
from app.repositories.dataset_repository import DatasetRepository

from app.services.context_builder import ContextBuilder
from app.services.scoring.feature_extractor import FeatureExtractor
from app.services.reasoning.decision_engine import DecisionEngine
from app.services.classification.message_classifier import MessageClassifier
from app.services.retrieval.evidence_retriever import EvidenceRetriever
from app.services.llm.reasoning_service import ReasoningService


class PredictionPipeline:

    def __init__(self):

        self.repo = DatasetRepository()

        self.builder = ContextBuilder()

        self.extractor = FeatureExtractor()

        self.engine = DecisionEngine()

        self.classifier = MessageClassifier()

        self.retriever = EvidenceRetriever()

        self.reasoner = ReasoningService()

    def run(self):

        predictions = []

        for _, row in self.repo.messages.iterrows():

            message_id = row["message_id"]

            context = self.builder.build(message_id)

            features = self.extractor.extract(context)

            decision = self.engine.decide(features)

            evidence = self.retriever.retrieve(context)

            prediction_data = {
                "action": decision.action,
                "message_type": self.classifier.classify(context),
                "reason": "; ".join(decision.reason),
                "confidence": decision.confidence,
                "evidence": [item["message_id"] for item in evidence],
            }

            # Use the LLM only for low-confidence predictions
            if prediction_data["confidence"] < 0.80:

                try:
                    prediction_data = self.reasoner.review_prediction(
                        context=context,
                        features=features,
                        prediction=prediction_data,
                    )

                except Exception as e:
                    print(
                        f"LLM review failed for {message_id}: {e}"
                    )

            prediction = Prediction(
                message_id=message_id,
                action=prediction_data["action"],
                message_type=prediction_data["message_type"],
                reason=prediction_data["reason"],
                confidence=prediction_data["confidence"],
                evidence_message_ids=[item["message_id"] for item in evidence]
            )

            predictions.append(prediction)

        return predictions