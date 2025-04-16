# scripts/preprocessamento.py

import os
import pandas as pd
import locale

# Define o locale para reconhecer meses em português (Janeiro, Fevereiro, etc.)
try:
    locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")  # Linux/macOS
except Exception as e:
    try:
        locale.setlocale(locale.LC_TIME, "Portuguese_Brazil.1252")  # Windows
    except Exception as e2:
        pass

def carregar_csv(caminho, skiprows=0, skipfooter=0, encoding="latin1"):
    """
    Carrega um arquivo CSV com tratamento de erros e parâmetros opcionais.
    """
    engine = "python" if skipfooter > 0 else "c"
    try:
        df = pd.read_csv(
            caminho,
            skiprows=skiprows,
            skipfooter=skipfooter,
            encoding=encoding,
            engine=engine,
            sep=";",
            on_bad_lines="skip"
        )
        return df
    except Exception as e:
        return None


def tratar_tabela_datasus(df):
    df = df.copy()

    df.rename(columns={df.columns[0]: "data"}, inplace=True)

    # Limpa espaços e pontos no início da coluna
    df["data"] = df["data"].astype(str).str.strip().str.replace(r"^\.*", "", regex=True)

    # Substitui traços por zero
    df.replace("-", 0.0, inplace=True)

    # Tenta converter datas nos formatos "Janeiro/2021" e "jan/21"
    data_convertida_1 = pd.to_datetime(df["data"], format="%B/%Y", errors="coerce")
    data_convertida_2 = pd.to_datetime(df["data"], format="%b/%y", errors="coerce")

    # Usa a primeira que funcionar, e descarta linhas em que nenhuma funcionou
    df["data"] = data_convertida_1.combine_first(data_convertida_2)
    df = df[df["data"].notna()]

    # Converte colunas numéricas
    for col in df.columns:
        if col != "data":
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df




