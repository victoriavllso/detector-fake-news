from transformers import TrainingArguments, Trainer
from bert_model import model
from tokenizer import train_encodings, test_encodings, y_train, y_test, tokenizer
from fake_news_dataset import FakeNewsDataset
import numpy as np
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from transformers import TrainingArguments, Trainer


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    
    acc = accuracy_score(labels, predictions)
    f1 = f1_score(labels, predictions, average='binary')
    precision = precision_score(labels, predictions, average='binary')
    recall = recall_score(labels, predictions, average='binary')
    
    return {
        'accuracy': acc,
        'f1': f1,
        'precision': precision,
        'recall': recall
    }


train_dataset = FakeNewsDataset(train_encodings, y_train)
test_dataset = FakeNewsDataset(test_encodings, y_test)


training_args = TrainingArguments(
    output_dir="./results",          # Pasta temporária para checkpoints
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    eval_strategy="epoch",           
    save_strategy="epoch",
    load_best_model_at_end=True,     # garante que o melhor modelo seja mantido
    metric_for_best_model="f1",      # critério para decidir o "melhor"
    fp16=True,                       # acelerar a GPU
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    compute_metrics=compute_metrics, 
)

trainer.train()

model_path = "../model"
trainer.save_model(model_path)
tokenizer.save_pretrained(model_path) 
print(f"Modelo salvo com sucesso em {model_path}")