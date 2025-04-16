
# Impacto da Pandemia de COVID-19 sobre Eventos Cardiovasculares no Brasil
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Data: DATASUS](https://img.shields.io/badge/Data-DATASUS-blue)](https://datasus.saude.gov.br/)  
[![Status: Concluído](https://img.shields.io/badge/Status-Concluído-success)](https://github.com/username/repo)

---

## Sobre o Projeto

Este projeto analisa o impacto da pandemia de COVID-19 sobre eventos cardiovasculares no Brasil, utilizando dados públicos do DataSUS. O objetivo é identificar e avaliar mudanças nas internações e óbitos por condições como infarto, AVC, arritmias, trombose, insuficiência cardíaca e miocardite, comparando os períodos pré e pós-pandemia (2018–2025).

> ⚠️ Projeto desenvolvido para fins educacionais e prática de análise de dados. Os resultados não devem ser interpretados como diretrizes para decisões em saúde pública.

---

## Fonte dos Dados

- **Departamento de Informática do SUS (DATASUS)**  
- **Sistema de Informações Hospitalares (SIH/SUS) – TabNet**  
- Plataforma: [TabNet – DATASUS](http://tabnet.datasus.gov.br)

---

## Estrutura do Projeto

```
📁 dados_tratados/
│   ├── morbidade/
│   └── mortalidade/
📁 graficos/
│   ├── dessazonalizadas_morbidade/
│   └── dessazonalizadas_mortalidade/
📁 notebooks/
│   ├── 01_pre_processamento_dados.ipynb
│   ├── 02_analise_exploratoria.ipynb
│   ├── 03_dessazonalizacao_stl.ipynb
│   └── 04_testes_estatisticos.ipynb
📁 resultados/
📁 scripts/
│   ├── carregamento.py
│   ├── dessazonalizacao.py
│   ├── preprocessamento.py
│   ├── testes_estatisticos.py
│   └── visualizacao.py
```

---

## Etapas do Projeto

- **[01] [Pré-processamento](notebooks/01_pre_processamento_dados.ipynb):** limpeza de cabeçalhos, conversão de datas, tratamento de valores ausentes e padronização de colunas.  
- **[02] [Análise exploratória](notebooks/02_analise_exploratoria.ipynb):** visualização de tendências, comparação pré/pós-pandemia e análise da dispersão.  
- **[03] [Dessazonalização](notebooks/03_dessazonalizacao_stl.ipynb):** remoção de efeitos sazonais com o método STL.  
- **[04] [Testes estatísticos](notebooks/04_testes_estatisticos.ipynb):** comparação entre os períodos usando Mann-Whitney, Levene e *rank biserial*.

---

## Questões Investigadas

1. A pandemia alterou a tendência de internações e óbitos cardiovasculares no Brasil?
2. Houve aumento na variabilidade dos registros durante ou após a pandemia?
3. Quais eventos apresentaram maior instabilidade ou comportamento atípico?
4. As mudanças observadas são estatisticamente ou praticamente relevantes?

---

## Resultados e Descobertas

### Internações
- Queda abrupta em 2020, indicando possível colapso do sistema de saúde.
- Aumento na variabilidade após a pandemia, especialmente em arritmias.
- Recuperação e crescimento em infarto e AVC nos anos seguintes.

### Óbitos
- Crescimento contínuo, sem as quedas vistas nas internações.
- Insuficiência cardíaca e trombose apresentaram aumentos expressivos.
- Miocardite reverteu tendência de queda, com pico em 2021.

### Testes Estatísticos
- Nenhum dos testes de Mann-Whitney identificou significância estatística (p > 0.05).
- No entanto, o *intervalo de confiança do rank biserial* excluiu o zero em 4 dos 5 eventos de mortalidade analisados, indicando efeitos práticos robustos mesmo sem significância clássica.
- Óbitos por insuficiência cardíaca, AVC, miocardite e trombose apresentaram efeitos grandes e consistentes entre períodos.
- A análise de Levene confirmou aumento de variabilidade em eventos específicos, principalmente nas internações e em alguns óbitos (ex: infarto).

---

## Conclusão

Apesar da ausência de significância estatística convencional, os *intervalos de confiança do efeito* revelaram mudanças relevantes após a pandemia em diversos desfechos.

Eventos como óbitos por insuficiência cardíaca, AVC, miocardite e trombose apresentaram aumentos sistemáticos com efeitos práticos consistentes, segundo o rank biserial.

Os achados reforçam a importância de se analisar medidas de efeito com intervalo de confiança, especialmente em contextos com variabilidade alta ou eventos raros, e de não se limitar apenas à interpretação de valores de p.


## Tecnologias Utilizadas

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)]()  
[![Pandas](https://img.shields.io/badge/Pandas-1.5.0+-150458?style=flat-square&logo=pandas&logoColor=white)]()  
[![NumPy](https://img.shields.io/badge/NumPy-1.23.0+-013243?style=flat-square&logo=numpy&logoColor=white)]()  
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.6.0+-3776AB?style=flat-square&logo=matplotlib&logoColor=white)]()  
[![SciPy](https://img.shields.io/badge/SciPy-1.9.0+-8CAAE6?style=flat-square&logo=scipy&logoColor=white)]()  
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)]()  
[![Seaborn](https://img.shields.io/badge/Seaborn-0.12.0+-76B900?style=flat-square&logo=python&logoColor=white)]()  
[![Statsmodels](https://img.shields.io/badge/Statsmodels-0.13.0+-4B8BBE?style=flat-square&logo=python&logoColor=white)]()  

---

## Como Reproduzir

1. Clone este repositório:

```bash
git clone https://github.com/victorvanazzi/impacto-covid-eventos-cardiovasculares.git
cd impacto-covid-eventos-cardiovasculares
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

3. Instale o projeto no modo editável para garantir o uso correto dos scripts:

```bash
pip install -e .
```

4. Execute os notebooks da pasta `/notebooks` para acompanhar todas as etapas da análise:

```bash
jupyter notebook notebooks/
```

Ou rode diretamente os scripts desejados, como:

```bash
python scripts/carregamento.py
```

>  Requisitos: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`.

---

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
