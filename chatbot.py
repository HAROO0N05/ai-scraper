import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

with open("scraped_data.json", encoding="utf-8") as f:
    data = json.load(f)

texts = [d["content"] for d in data]

print("Loading embedder...")
embedder = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = embedder.encode(texts)

def get_answer(question):
    q_embedding = embedder.encode([question])
    sims = cosine_similarity(q_embedding, embeddings)[0]
    top_idx = np.argsort(sims)[-3:][::-1]
    context = "\n".join([texts[i] for i in top_idx])

    prompt = f"""Answer the question using only the context below.
If the answer isn't in the context, say so.

Context:
{context}

Question: {question}
Answer:"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("Chatbot ready! Type 'exit' to quit.\n")
    while True:
        q = input("Ask: ")
        if q.lower() == "exit":
            break
        print("\n" + get_answer(q) + "\n")