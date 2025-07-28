import os
import sys
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Check if a prompt was provided
if len(sys.argv) < 2:
    print("Usage: python3 main.py \"<your prompt here>\"")
    sys.exit(1)

# Define prompt
prompt = " ".join(sys.argv[1:])

# Create Gemini client
client = genai.Client(api_key=api_key)

# Generate content
response = client.models.generate_content(model="gemini-2.0-flash-001", contents=prompt)

# Print response text
print("Response:\n", response.text)

# Print token usage
print(f"\nPrompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

def main():
    return


if __name__ == "__main__":
    main()
