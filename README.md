# Processamento de Dados de Sensores para TCC

Este repositório contém scripts para o tratamento inicial dos dados de sensores de movimento e frequência cardíaca coletados para um Trabalho de Conclusão de Curso (TCC). Os dados brutos são processados e salvos em arquivos CSV para análise subsequente.

## Análise Exploratória de Dados

A análise exploratória dos dados (EDA) foi realizada para entender a estrutura e os padrões nos dados de movimento e frequência cardíaca.

### Passos da EDA

1. **Carregamento dos dados**: Os dados foram carregados dos arquivos CSV.
2. **Entendimento da estrutura dos dados**: Foram verificadas as formas dos dados, tipos de dados e valores ausentes.
3. **Análise de estatísticas descritivas**: Estatísticas básicas foram obtidas.
4. **Visualização dos dados**: Gráficos foram criados para visualizar distribuições, tendências e correlações, incluindo análise por `label`.
5. **Identificação e tratamento de valores ausentes**: Valores ausentes ou inconsistentes foram identificados e tratados.

O arquivo da EDA podem ser encontrados na pasta `src/eda/`.

### Estrutura do Repositório

```plaintext
tcc-dataset-processing/
├── data/
│   ├── motion/
│   │   └── ... (arquivos .txt)
│   └── heart_rate/
│       └── ... (arquivos .txt)
├── src/
│   ├── process_motion_data.py
│   ├── process_heart_rate_data.py
│   └── eda/
│       └── analise_exp.ipynb
├── results/
│   ├── motion.csv
│   ├── heartrate.csv
├── README.md
├── requirements.txt
└── .gitignore
