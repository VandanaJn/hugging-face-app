---
title: Demo
emoji: 🌖
colorFrom: purple
colorTo: purple
sdk: gradio
sdk_version: 4.15.0
app_file: app.py
pinned: false
license: mit
---

# 📝 Text Summarization Demo

This Hugging Face Space generates concise summaries from long-form text using a Transformer-based model. Built with Gradio 4.15.0, it supports both typed and spoken input for a smooth user experience.

[![Sync to Hugging Face hub](https://github.com/VandanaJn/hugging-face-app/actions/workflows/main.yml/badge.svg)](https://github.com/VandanaJn/hugging-face-app/actions/workflows/main.yml)

🔗 [Try the live demo here](https://huggingface.co/spaces/VandanaJn/Demo)

---

## 🚀 Features

- Summarizes long text into short, readable content  
- Supports voice input via microphone (Chrome/Firefox recommended)  
- Fast and intuitive interface powered by Gradio  
- Uses Hugging Face Transformers  

---

## 🧠 Model

This app uses [`sshleifer/distilbart-cnn-12-6`](https://huggingface.co/sshleifer/distilbart-cnn-12-6), a Transformer model fine-tuned for abstractive summarization on the CNN/Daily Mail dataset.

---

## 📋 How to Use

1. Paste or type your text into the input box.  
2. Click **Submit** to generate a summary.  
3. Optionally, use the microphone to speak your input.

---

## 🖼️ Screenshot

![App Screenshot](https://github.com/VandanaJn/repo-common/blob/main/huggingface-app-screenshot.png)

---

## 📦 Tech Stack

- Gradio 4.15.0  
- Hugging Face Transformers  
- Python 3.10+

---

## 📜 License

This project is licensed under MIT.

---

## 🙌 Acknowledgments

Thanks to Hugging Face and the open-source community for making powerful NLP tools accessible to everyone.

---

## 🙏 Inspiration

This project was inspired by [nogibjj's Hugging Face summarization app](https://github.com/nogibjj/hugging-face) and adapted for learning ML Ops and deployment with Gradio.