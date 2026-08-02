from app.services.llm.ollama_client import OllamaClient


client = OllamaClient()

response = client.generate(
    """
    Reply using ONLY this JSON.

    {
      "status":"ok"
    }
    """
)

print(response)