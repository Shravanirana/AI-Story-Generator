"""Core story‑generation logic."""
import os
import openai

# Load your OpenAI key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_story(prompt: str, model: str = "gpt-4o") -> str:
    """Return a story given a user prompt."""
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a creative story writer."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.9,
        max_tokens=800,
    )
    return response.choices[0].message.content.strip()
