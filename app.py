import torch
import gradio as gr
import whisper
from transformers import pipeline

# Load models
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
transcriber = whisper.load_model("base")

# Define summarization function
def summarize_input(text, audio_path):
    if audio_path:
        result = transcriber.transcribe(audio_path)
        input_text = result["text"]
    elif text:
        input_text = text
    else:
        return "Please provide either text or audio input."

    summary = summarizer(input_text)[0]["summary_text"]
    return summary

# Define clear function
def clear_inputs():
    return "", None, ""

# Build Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## 📝🎙️ Text & Voice Summarizer")

    with gr.Row():
        audio_input = gr.Audio(sources=["microphone"], type="filepath", label="Speak your input")
        text_input = gr.Textbox(label="Or Type your input", lines=4)

    output_text = gr.Textbox(label="Summary")

    with gr.Row():
        summarize_button = gr.Button("Summarize")
        clear_button = gr.Button("Clear")

    summarize_button.click(fn=summarize_input, inputs=[text_input, audio_input], outputs=output_text)
    clear_button.click(fn=clear_inputs, inputs=[], outputs=[text_input, audio_input, output_text])

demo.launch()