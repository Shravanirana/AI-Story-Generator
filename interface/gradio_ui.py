import gradio as gr
from story_generator.generator import generate_story

def interface(prompt):
    return generate_story(prompt)

gr.Interface(
    fn=interface,
    inputs=gr.components.Textbox(lines=4, label="Story Prompt"),
    outputs="text",
    title="AI Story Generator",
    description="Enter a prompt and receive a short story."
).launch()
