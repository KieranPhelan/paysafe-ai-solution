"""File to analyse mock customer enquiries with AI assistant."""

import argparse
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd

from request import analyse_enquiry


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-e",
        "--enquiry",
        type=int,
        default=0,
        help="Enquiry number to analyse"
    )

    args = parser.parse_args()

    load_dotenv()

    df = pd.read_excel("Customer_Contact_Emails_20.xlsx", sheet_name=0)
    enquiry = df.iloc[args.enquiry]["TEXT"]

    client = OpenAI()

    result = analyse_enquiry(client, enquiry)

    print(enquiry)
    print(result)
