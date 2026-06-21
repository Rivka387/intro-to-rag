# Intro To RAG

Educational RAG example built around a PDF document, OpenAI embeddings/chat, and Pinecone vector search.

This project demonstrates the basic RAG pipeline:
- load a PDF
- extract text
- split the text into chunks
- generate embeddings
- store embeddings in Pinecone
- retrieve relevant chunks for a question
- generate an answer from the retrieved context

## Project Files

- `intro_to_rag.ipynb`: main notebook for the full step-by-step demo
- `run_intro_to_rag.py`: helper script to execute the notebook code cells outside Jupyter
- `os_book.pdf`: example source document
- `requirements.txt`: Python dependencies
- `.env.example`: required environment variables template

## Requirements

- Python 3.11+
- OpenAI API key
- Pinecone API key

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file based on `.env.example` and fill in your keys:

```env
OPENAI_API_KEY=
PINECONE_API_KEY=
PINECONE_INDEX_NAME=rag-llm-index
PINECONE_CLOUD=aws
PINECONE_REGION=us-east-1
PDF_PATH=os_book.pdf
OPENAI_CHAT_MODEL=gpt-4o-mini
```

## Run In Jupyter

Open:

```text
intro_to_rag.ipynb
```

Then run the cells in order.

## Run From CLI

To execute the notebook logic as a Python script:

```bash
python run_intro_to_rag.py
```

## Notes

- This repository is an educational demo, not a production-ready RAG system.
- Pinecone and OpenAI access depend on network availability and local filtering rules.
- `.env` is ignored and should not be committed.

## Suggested GitHub Repository Name

- `intro-to-rag`
- `pdf-rag-demo`
- `rag-notebook-starter`
