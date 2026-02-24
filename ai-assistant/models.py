"""File for Pydantic models for structured AI analysis output."""

from pydantic import BaseModel, Field


class AssistantAnalysis(BaseModel):
    """Structured analysis of a customer enquiry."""

    summary: str = Field(
        description="""Single sentence summary of the customer's issue"""
    )
    summary_confidence: float = Field(
        ge=0.0, le=1.0,
        description="""Confidence score for summary (0.0 to 1.0)""",
    )
    intent: str = Field(
        description=(
            """Primary intent category. One of: 
            account_access,
            verification,
            payment_issue,
            account_closure,
            general_question,
            other"""
        )
    )
    intent_confidence: float = Field(
        ge=0.0, le=1.0,
        description="""Confidence score for intent category (0.0 to 1.0)""",
    )
    key_details: str = Field(
        description="""Key information from the customer message, e.g. 
        phone numbers,
        dates,
        reference numbers"""
    )
    escalation_needed: bool = Field(
        description=(
            """Whether this enquiry should be escalated 
            to a senior agent or specialist team"""
        )
    )
    escalation_confidence: float = Field(
        ge=0.0, le=1.0,
        description="""Confidence score for escalation decision (0.0 to 1.0)""",
    )
    escalation_reason: str | None = Field(
        None,
        description="""If escalation is needed, a brief reason why""",
    )
    suggested_action: str = Field(
        description=(
            """The recommended internal action for the agent, e.g. 
            'reset_password',
            'escalate_to_fraud_team',
            'check_account_restrictions'"""
        )
    )
    action_confidence: float = Field(
        ge=0.0, le=1.0,
        description="""Confidence score for suggested action (0.0 to 1.0)""",
    )
