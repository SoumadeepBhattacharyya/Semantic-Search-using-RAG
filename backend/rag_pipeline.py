from vector_store import search_vectors
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")


def rag_search(query):
    retrieved = search_vectors(query)
    context = " ".join(retrieved)

    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"

    output = generator(prompt, max_length=120, num_return_sequences=1)
    return output[0]["generated_text"]
