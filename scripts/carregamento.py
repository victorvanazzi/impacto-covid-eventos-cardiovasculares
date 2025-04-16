# scripts/carregamento.py

import os
import pandas as pd

def carregar_dados_tratados(caminho_base="../dados_tratados"):
    dados = {}

    for categoria in os.listdir(caminho_base):
        caminho_categoria = os.path.join(caminho_base, categoria)

        if not os.path.isdir(caminho_categoria):
            continue

        dados[categoria] = {}

        for arquivo in os.listdir(caminho_categoria):
            if arquivo.endswith("_tratado.csv"):
                nome_base = arquivo.replace("_tratado.csv", "")
                caminho_arquivo = os.path.join(caminho_categoria, arquivo)

                # Lê o CSV normalmente
                df = pd.read_csv(caminho_arquivo, sep=";", encoding="utf-8-sig")

                # Se tiver a coluna 'data', converte para datetime
                if 'data' in df.columns:
                    df['data'] = pd.to_datetime(df['data'], errors='coerce')

                dados[categoria][nome_base] = df

    return dados

