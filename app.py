from story_generator.generator import generate_story
from story_generator.prompts import get_default_prompt

if __name__ == "__main__":
    prompt = get_default_prompt()
    story = generate_story(prompt)
    print("\nGenerated Story:\n")
    print(story)
