from app.services.llm.groq_client import GroqClient

client = GroqClient()

response = client.generate(
    """
Reply ONLY with JSON.

{
    "status":"ok"
}
"""
)

print(response)