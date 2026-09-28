import argparse
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from data_utils import load_jsonl, to_text

EMBEDDINGS_PATH = "embeddings.npy"

companies = load_jsonl("companies.jsonl")
model = SentenceTransformer("./finetuned-model")

def load_or_build_embeddings(rebuild=False):
    if not rebuild and os.path.exists(EMBEDDINGS_PATH):
        emb = np.load(EMBEDDINGS_PATH)
        if len(emb) == len(companies):
            return emb
        print("Cached embeddings don't match companies.jsonl, rebuilding...")

    print("Encoding dataset...")
    texts = [to_text(c) for c in companies]
    emb = model.encode(texts, normalize_embeddings=True, show_progress_bar=True)
    np.save(EMBEDDINGS_PATH, emb)
    return emb

embeddings = None

def search(query, top_k=5):
    q_emb = model.encode([query], normalize_embeddings=True)
    scores = (embeddings @ q_emb.T).ravel()
    top_idx = np.argsort(-scores)[:top_k]
    return [(companies[i].get("operational_name", "Unknown"), float(scores[i])) for i in top_idx]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True, type=str)
    parser.add_argument("--rebuild", action="store_true", help="re-encode and overwrite embeddings.npy")
    args = parser.parse_args()

    embeddings = load_or_build_embeddings(rebuild=args.rebuild)

    print("\nTop 5 matches\n" + "=" * 40)
    for name, score in search(args.query, top_k=5):
        print(f"{score:.3f}  {name}")