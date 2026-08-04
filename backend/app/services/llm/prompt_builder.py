from app.models.notification_context import NotificationContext
from app.models.decision_features import DecisionFeatures


class PromptBuilder:
    """
    Builds structured prompts for the LLM.
    """

    def build(
        self,
        context: NotificationContext,
        features: DecisionFeatures,
        current_prediction: dict,
        evidence: list[dict],
    ) -> str:

        evidence_text = ""

        if evidence:
            for item in evidence:
                evidence_text += f"""
Message ID: {item["message_id"]}

Message:
{item["message"]}

Similarity Score:
{item["score"]}

------------------------
"""
        else:
            evidence_text = "No similar notifications found."

        return f"""
You are an AI Notification Intelligence System.

Review the notification below and determine whether the current prediction is correct.

========================
MESSAGE
========================
{context.message.message_text}

========================
USER PROFILE
========================
User ID:
{context.user.user_id}

Engagement Score:
{context.user.engagement_score:.2f}

Dismissed Notifications:
{context.user.notifications_dismissed_30d}

========================
FEATURES
========================
Urgency:
{features.contains_urgency}

OTP Request:
{features.contains_otp_request}

Credential Request:
{features.contains_credential_request}

Forward Count:
{features.forwarding_risk}

Risk Score:
{features.risk_score:.2f}

========================
CURRENT PREDICTION
========================
Action:
{current_prediction["action"]}

Message Type:
{current_prediction["message_type"]}

Allowed Message Types:
personal, urgent, event, payment, business_update, promotion, greeting, forward, spam, scam, unknown

Confidence:
{current_prediction["confidence"]}

Reason:
{current_prediction["reason"]}

========================
SIMILAR NOTIFICATIONS
========================

{evidence_text}

========================

Return ONLY raw JSON.

Do NOT include:
- markdown
- ```json
- explanations
- notes
- comments

The first character of your response must be '{{'
The last character must be '}}'

Return this format exactly:

{{
    "action": "...",
    "message_type": "...",
    "confidence": 0.95,
    "reason": "..."
}}
"""