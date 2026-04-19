---
title: Flykite Airlines HR Policy Bot
emoji: ✈️
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 6.12.0
app_file: app.py
pinned: false
license: mit
---

# ✈️ Flykite Airlines HR Policy Q&A Bot

A RAG-powered HR assistant that answers employee questions from the Flykite Airlines HR handbook using **Groq (LLaMA 3 70B)**, **FAISS**, and **Gradio**.

## How it works

1. **PDF ingestion** — The Flykite Airlines HR handbook is loaded and split into chunks
2. **Embeddings** — `all-MiniLM-L6-v2` (sentence-transformers) encodes chunks into a FAISS vector index
3. **Retrieval** — Semantic search fetches the top 4 most relevant policy sections per query
4. **Generation** — Groq's LLaMA 3 70B generates grounded, cited answers

## Setup (local)

```bash
git clone https://github.com/ananttripathi/Airline-QnA-Bot.git
cd Airline-QnA-Bot
pip install -r requirements.txt
export GROQ_API_KEY=your_key_here
python app.py
```

## Deploy to Hugging Face Spaces

1. Create a new Space (SDK: Gradio)
2. Push this repo to the Space
3. Add `GROQ_API_KEY` as a Space secret under **Settings → Variables and secrets**

## Stack

| Component | Technology |
|-----------|-----------|
| LLM | Groq — LLaMA 3 70B (free) |
| Embeddings | sentence-transformers/all-MiniLM-L6-v2 |
| Vector DB | FAISS (CPU) |
| Framework | LangChain 0.3 |
| UI | Gradio 4.x |

## Project Structure

```
Airline-QnA-Bot/
├── app.py                              # Main app — RAG pipeline + Gradio UI
├── requirements.txt
├── Dataset - Flykite Airlines_ HRP.pdf # Knowledge source
└── README.md
```

## License

[MIT](LICENSE)
