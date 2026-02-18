
from bert_model import model_init
from fake_news_dataset import FakeNewsDataset
from tokenizer import tokenize_function, tokenizer
import numpy as np
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix
from transformers import TrainingArguments
from dataset_processing import texts, labels
from sklearn.model_selection import train_test_split
from transformers import Trainer
import matplotlib.pyplot as plt
import seaborn as sns

 # --------- definição das métricas de avaliação

 # macro -> usa para classes desbalanceadas, pois calcula a média das métricas para cada classe, dando igual importância a todas as classes, independentemente do número de amostras em cada classe.
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
   processing_class=tokenizer
)

trainer.train()

# --------- matriz de confusão

# 1. Obter as predições do conjunto de validação
output = trainer.predict(val_dataset)
y_true = output.label_ids
y_pred = np.argmax(output.predictions, axis=-1)

# 2. Gerar a matriz de confusão
# Os nomes das labels seguem a ordem: 0 (Verdadeira), 1 (Fake)
labels = ['Verdadeira', 'Fake']
cm = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=labels, yticklabels=labels)
plt.ylabel('Real')
plt.xlabel('Predito')
plt.title('Matriz de Confusão - BERTimbau')
plt.savefig('../model/confusion_matrix.png') # Salva a imagem na sua pasta de modelos

# --------- salvamento do modelo treinado

final_model_path = "../model/final"

trainer.save_model(final_model_path)
tokenizer.save_pretrained(final_model_path)

print(f"Modelo final salvo em: {final_model_path}")
