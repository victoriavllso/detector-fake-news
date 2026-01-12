from transformers import AutoTokenizer
from sklearn.model_selection import train_test_split
import pandas as pd


model_name = "neuralmind/bert-base-portuguese-cased" # toklenizer pré-treinado da google para português
tokenizer = AutoTokenizer.from_pretrained(model_name)

def tokenize_function(texts):
    return tokenizer(
        texts,
        padding="max_length",
        truncation=True,
        max_length=512, # Limite padrão do BERT
        return_tensors="pt"
    )
dataset_path = '../dataset/dataset_fake_news.csv'

df = pd.read_csv(dataset_path)
x = df["text"]
y = df["label"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

train_encodings = tokenize_function(x_train.tolist())
test_encodings = tokenize_function(x_test.tolist())

#input_ids são os índices correspondentes a cada token na frase.
#attention_mask indica se um token deve receber atenção ou não.
#token_type_ids identifica a qual sequência um token pertence quando há mais de uma sequência.

#teste = tokenizer.decode(tokenization['input_ids'][0], skip_special_tokens=True)
#print(teste)