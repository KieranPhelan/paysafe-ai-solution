"""File to connect to OpenAI."""

from dotenv import load_dotenv
from openai import OpenAI


if __name__ == "__main__":

    load_dotenv()

    client = OpenAI()

    text_response = client.responses.create(
        model="gpt-5-nano",
        input="Tell me a joke about Python programming"
    )

    print(f"Joke:\n{text_response.output_text}")
