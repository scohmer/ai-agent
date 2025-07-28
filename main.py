import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from .env
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Check if a prompt was provided
if len(sys.argv) < 2:
    print("Usage: python3 main.py \"<your prompt here>\" [--verbose]")
    sys.exit(1)

# Check for --verbose flag
verbose = False
if "--verbose" in sys.argv:
    verbose = True
    sys.argv.remove("--verbose")

# Define prompt
prompt = " ".join(sys.argv[1:])

# Create Gemini client
client = genai.Client(api_key=api_key)

# Create conversation
messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]

# Generate content
response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

# Print response text
print("Response:\n", response.text)

if verbose:
    print(f"\nUser prompt: {prompt}")
    # Print token usage
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

def main():
    return


if __name__ == "__main__":
    main()
