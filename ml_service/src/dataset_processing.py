import os
import pandas as pd
from tqdm import tqdm 

def criar_csv_fake_news(diretorio_base, nome_arquivo_saida='../datasets/dataset_fake_news.csv'):
    dados = []
    
    # Mapeamento de pastas e seus respectivos labels
    # 0 para Verdadeira (True), 1 para Fake (False)
    categorias = {
        'true': 0,
        'fake': 1
    }
        
    for pasta, label in categorias.items():
        caminho_completo = os.path.join(diretorio_base, pasta)
        
        if not os.path.exists(caminho_completo):
            print(f"Aviso: Pasta {caminho_completo} não encontrada. Pulando...")
            continue
        
        arquivos = [f for f in os.listdir(caminho_completo) if f.endswith('.txt')]
                
        for nome_arquivo in tqdm(arquivos):
            caminho_arquivo = os.path.join(caminho_completo, nome_arquivo)
            
            try:
                with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                    conteudo = f.read().strip()
                    if conteudo: 
                        dados.append({
                            'label': label,
                            'file_source': nome_arquivo, # para rastrear a origem se necessário
                            'text': conteudo
                        })
            except Exception as e:
                print(f"Erro ao ler o arquivo {nome_arquivo}: {e}")

    df = pd.DataFrame(dados)
    
    df.to_csv(nome_arquivo_saida, index=False, encoding='utf-8')
    print(f"\nSucesso! Dataset salvo como: {nome_arquivo_saida}")
    print(f"Total de registros: {len(df)}")
    print(df['label'].value_counts()) # balanceamento entre classes

criar_csv_fake_news('../datasets')