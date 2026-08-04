from pathlib import Path

base_dir = Path(__file__).resolve().parent

content = '''from app.config.settings import settings
from app.services.llm.ollama_client import OllamaClient


class LLMFactory:
    """
    Creates the configured LLM client.
    """

    @staticmethod
    def create():

        provider = settings.LLM_PROVIDER.lower()

        if provider == "groq":
            try:
                from app.services.llm.groq_client import GroqClient

                return GroqClient()
            except ImportError:
                print(
                    "groq package is not installed; falling back to Ollama for LLM generation."
                )
                return OllamaClient()

        if provider == "ollama":
            return OllamaClient()

        raise ValueError(
            f"Unsupported LLM provider: {provider}"
        )
'''

(base_dir / 'app' / 'services' / 'llm' / 'llm_factory.py').write_text(content, encoding='utf-8')
print('patched llm_factory')
