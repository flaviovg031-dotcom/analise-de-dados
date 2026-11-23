# Análise de Cancelamento de Cartões de Crédito (Churn)

## 📌 Visão Geral
Este projeto aborda o desafio de **reduzir o cancelamento de cartões de crédito (churn)** a partir da análise de dados históricos de clientes ativos e cancelados. O objetivo é identificar padrões comportamentais e sinais associados à maior propensão ao cancelamento para apoiar ações de retenção.

* **Base de dados (GitHub):** [ClientesBanco.csv](https://github.com/flaviovg031-dotcom/analise-de-dados/blob/main/Analise_de_dados_ClientesBanco/ClientesBanco.csv)
* **Notebook da análise (GitHub):** [analise-de-dados_ClientesBanco_notebook-jupyter.ipynb](https://github.com/flaviovg031-dotcom/analise-de-dados/blob/main/Analise_de_dados_ClientesBanco/analise-de-dados_ClientesBanco_notebook-jupyter.ipynb)
* **Referência original do dataset:** [Kaggle — Credit Card Customers](https://www.kaggle.com/sakshigoyal7/credit-card-customers)

---

## 🛠️ Ferramentas e Bibliotecas Utilizadas
* **Python:** Linguagem utilizada para executar a extração, limpeza, exploração estatística e geração de visualizações do pipeline de dados.
* **pandas:** Utilizada para importar o arquivo CSV (`pd.read_csv`), remover a coluna `CLIENTNUM`, tratar valores ausentes (`dropna()`), inspecionar estrutura e estatísticas (`info()`, `describe()`) e calcular frequências/proporções (`value_counts()`).
* **plotly.express:** Utilizada para gerar histogramas comparativos entre `Cliente` e `Cancelado` (`px.histogram`) em todas as variáveis da base.
* **plotly.io:** Utilizada para configurar o renderizador (`pio.renderers.default`) e exibir/exportar os gráficos (`grafico.show("png")`).

---

## 🔄 Pipeline de Dados e Passo a Passo da Análise

### 1. Definição do Problema
* **Contexto:** Aumento significativo no cancelamento de cartões de crédito, gerando impacto financeiro negativo para a empresa.
* **Perguntas centrais:** Quais são os principais fatores/motivos associados ao cancelamento? Como identificar clientes com maior tendência a cancelar para agir de forma preventiva?

### 2. Coleta de Dados
* Extração da base `ClientesBanco.csv` (encoding `latin1`), contendo **10.127 registros iniciais** e colunas demográficas, de relacionamento e de uso do cartão (ex.: `Categoria`, `Idade`, `Sexo`, `Dependentes`, `Educação`, `Estado Civil`, `Faixa Salarial Anual`, `Categoria Cartão`, `Meses como Cliente`, `Produtos Contratados`, `Inatividade 12m`, `Contatos 12m`, `Limite`, `Limite Consumido`, `Limite Disponível`, `Valor Transacoes 12m`, `Qtde Transacoes 12m` e `Taxa de Utilização Cartão`).

### 3. ETL (Extract, Transform and Load)
* **Extract:** Leitura do arquivo CSV com `pandas` e remoção da coluna identificadora `CLIENTNUM`.
* **Transform:** Remoção de linhas com valores nulos via `dropna()` (restando `10.126` registros) e verificação de tipos de dados e estatísticas descritivas com `info()` e `describe().round(1)`.
* **Load:** Disponibilização do *DataFrame* tratado em memória para as etapas exploratórias no notebook.

### 4. EDA (Exploratory Data Analysis)
* Avaliação da distribuição da variável alvo `Categoria`:
  * **Cliente:** `8.499` registros
  * **Cancelado:** `1.627` registros (aproximadamente `16,1%` da base tratada; `20.0` no arredondamento `round(1)*100` aplicado no notebook)
* Comparação visual da distribuição entre `Cliente` e `Cancelado` para cada coluna da tabela.

### 5. Visualização de Dados (Gráficos)
* Geração de histogramas segmentados por `Categoria` em loop para todas as colunas usando `plotly.express` e controle de renderização com `plotly.io`:
  ```python
  import plotly.express as px
  import plotly.io as pio

  pio.renderers.default = "notebook"  # ou "browser", "vscode"

  for coluna in tabela:
      grafico = px.histogram(tabela, x=coluna, color="Categoria")
      grafico.show("png")
  ```

### 6. Interpretação e Geração de Insights

#### Principais sinais de risco de cancelamento
* **Menor quantidade de produtos contratados:** Quanto menos produtos o cliente possui com a instituição, maior tende a ser a chance de cancelamento; à medida que o engajamento em mais produtos aumenta, a tendência de cancelar cai.
* **Menor volume e valor de transações:** Clientes com menor quantidade e menor valor transacionado nos últimos 12 meses apresentam maior propensão ao cancelamento.
* **Maior quantidade de contatos:** Quanto maior o número de contatos realizados pelo cliente nos últimos 12 meses, maior é a chance de cancelamento — sinal de possível atrito, dúvida não resolvida ou insatisfação.

#### Perfil geral observado na base analisada
* Cerca de **80%** dos clientes estão na categoria de cartão **Blue**.
* Cerca de **90%** dos clientes têm idade entre **30 e 60 anos**.
* A escolaridade se divide de forma equilibrada entre **Ensino Médio** (~30%), **Ensino Superior** (~30%) e **Sem ensino formal / Não informado** (~30%).
* Cerca de **35%** possuem faixa salarial anual **menor que $40K** (`Less than $40K`).
* Cerca de **24%** têm ao menos **36 meses** de relacionamento como cliente.
* Cerca de **80%** passam até **3 meses** inativos (`Inatividade 12m`).

---

## 📂 Estrutura do Repositório
```text
Analise_de_dados_ClientesBanco/
├── ClientesBanco.csv
└── analise-de-dados_ClientesBanco_notebook-jupyter.ipynb
```

---

## ▶️ Como Executar
1. Clone o repositório:
   ```bash
   git clone [https://github.com/flaviovg031-dotcom/analise-de-dados.git](https://github.com/flaviovg031-dotcom/analise-de-dados.git)
   ```
2. Acesse a pasta do projeto e instale as dependências:
   ```bash
   pip install pandas plotly
   ```
3. Abra o notebook `analise-de-dados_ClientesBanco_notebook-jupyter.ipynb` no Jupyter Notebook ou VS Code e execute as células em sequência.

---

## ✍️ Autor
**Flavio Barbosa Cardoso da Silva** — Estudante de Engenharia de Produção | Análise de Dados
