import os
import pandas as pd
from tqdm import tqdm 

def extrair_noticias_fake_e_verdadeiras(diretorio_base):
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

    return pd.DataFrame(dados)


def extrair_noticias_tendenciosas(caminho_arquivo_tsv: str) -> pd.DataFrame:
    categorias = {
        'distorcido': 2,
        'exagerado': 2
    }

    df = pd.read_csv(caminho_arquivo_tsv, sep='\t', encoding='utf-8')

    df['alternativeName'] = (
        df['alternativeName']
        .dropna()
        .str.lower()
        .str.strip()
    )

    df_filtrado = df[df['alternativeName'].isin(categorias)]

    df_filtrado['label'] = df_filtrado['alternativeName'].map(categorias)

    return df_filtrado[['label', 'claimReviewed']] \
        .rename(columns={'claimReviewed': 'text'})


def criar_csv_fake_news(diretorio_base: str,caminho_tsv: str, nome_arquivo_saida: str):
    df_fake_true = extrair_noticias_fake_e_verdadeiras(diretorio_base)
    df_tendenciosas = extrair_noticias_tendenciosas(caminho_tsv)

    df_final = pd.concat(
        [df_fake_true[['label', 'text']], df_tendenciosas],
        ignore_index=True
    )

    df_final.to_csv(nome_arquivo_saida, index=False)

    print("Dataset criado com sucesso!")
    print(df_final['label'].value_counts())

    

diretorio_base = '../dataset'
#criar_csv_fake_news(diretorio_base, '../dataset/FACTCKBR.tsv', '../dataset/fake_news_dataset.csv')


 # --------- preparação do dataset 
 
dataset_path = '../dataset/dataset_fake_news_corpus.csv'

df = pd.read_csv(dataset_path)
df = df.dropna(subset=['text', 'label'])  # Remover linhas com valores ausentes
texts = df["text"]
labels = df["label"]
