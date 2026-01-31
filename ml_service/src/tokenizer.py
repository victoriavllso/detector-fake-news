from transformers import AutoTokenizer
from config import model_name


tokenizer = AutoTokenizer.from_pretrained(model_name)
 
 # --------- processo de tokenização  
def tokenize_function(texts):
    return tokenizer(
        texts,
        padding=True,
        truncation=True,
        max_length=512, # Limite padrão do BERT
        return_tensors="pt"
    )
