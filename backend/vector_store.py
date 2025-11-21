from transformers import AutoTokenizer, AutoModel
import chromadb
import torch

client = chromadb.Client()
collection = client.get_or_create_collection("docs")

# Load embedding model (PyTorch only)
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")


def embed(texts):
    with torch.no_grad():
        inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1)
        return embeddings.numpy()


def store_document(text):
    chunks = text.split(".")
    chunks = [c.strip() for c in chunks if c.strip()]

    embeddings = embed(chunks)
    ids = [f"id_{i}" for i in range(len(chunks))]

    collection.add(ids=ids, documents=chunks, embeddings=embeddings)


def search_vectors(query):
    embedding = embed([query])[0]
    results = collection.query(query_embeddings=[embedding.tolist()], n_results=3)
    return results["documents"][0]
