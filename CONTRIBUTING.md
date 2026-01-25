# Contributing to Airline Q&A Bot (Flykite HR Policy RAG)

This repo hosts a **RAG-powered HR policy Q&A bot** over the Flykite Airlines employee handbook.

---

## Running Locally

1. **Clone and install**
   ```bash
   git clone https://github.com/ananttripathi/Airline-QnA-Bot.git
   cd Airline-QnA-Bot
   pip install -r requirements.txt
   ```
2. **API keys**  
   Set `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` (e.g. in `.env`). See [README → Installation](README.md#installation).
3. **Data**  
   Use `Dataset - Flykite Airlines_ HRP.pdf` as the HR handbook. Build the RAG pipeline per the [Evaluation Rubrics](README.md#evaluation-rubrics): load PDF → chunk → embed → vector DB → retriever → LLM generation.
4. **Implement & run**  
   LLM-only → prompt engineering → data prep for RAG → RAG Q&A → RAG hyperparameter tuning (5+ combinations). Use LangChain with OpenAI or Anthropic.

---

## Project Layout

- `README.md` — Overview, rubrics, setup, usage.
- `Dataset - Flykite Airlines_ HRP.pdf` — Flykite HR handbook.
- `requirements.txt` — Python deps (LangChain, etc.).

Add notebooks or `src/` as you implement the pipeline.

---

## Feedback

Open a [GitHub Issue](https://github.com/ananttripathi/Airline-QnA-Bot/issues) for questions or suggestions.
