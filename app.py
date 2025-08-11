from transformers import pipeline
import gradio as gr
import torch

# Load summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Define prediction function
def summarize_text(text):
    summary = summarizer(text)[0]["summary_text"]
    return summary

# Build Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## 📝 Text Summarization App")
    input_text = gr.Textbox(placeholder="Enter text to summarize", lines=5, label="Input")
    output_text = gr.Textbox(label="Summary")
    summarize_button = gr.Button("Summarize")

    summarize_button.click(fn=summarize_text, inputs=input_text, outputs=output_text)

# Launch the app
demo.launch()

