"""File to analyse mock customer enquiries with AI assistant."""

import argparse
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd

from request import analyse_enquiry


def display_result(enquiry: str, analysis):
    """Display the enquiry and analysis result."""
    print("Customer Enquiry:")
    print(enquiry)

    print("\nAI Analysis:")

    print(
        f"Summary: {analysis.summary} (Confidence: {analysis.summary_confidence:.2f})")

    print(
        f"Intent: {analysis.intent} (Confidence: {analysis.intent_confidence:.2f})")

    print(f"Key Details: {analysis.key_details}")

    print(f"Escalation Needed: {analysis.escalation_needed} "
          f"(Confidence: {analysis.escalation_confidence:.2f})")
    if analysis.escalation_needed and analysis.escalation_reason:
        print(f"Escalation Reason: {analysis.escalation_reason}")

    print(
        f"Suggested Action: {analysis.suggested_action} (Confidence: {analysis.action_confidence:.2f})")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-e",
        "--enquiry",
        type=int,
        default=1,
        help="Enquiry number to analyse"
    )

    args = parser.parse_args()

    load_dotenv()

    df = pd.read_excel("Customer_Contact_Emails_20.xlsx", sheet_name=0)
    enquiry = df.iloc[args.enquiry - 1]["TEXT"]

    client = OpenAI()

    result = analyse_enquiry(client, enquiry)

    display_result(enquiry, result)
