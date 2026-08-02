import requests

from app.config.settings import settings


class OllamaClient:
    """
    Wrapper around the local Ollama API.
    """

    def __init__(self):
        self.host = "http://localhost:11434"
        self.model = settings.LLM_MODEL

    def generate(self, prompt: str) -> str:

        response = requests.post(
            f"{self.host}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
            },
            timeout=120,
        )

        response.raise_for_status()

        data = response.json()

        return data["response"]