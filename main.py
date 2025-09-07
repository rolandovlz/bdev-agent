import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv

def main():
    if len(sys.argv) < 2:
        print("Usage: uv run main.py <prompt>")
        sys.exit(1)
    prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages
    )

    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
