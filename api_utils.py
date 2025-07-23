import os
from dotenv import load_dotenv
import anthropic

# Load environment variables from .env file
load_dotenv()

def analyze_with_llm(prompt):
    """
    Calls the Anthropic Claude Sonnet 4 API to get a response for the given prompt.
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise Exception("ANTHROPIC_API_KEY not set in .env!")

    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.content[0].text
