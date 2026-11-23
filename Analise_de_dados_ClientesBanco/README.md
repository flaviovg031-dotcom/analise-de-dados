## Análise de dados - Clientes que cancelam o cartão de crédito.

### 📌 Visão Geral
[Escreva aqui um resumo curto e direto sobre o objetivo do projeto, qual contexto ele aborda e qual resultado principal ele entrega.]

---

### 🛠️ Ferramentas e Bibliotecas Utilizadas
Este projeto foi desenvolvido em **Python**, priorizando clareza, reprodutibilidade e visualizações interativas:

* **Python:** Linguagem principal utilizada para estruturar o pipeline de dados, aplicar regras de transformação e gerar análises.
* **pandas:** Utilizada para leitura, limpeza, filtragem, agregação e manipulação tabular dos dados.
* **plotly.express:** Utilizada para criar gráficos interativos de forma rápida e exploratória a partir dos *DataFrames*.
* **plotly.io:** Utilizada para gerenciar templates visuais, padronizar a aparência dos gráficos e exportar/renderizar figuras ou relatórios visuais.

---

### 🔄 Pipeline de Dados e Linha de Raciocínio
O desenvolvimento seguiu uma sequência estruturada em seis etapas para garantir que cada conclusão tivesse lastro nos dados e no contexto do problema:

#### 1. Definição do Problema
* **Objetivo:** [Qual pergunta de negócio ou problema operacional/analítico este projeto busca responder?]
* **Critérios de sucesso:** [O que define uma boa resposta ou um bom direcionamento a partir da análise?]

#### 2. Coleta de Dados
* **Fonte dos dados:** [Ex.: arquivo CSV, planilha, base pública, sistema interno, etc.]
* **Escopo:** [Período coberto, volume aproximado de registros e principais variáveis envolvidas.]

#### 3. ETL (Extract, Transform and Load)
* **Extract:** Carregamento dos dados brutos com `pandas` a partir de `[formato/origem do arquivo]`.
* **Transform:** Tratamento de valores ausentes, padronização de tipos de dados (datas, números, categorias), remoção de duplicidades e criação de colunas derivadas/métricas.
* **Load:** Salvamento ou disponibilização da base tratada (`[ex.: CSV limpo / estrutura pronta para análise]`) para as etapas seguintes.

#### 4. EDA (Exploratory Data Analysis)
* Investigação estatística e estrutural da base tratada para entender distribuições, tendências, concentrações, anomalias e relações entre variáveis antes de tirar conclusões definitivas.

#### 5. Visualização de Dados
* Construção de gráficos interativos com **`plotly.express`** e controle de layout/exportação com **`plotly.io`** para facilitar a leitura dos padrões encontrados na EDA e comunicar os achados de forma visual.

#### 6. Interpretação e Geração de Insights
* Tradução dos números e gráficos em achados práticos: o que os dados mostram, por que certos comportamentos ocorrem e quais ações ou recomendações fazem sentido a partir disso.
  


## ▶️ Como Executar
1. Clone o repositório:
   ```bash
   git clone [URL_DO_REPOSITORIO]
   ```
2. Instale as dependências:
   ```bash
   pip install pandas plotly
   ```
3. Execute o script ou abra o notebook principal:
   ```bash
   python [caminho/do/script.py]
   ```

---

## ✍️ Autor
**Flavio Barbosa Cardoso da Silva** — Estudante de Engenharia de Produção | Análise de Dados
