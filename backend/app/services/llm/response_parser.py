import json
import re


class ResponseParser:
    """
    Parses and validates LLM JSON responses.
    """

    REQUIRED_FIELDS = {
        "action",
        "message_type",
        "confidence",
        "reason",
    }

    def parse(self, response: str) -> dict:

        response = response.strip()

        # Remove Markdown code fences if present
        response = re.sub(r"^```json\s*", "", response, flags=re.IGNORECASE)
        response = re.sub(r"^```\s*", "", response)
        response = re.sub(r"\s*```$", "", response)

        try:
            data = json.loads(response)

        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Invalid JSON returned by LLM:\n{response}"
            ) from exc

        missing = self.REQUIRED_FIELDS - data.keys()

        if missing:
            raise ValueError(
                f"Missing required fields: {missing}"
            )

        return data