
from bert_model import model_init
from fake_news_dataset import FakeNewsDataset
from tokenizer import tokenize_function, tokenizer
import numpy as np
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from transformers import TrainingArguments
from dataset_processing import texts, labels
from sklearn.model_selection import train_test_split
from transformers import Trainer

 # --------- definição das métricas de avaliação
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    
    acc = accuracy_score(labels, predictions)
    f1_macro = f1_score(labels, predictions, average='macro')
    precision = precision_score(labels, predictions, average='macro')
    recall = recall_score(labels, predictions, average='macro')
    
    return {
        'accuracy': acc,
        'f1_macro': f1_macro,
        'precision': precision,
        'recall': recall
    }


training_args = TrainingArguments(
    output_dir="../model",             # Pasta temporária para checkpoints
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    eval_strategy="epoch",           
    save_strategy="epoch",
    load_best_model_at_end=True,        # garante que o melhor modelo seja mantido
    metric_for_best_model="f1_macro",   # critério para decidir o "melhor"
    fp16=True,                          # acelerar a GPU
    label_smoothing_factor=0.1
)

 # --------- preparação dos datasets de treino e validação
x_train, x_val, y_train, y_val = train_test_split(texts, labels, test_size=0.1, stratify=labels, random_state=42)

train_encodings = tokenize_function(x_train.tolist())
val_encodings = tokenize_function(x_val.tolist())

train_dataset = FakeNewsDataset(train_encodings, y_train)
val_dataset = FakeNewsDataset(val_encodings, y_val)

 # --------- configuração e inicialização do Trainer
trainer = Trainer(
    model_init=model_init,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    compute_metrics=compute_metrics,
    tokenizer=tokenizer
)

trainer.train()

# --------- salvamento do modelo treinado

final_model_path = "../model/final"

trainer.save_model(final_model_path)
tokenizer.save_pretrained(final_model_path)

print(f"Modelo final salvo em: {final_model_path}")
