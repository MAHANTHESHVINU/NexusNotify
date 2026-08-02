import json


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