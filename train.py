import json
import torch
import random
import torch.nn.functional as F

from lookup import companies, COUNTRYCODE_DICT
from data_utils import load_jsonl, to_text

from datasets import Dataset
from sentence_transformers import SentenceTransformer, SentenceTransformerTrainer, SentenceTransformerTrainingArguments
from sentence_transformers.sentence_transformer.losses import MultipleNegativesRankingLoss
from sentence_transformers.sentence_transformer.evaluation import InformationRetrievalEvaluator

BATCH_SIZE = 128
EVAL_BATCH_SIZE = 128
NUM_EPOCHS = 10
LEARNING_RATE = 2e-5
TEMPERATURE = 0.05
EVAL_K = 10
TRAIN_FRAC = 0.8
VAL_FRAC = 0.1

CODE_TO_COUNTRY = {}
for name, code in COUNTRYCODE_DICT.items():
    CODE_TO_COUNTRY.setdefault(code, name)

documents = [to_text(company) for company in companies]
NUM_DOCUMENTS = len(documents)

training_data = load_jsonl("complex_dataset.jsonl")
shuffled = training_data[:]
random.shuffle(shuffled)

n_total = len(shuffled)
n_train = int(TRAIN_FRAC * n_total)
n_val = int(VAL_FRAC * n_total)

train_rows = shuffled[:n_train]
val_rows = shuffled[n_train:n_train + n_val]
test_rows = shuffled[n_train + n_val:]

print(f"{n_total} rows -> train={len(train_rows)} val={len(val_rows)} test={len(test_rows)}")

def build_paired_dataset(rows):
    anchors = []
    positives = []
    for row in rows:
        for idx in row["relevant_indices"]:
            anchors.append(row["query"])
            positives.append(documents[idx])
    return Dataset.from_dict({"anchor": anchors, "positive": positives})

train_dataset = build_paired_dataset(train_rows)
val_dataset = build_paired_dataset(val_rows)
test_dataset = build_paired_dataset(test_rows)

corpus = {str(i): doc for i, doc in enumerate(documents)}

def build_eval_dicts(rows):
    queries = {str(i): row["query"] for i, row in enumerate(rows)}
    relevant_docs = {str(i): {str(idx) for idx in row["relevant_indices"]} for i, row in enumerate(rows)}
    return queries, relevant_docs

test_queries, test_relevant_docs = build_eval_dicts(test_rows)

args = SentenceTransformerTrainingArguments(
    output_dir="./finetuned-model",
    num_train_epochs=NUM_EPOCHS,
    per_device_train_batch_size=BATCH_SIZE,
    per_device_eval_batch_size=EVAL_BATCH_SIZE,
    learning_rate=LEARNING_RATE,
    eval_strategy="no",
    save_strategy="no",
    logging_strategy="epoch",
    fp16=torch.cuda.is_available(),
    batch_sampler = "no_duplicates",
)

model = SentenceTransformer("all-MiniLM-L6-v2")
loss = MultipleNegativesRankingLoss(model)

trainer = SentenceTransformerTrainer(
    model=model,
    args=args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    loss=loss,
)

trainer.train()

print("\n--- Running Test Evaluation ---")
test_evaluator = InformationRetrievalEvaluator(
    queries=test_queries, 
    corpus=corpus, 
    relevant_docs=test_relevant_docs, 
    name="test",
    accuracy_at_k=[EVAL_K],
    precision_recall_at_k=[EVAL_K]
)
test_metrics = test_evaluator(model)
print(json.dumps(test_metrics, indent=4))

model.save_pretrained("./finetuned-model")