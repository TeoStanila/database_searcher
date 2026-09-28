import json
from sentence_transformers import SentenceTransformer
import numpy as np

from data_utils import to_text

companies = []
with open("companies.jsonl", encoding="utf-8") as f:
    for line in f:
        if line.strip():
            companies.append(json.loads(line))

model = SentenceTransformer("all-MiniLM-L6-v2")
texts = [to_text(c) for c in companies]
embeddings = model.encode(texts, normalize_embeddings=True)

query = input("Search query: ")
q_emb = model.encode([query], normalize_embeddings=True)
scores = (embeddings @ q_emb.T).ravel()
top5 = np.argsort(-scores)[:5]

for i in top5:
    print(f"{scores[i]:.3f}  {companies[i]['operational_name']}")