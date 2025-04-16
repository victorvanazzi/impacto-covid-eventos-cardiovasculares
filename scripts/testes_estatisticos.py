from scipy.stats import mannwhitneyu, levene
import pandas as pd
import numpy as np

def calcular_rank_biserial(pre, pos):
    n_pre = len(pre)
    n_pos = len(pos)
    U, _ = mannwhitneyu(pre, pos, alternative="greater")
    r_rb = (2 * U - n_pre * n_pos) / (n_pre * n_pos)
    return r_rb

def bootstrap_ic_rank_biserial(pre, pos, n_bootstrap=1000, seed=42):
    np.random.seed(seed)
    r_vals = []

    pre = np.array(pre)
    pos = np.array(pos)

    for _ in range(n_bootstrap):
        sample_pre = np.random.choice(pre, size=len(pre), replace=True)
        sample_pos = np.random.choice(pos, size=len(pos), replace=True)
        r = calcular_rank_biserial(sample_pre, sample_pos)
        r_vals.append(r)

    ic_inf = float(np.percentile(r_vals, 2.5))
    ic_sup = float(np.percentile(r_vals, 97.5))
    return ic_inf, ic_sup

def aplicar_testes_estatisticos(df, coluna_valor="Total", data_corte="2020-01-01"):
    """
    Aplica Mann-Whitney, Levene e Rank Biserial com intervalo de confiança (bootstrap).
    Divide os dados em pré e pós-pandemia com base na data_corte.
    """
    df = df.dropna(subset=["data", coluna_valor]).sort_values("data")
    df["data"] = pd.to_datetime(df["data"])
    
    pre = df[df["data"] < data_corte][coluna_valor]
    pos = df[df["data"] >= data_corte][coluna_valor]

    if len(pre) < 3 or len(pos) < 3:
        return {
            "mannwhitney_p": None,
            "levene_p": None,
            "rank_biserial_r": None,
            "rank_biserial_ic": (None, None)
        }

    # Mann-Whitney e effect size
    u_res = mannwhitneyu(pre, pos, alternative="greater")
    U = u_res.statistic
    p_mw = u_res.pvalue

    n_pre, n_pos = len(pre), len(pos)
    r_rb = (2 * U - n_pre * n_pos) / (n_pre * n_pos)

    # Bootstrap para IC do rank biserial
    ic_rb = bootstrap_ic_rank_biserial(pre, pos)

    resultados = {
        "mannwhitney_p": p_mw,
        "rank_biserial_r": r_rb,
        "rank_biserial_ic": ic_rb,
        "levene_p": levene(pre, pos).pvalue,
        "media_pre": pre.mean(),
        "media_pos": pos.mean(),
        "cv_pre": pre.std() / pre.mean(),
        "cv_pos": pos.std() / pos.mean()
    }

    return resultados
