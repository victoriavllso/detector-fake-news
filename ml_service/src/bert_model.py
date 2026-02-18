from transformers import AutoModelForSequenceClassification
from config import model_name

def model_init():
	return AutoModelForSequenceClassification.from_pretrained(
    model_name, 
    num_labels=2 # fake ou real ou sensacionalista
)