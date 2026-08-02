from app.models.notification_context import NotificationContext
from app.models.decision_features import DecisionFeatures

from app.services.llm.ollama_client import OllamaClient
from app.services.llm.prompt_builder import PromptBuilder
from app.services.llm.response_parser import ResponseParser
from app.services.llm.llm_factory import LLMFactory


class ReasoningService:
    """
    Uses the LLM to review and improve
    low-confidence predictions.
    """

    def __init__(self):

        self.client = OllamaClient()

        self.prompt_builder = PromptBuilder()

        self.parser = ResponseParser()

        self.client = LLMFactory.create()

    def review_prediction(
        self,
        context: NotificationContext,
        features: DecisionFeatures,
        prediction: dict,
        evidence: list[dict] = None,
    ) -> dict:

        prompt = self.prompt_builder.build(
            context=context,
            features=features,
            current_prediction=prediction,
            evidence=evidence,
        )

        response = self.client.generate(prompt)

        return self.parser.parse(response)