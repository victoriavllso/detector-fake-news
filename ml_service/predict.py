import torch
import argparse
import os
from transformers import AutoModelForSequenceClassification, AutoTokenizer


def load_resources(model_path):
    # Converte o caminho para absoluto (ex: /home/bridge/.../model)
    abs_model_path = os.path.abspath(model_path)
    
    if not os.path.exists(abs_model_path):
        raise FileNotFoundError(f"A pasta do modelo não foi encontrada em: {abs_model_path}")

    print(f"Carregando modelo de: {abs_model_path}...")
    
    tokenizer = AutoTokenizer.from_pretrained(abs_model_path)
    model = AutoModelForSequenceClassification.from_pretrained(abs_model_path)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()
    return model, tokenizer, device

def predict(texto, model, tokenizer, device):
    """Realiza a inferência no texto fornecido."""
    inputs = tokenizer(
        texto, 
        return_tensors="pt", 
        truncation=True, 
        max_length=256, 
        padding="max_length"
    ).to(device)

    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        prediction = torch.argmax(probs, dim=-1).item()
    
    label = "FAKE" if prediction == 1 else "REAL"
    confianca = probs[0][prediction].item() * 100
    return label, confianca

def main():
    # Configura o argumento do terminal
    parser = argparse.ArgumentParser(description="Classificador de Fake News via Arquivo TXT")
    parser.add_argument("arquivo", help="Caminho para o arquivo .txt que contém a notícia")
    parser.add_argument("--model_dir", default="./model", help="Diretório onde o modelo está salvo")
    
    args = parser.parse_args()

    # Verifica se o arquivo existe
    if not os.path.exists(args.arquivo):
        print(f"Erro: O arquivo '{args.arquivo}' não foi encontrado.")
        return

    # Lê o conteúdo do arquivo
    try:
        with open(args.arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read().strip()
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return

    if not conteudo:
        print("Erro: O arquivo está vazio.")
        return

    # Carrega recursos e prediz
    model, tokenizer, device = load_resources(args.model_dir)
    resultado, score = predict(conteudo, model, tokenizer, device)

    # Output visual
    cor = "\033[91m" if resultado == "FAKE" else "\033[92m"
    reset = "\033[0m"
    
    print("\n" + "="*30)
    print(f"ARQUIVO: {args.arquivo}")
    print(f"RESULTADO: {cor}{resultado}{reset}")
    print(f"CONFIANÇA: {score:.2f}%")
    print("="*30 + "\n")

if __name__ == "__main__":
    main()