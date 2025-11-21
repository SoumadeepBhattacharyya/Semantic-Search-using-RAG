from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from rag_pipeline import rag_search
from vector_store import store_document

app = FastAPI()

# -------------------------
# CORS (Required for Vite)
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Upload Document Endpoint
# -------------------------
@app.post("/upload")
async def upload_doc(file: UploadFile = File(...)):
    text = (await file.read()).decode("utf-8")
    store_document(text)
    return {"message": "Document uploaded successfully"}

# -------------------------
# Semantic Search Endpoint
# -------------------------
@app.post("/search")
async def search(payload: dict):
    query = payload.get("query", "")
    if not query:
        return {"answer": "Query is empty."}

    answer, sources = rag_search(query)
    return {
        "answer": answer,
        "sources": sources
    }
