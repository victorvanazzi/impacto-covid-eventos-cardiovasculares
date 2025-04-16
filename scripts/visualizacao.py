# scripts/graficos.py

import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
import pandas as pd
from pathlib import Path


def plot_tendencia_pre_pos_pandemia(df, titulo, ylabel="Total", coluna_valor="Total", salvar_em=None, data_min=None):
    """
    Gera dois gráficos (pré e durante pandemia) com regressão linear.
    Exibe e salva, e permite cortar dados antes de uma data mínima.

    Parâmetros:
        df: DataFrame com colunas 'data' e a coluna de valores numéricos
        titulo: Título do gráfico
        ylabel: Rótulo do eixo Y
        coluna_valor: Nome da coluna que será usada no eixo Y
        salvar_em: Pasta de destino (se quiser salvar PNG)
        data_min: Data mínima para análise (ex: '2018-01-01')
    """
    df = df.dropna(subset=["data", coluna_valor]).sort_values("data")

    if data_min:
        df = df[df["data"] >= pd.to_datetime(data_min)]

    dados_pre = df[df["data"] < pd.to_datetime("2020-01-01")].copy()
    dados_pos = df[df["data"] >= pd.to_datetime("2020-01-01")].copy()

    dados_pre["data_num"] = mdates.date2num(dados_pre["data"])
    dados_pos["data_num"] = mdates.date2num(dados_pos["data"])

    fig, ax = plt.subplots(1, 2, figsize=(16, 6), sharey=True)

    sns.regplot(x="data_num", y=coluna_valor, data=dados_pre,
                ax=ax[0], scatter_kws={"alpha": 0.5}, line_kws={"color": "red"})
    ax[0].set_title(f"{titulo} – Pré-pandemia")
    ax[0].set_xlabel("Data")
    ax[0].set_ylabel(ylabel)
    ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    sns.regplot(x="data_num", y=coluna_valor, data=dados_pos,
                ax=ax[1], scatter_kws={"alpha": 0.5}, line_kws={"color": "red"})
    ax[1].set_title(f"{titulo} – Durante pandemia")
    ax[1].set_xlabel("Data")
    ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    for a in ax:
        a.tick_params(axis='x', rotation=45)

    plt.tight_layout()

    if salvar_em:
        Path(salvar_em).mkdir(parents=True, exist_ok=True)
        nome_arquivo = f"{titulo.lower().replace(' ', '_').replace('–', '-')}.png"
        caminho = Path(salvar_em) / nome_arquivo
        plt.savefig(caminho, dpi=300)

    plt.show()


def plotar_comparativo_eventos(dicionario_eventos, titulo_base, ylabel, coluna_valor="Total", salvar_em=None):
    """
    Gera gráficos para todos os eventos de um dicionário de dataframes.

    Parâmetros:
        dicionario_eventos: dict como dados["mortalidade"] ou dados["morbidade"]
        titulo_base: prefixo comum para o título (ex: "Óbitos por", "Internações –")
        ylabel: rótulo do eixo Y (ex: "Óbitos", "Internações")
        coluna_valor: nome da coluna a ser usada como valores no eixo Y
        salvar_em: pasta onde os gráficos serão salvos (ou None para exibir)
    """
    for nome_evento, df in dicionario_eventos.items():
        if coluna_valor not in df.columns:
            print(f"[AVISO] Coluna '{coluna_valor}' não encontrada em: {nome_evento}. Ignorando.")
            continue

        nome_formatado = nome_evento.replace("obitos_", "").replace("internacoes_", "").replace("_", " ").title()
        titulo = f"{titulo_base} {nome_formatado}"
        print(f"Gerando gráfico: {titulo}")
        plot_tendencia_pre_pos_pandemia(df, titulo=titulo, ylabel=ylabel, coluna_valor=coluna_valor, salvar_em=salvar_em)