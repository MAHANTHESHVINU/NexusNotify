import pandas as pd

from app.models.prediction import Prediction
from app.repositories.dataset_repository import DatasetRepository
from app.services.context_builder import ContextBuilder
from app.services.scoring.feature_extractor import FeatureExtractor
from app.services.reasoning.decision_engine import DecisionEngine
from app.services.classification.message_classifier import MessageClassifier
from app.services.retrieval.evidence_retriever import EvidenceRetriever

class PredictionPipeline:

    def __init__(self):

        self.repo = DatasetRepository()

        self.builder = ContextBuilder()

        self.extractor = FeatureExtractor()

        self.engine = DecisionEngine()

        self.classifier = MessageClassifier()

        self.retriever = EvidenceRetriever()

    def run(self):

        predictions = []

        for _, row in self.repo.messages.iterrows():

            message_id = row["message_id"]

            context = self.builder.build(message_id)

            features = self.extractor.extract(context)

            decision = self.engine.decide(features)

            evidence = self.retriever.retrieve(context)

            prediction = Prediction(
                message_id=message_id,
                action=decision.action,
                message_type=self.classifier.classify(context),
                reason="; ".join(decision.reason),
                confidence=decision.confidence,
                evidence_message_ids=evidence ,
            )

            predictions.append(prediction)

        return predictions