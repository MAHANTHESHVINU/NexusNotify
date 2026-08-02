from app.config.settings import settings

from app.services.llm.groq_client import GroqClient
from app.services.llm.ollama_client import OllamaClient


class LLMFactory:
    """
    Creates the configured LLM client.
    """

    @staticmethod
    def create():

        provider = settings.LLM_PROVIDER.lower()

        if provider == "groq":
            return GroqClient()

        if provider == "ollama":
            return OllamaClient()

        raise ValueError(
            f"Unsupported LLM provider: {provider}"
        )