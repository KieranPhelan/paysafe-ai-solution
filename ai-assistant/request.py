"""File to send enquiry to the LLM and returns structured output."""

from openai import OpenAI

from models import AssistantAnalysis


SYSTEM_PROMPT = """
You are an internal AI assistant at Paysafe, a regulated payments company.
Your job is to analyse incoming customer enquiries and produce structured
output to help a human support agent respond quickly and accurately.

Guidelines:
- Be precise with all fields.
- Set confidence scores honestly.
- Never fabricate information. Only extract what is present in the message.
- Suggested actions should be clear, concise steps the agent can take.
"""


def analyse_enquiry(client: OpenAI,
                    message: str,
                    model: str = "gpt-5-nano") -> AssistantAnalysis:
    """Analyse a customer enquiry and return structured output."""
    response = client.responses.parse(
        model=model,
        instructions=SYSTEM_PROMPT,
        input=[{"role": "user", "content": message}],
        text_format=AssistantAnalysis,
    )

    return response.output_parsed
