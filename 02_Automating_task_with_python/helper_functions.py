from google import genai

import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=gemini_api_key)


def get_llm_response(prompt):
    """Takes a prompt and returns the Gemini response."""

    if not isinstance(prompt, str):
        raise ValueError("Input must be a string enclosed in quotes.")

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"


def print_llm_response(prompt):
    """Takes a prompt and prints the Gemini response."""

    llm_response = get_llm_response(prompt)
    print(llm_response)