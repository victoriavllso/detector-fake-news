from transformers import AutoModelForSequenceClassification
from tokenizer import model_name

model = AutoModelForSequenceClassification.from_pretrained(
    model_name, 
    num_labels=2 # fake ou real
)