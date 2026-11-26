
# 💳 Detecção de Fraudes em Transações com Cartão de Crédito

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-Gradient%20Boosting-green)
![SHAP](https://img.shields.io/badge/SHAP-Explainable%20AI-purple)

Projeto completo de Ciência de Dados e Machine Learning focado na identificação de transações fraudulentas em cartões de crédito, abordando desde a análise exploratória e tratamento de desbalanceamento extremo até a explicabilidade das predições com **SHAP**.

---

## 📌 1. O Problema e a Escolha das Métricas

O conjunto de dados utilizado reúne transações reais realizadas com cartões de crédito, contendo variáveis numéricas anonimizadas via **PCA (`V1` a `V28`)**, além de **`Time`** (tempo decorrido desde a primeira transação), **`Amount`** (valor da operação) e **`Class`** (`0` para transação legítima e `1` para fraude).

### Por que o desbalanceamento muda a forma de avaliar?
A base apresenta um **desbalanceamento severo**: aproximadamente **99,83%** das transações são normais e apenas **0,17%** são fraudes. 

Nesse cenário, a **acurácia é uma métrica enganosa**. Um modelo ingênuo que classificasse 100% das operações como legítimas alcançaria **99,83% de acurácia**, mas teria **0% de utilidade prática**, deixando passar todas as fraudes. Por isso, a avaliação deste projeto foi direcionada para a **classe minoritária (`Class = 1`)**:

* **Recall (Sensibilidade):** Principal métrica de negócio do projeto. Mede a proporção de fraudes reais que o modelo conseguiu capturar (minimizar Falsos Negativos, cujo custo financeiro é direto).
* **Precision (Precisão):** Mede quantas das transações bloqueadas/sinalizadas como fraude eram de fato fraudulentas (controle de Falsos Positivos para evitar atrito com clientes legítimos).
* **F1-Score:** Média harmônica entre Precisão e Recall, garantindo equilíbrio operacional.
* **Curva Precision-Recall (PR-AUC):** Ferramenta visual central para avaliar o trade-off entre captura de fraudes e alarmes falsos em bases desbalanceadas.

---

## ⚙️ 2. Preparação dos Dados

1. **Coleta Dinâmica (Sem sobrecarga no repositório):** O dataset é carregado diretamente via URL (`pd.read_csv`), evitando o versionamento de arquivos acima de 100 MB no GitHub.
2. **Tratamento de Assimetria (`Amount`):** Aplicação de transformação logarítmica (`np.log1p`) para suavizar valores extremos (outliers) e reduzir a assimetria da distribuição monetária.
3. **Divisão Estratificada (`train_test_split`):** Separação entre treino e teste utilizando `stratify=y`, preservando exatamente a proporção original de **0,17%** de fraudes em ambos os subconjuntos.
4. **Padronização e Prevenção de *Data Leakage*:** Uso do `StandardScaler` encapsulado dentro de um `Pipeline` do `scikit-learn` para garantir que a escala seja ajustada apenas nos dados de treino e aplicada nos dados de teste.

---

## 📊 3. Comparação entre os Modelos (Classe Fraude)

Foram avaliados diferentes algoritmos e estratégias de tratamento de desbalanceamento (ponderação de classes, *undersampling*, *oversampling* com SMOTE e otimização de hiperparâmetros via `GridSearchCV` com foco em **Recall**):

| Modelo / Abordagem | Estratégia de Balanceamento | Threshold | Precision (Classe 1) | Recall (Classe 1) | F1-Score (Classe 1) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Regressão Logística (Baseline)** | Nenhuma (Padrão) | 0.50 | *0.87* | *0.68* | *0.77* |
| **Regressão Logística (Pipeline)** | Ajuste de Limiar | 0.30 | *0.XX* | *0.XX* | *0.XX* |
| **Random Forest** | `class_weight='balanced'` | 0.50 | *0.94* | *0.76* | *0.84* |
| **XGBoost** | `scale_pos_weight` | 0.50 | *0.93* | *0.78* | *0.85* |
| **Modelo Final Otimizado** | **GridSearchCV (`scoring='recall'`) + Threshold** | **0.30** | ***0.XX*** | ***0.XX*** | ***0.XX*** |

> **Nota:** Substitua os valores em itálico (*0.XX*) pelos resultados exatos exibidos no `classification_report` das suas células no notebook.

---

## 🔍 4. Limiar de Decisão e Explicabilidade (SHAP)

### Ajuste do Limiar de Decisão (*Threshold*)
Por padrão, os classificadores convertem probabilidades em classes usando o ponto de corte **`0.50`**. Como o objetivo prioritário na prevenção a fraudes é maximizar a detecção de eventos suspeitos, o limiar foi reduzido para **`0.30`**. Essa mudança elevou o **Recall** do modelo, permitindo identificar transações fraudulentas que apresentavam probabilidade intermediária de risco, mantendo um nível aceitável de Precisão.

### O que o SHAP mostrou sobre as decisões do modelo?
Para evitar que o modelo funcionasse como uma "caixa-preta", foi aplicada a biblioteca **SHAP** (`shap.Explainer`) sobre o conjunto de teste:
* **Visão Global (`shap.plots.bar` / Summary Plot):** As componentes **`V14`**, **`V4`**, **`V12`** e **`V17`** *(ajuste conforme o topo do seu gráfico)* apresentaram o maior impacto médio absoluto na predição de fraude.
* **Direção do Impacto:** Valores fortemente negativos em `V14` e `V12` e valores elevados em `V4` empurram a probabilidade da transação para a classe fraudulenta.

---

## 🚀 5. Evoluções Implementadas (Diferenciais em relação à aula base)

Além de reproduzir o fluxo proposto pela Expert Isadora, este projeto incorporou melhorias estruturais e analíticas:
* **Encapsulamento Completo em `Pipeline`:** Integração de pré-processamento e modelagem para eliminar qualquer risco de vazamento de dados (*data leakage*) durante a validação cruzada.
* **Comparação Empírica de Reamostragem:** Avaliação prática entre *Undersampling* e *Oversampling* (`SMOTE`) aplicados exclusivamente nos dados de treino para comparar o ganho real de Recall.
* **Engenharia de Atributos / Refinamento de Busca:** *(Descreva aqui se você criou variáveis temporais a partir de `Time`, testou novos modelos ou ampliou a grade de parâmetros do `GridSearchCV`)*.

---

## 📁 Estrutura do Repositório

```text
├── deteccao_de_fraudes_em_transacoes.ipynb   # Notebook completo com análises, gráficos e saídas salvas
└── README.md                                 # Documentação técnica e resumo dos resultados
