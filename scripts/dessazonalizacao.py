import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import STL
from pathlib import Path

def dessazonalizar(df, coluna="Total", freq="MS", seasonal=13, robust=True):
    """
    Aplica decomposição STL na série temporal de uma coluna específica do DataFrame.

    Parâmetros:
        df (DataFrame): Dados com colunas 'data' e a coluna de valores.
        coluna (str): Nome da coluna a dessazonalizar.
        freq (str): Frequência da série (ex: 'MS' para início de mês).
        seasonal (int): Comprimento da janela sazonal.
        robust (bool): Se True, utiliza método robusto do STL.

    Retorna:
        DataFrame: Mesmos dados originais acrescidos das colunas:
            - 'trend': componente de tendência
            - 'seasonal': componente sazonal
            - 'resid': resíduos
            - 'dessazonalizado': série original menos sazonalidade
    """
    df = df.copy().dropna(subset=["data", coluna]).sort_values("data")
    df = df.set_index("data").asfreq(freq)
    df[coluna] = df[coluna].ffill()

    stl = STL(df[coluna], seasonal=seasonal, robust=robust)
    resultado = stl.fit()

    df["trend"] = resultado.trend
    df["seasonal"] = resultado.seasonal
    df["resid"] = resultado.resid
    df["dessazonalizado"] = df[coluna] - resultado.seasonal

    return df.reset_index()


def plot_dessazonalizacao(df, coluna="Total", titulo=None, salvar_em=None):
    """
    Plota comparação entre a série original e a série dessazonalizada.

    Parâmetros:
        df (DataFrame): Resultado da dessazonalização, contendo a coluna 'dessazonalizado'.
        coluna (str): Nome da coluna original.
        titulo (str): Título do gráfico.
        salvar_em (str): Diretório para salvar o gráfico (opcional).
    """
    titulo = titulo or coluna
    plt.figure(figsize=(14, 5))
    plt.plot(df["data"], df[coluna], label="Original", linestyle="--", alpha=0.5)
    plt.plot(df["data"], df["dessazonalizado"], label="Dessazonalizada")
    plt.title(f"Série Original vs. Dessazonalizada – {titulo}")
    plt.xlabel("Data")
    plt.ylabel(coluna)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    if salvar_em:
        Path(salvar_em).mkdir(parents=True, exist_ok=True)
        nome_arquivo = f"{titulo.lower().replace(' ', '_').replace('/', '_')}.png"
        caminho = Path(salvar_em) / nome_arquivo
        plt.savefig(caminho, dpi=300)

    plt.show()


def dessazonalizar_em_lote(dicionario_eventos, eventos_a_dessazonalizar=None):
    """
    Aplica dessazonalização STL em lote, retornando apenas os DataFrames transformados.

    Parâmetros:
        dicionario_eventos (dict): Chave: nome do evento; valor: DataFrame.
        eventos_a_dessazonalizar (list, optional): Lista de eventos a processar. Se None, todos.

    Retorna:
        dict: Novo dicionário em que cada valor é o DataFrame dessazonalizado ou o original.
    """
    resultado = {}
    for nome_evento, df in dicionario_eventos.items():
        if eventos_a_dessazonalizar is None or nome_evento in eventos_a_dessazonalizar:
            resultado[nome_evento] = dessazonalizar(df)
        else:
            resultado[nome_evento] = df
    return resultado
