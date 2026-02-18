from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

app = Flask(__name__)
CORS(app) # Permite chamadas de outras origens (como backend Kotlin)

# 1. Carregar o modelo e tokenizer 
MODEL_PATH = "./model/final" 
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

labels = {0: "Real", 1: "Fake"}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Texto não fornecido"}), 400

    # 2. Tokenização e Predição
    inputs = tokenizer(data['text'], return_tensors="pt", truncation=True, padding=True, max_length=512)
    
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        prediction = torch.argmax(logits, dim=-1).item()
        probability = torch.nn.functional.softmax(logits, dim=-1)

    # 3. Resposta formatada
    return jsonify({
        "label": labels[prediction],
        "confidence": float(probability[0][prediction]),
        "all_scores": {labels[i]: float(probability[0][i]) for i in labels}
    })
@app.route('/')
def home():
    return "Bem-vindo ao Detector de Fake News API! Use o endpoint /predict para classificar notícias.", 200

if __name__ == '__main__':
    app.run(port=5000)
    
	#https://www.youtube.com/watch?v=GS_ylghUtLQ&start=0