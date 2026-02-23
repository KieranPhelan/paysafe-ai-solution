"""File for Pydantic models for structured AI analysis output."""

from pydantic import BaseModel, Field


class AssistantAnalysis(BaseModel):
    """Structured analysis of a customer enquiry."""

    summary: str = Field(
        description="""Single sentence summary of the customer's issue"""
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
    confidence: float = Field(
        ge=0.0, le=1.0,
        description="""Confidence score for intent category (0.0 to 1.0)""",
    )
    escalation_needed: bool = Field(
        description=(
            """Whether this enquiry should be escalated 
            to a senior agent or specialist team"""
        )
    )
    key_entities: str = Field(
        description="""Key information from the customer message, e.g. 
        phone numbers,
        dates,
        reference numbers"""
    )
    suggested_action: str = Field(
        description=(
            """The recommended internal action for the agent, e.g. 
            'reset_password',
            'escalate_to_fraud_team',
            'check_account_restrictions'"""
        )
    )
