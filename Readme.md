# 🔍 Semantic Search Engine using RAG (Retrieval-Augmented Generation)

A full-stack AI project that performs semantic search over documents using:

- Sentence Transformers (MiniLM)
- ChromaDB vector database
- GPT-2 based text generation (RAG)
- FastAPI backend
- React frontend

---

## 🚀 Features

- Upload documents (TXT/PDF → convert to text)
- Chunks content and stores in vector DB
- Semantic search via embeddings
- RAG pipeline generates final answer
- Full React UI for query/response

---

## 🏗️ Architecture

User → React App → FastAPI → Embeddings → VectorDB (Chroma) → RAG → Response

---

## 🕳️ Tech Stack

- FastAPI
- Sentence Transformer
- ChromaDB
- GPT-2 (HuggingFace)
- React

---

## 🧠 How RAG Works

1. Convert document into chunks
2. Create embeddings using MiniLM
3. Store in ChromaDB
4. Query is embedded
5. Retrieve top-N chunks
6. Pass context + query to LLM
7. Return final answer


