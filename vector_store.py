from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("knowledge_base.json") as f:
    knowledge_base = json.load(f)

texts = [item["question"] + " " + item["answer"] for item in knowledge_base]
embeddings = model.encode(texts)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

def search_similar(query, top_k=3):
    query_vector = model.encode([query])
    distances, indices = index.search(np.array(query_vector), top_k)
    
    results = [knowledge_base[i] for i in indices[0]]
    return results