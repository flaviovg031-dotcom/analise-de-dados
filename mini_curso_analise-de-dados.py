# Desafio: Você trabalha em uma grande empresa de Cartão de Crédito e o diretor da empresa percebeu que o número de clientes que cancelam seus cartões tem aumentado significativamente, causando prejuízos enormes para a empresa. 
# O que fazer para evitar isso? Como saber as pessoas que têm maior tendência a cancelar o cartão?

# O que temos: 
# Temos 1 base de dados com informações dos clientes, tanto clientes atuais quanto clientes que cancelaram o cartão
# Download da Base de Dados: Botão na página.
# Referência: https://www.kaggle.com/sakshigoyal7/credit-card-customers

# Passo 1: Importar a base de dados
# Passo 2: Visualizar e tratar essa base de dados
# Passo 3: "Dar uma olhada" na sua base de dados
# Passo 4: Construir uma análise para identificar o motivo de cancelamento
  # Identificar qual o motivo ou os principais motivos dos clientes estarem cancelando o cartão de crédito.

#importando as bibliotecas necessárias
import pandas as pd
import plotly.express as px
#Fazendo o ETL
#1. Extração
#impotando a base de dados.
tabela = pd.read_csv("ClientesBanco.csv", encoding="latin1")
#2. Transformação
tabela = tabela.drop("CLIENTNUM", axis=1)
tabela = tabela.dropna()
tabela.info()
tabela.describe()
#3.Carga de dados
print(tabela.head())
print(tabela.describe().round(1))

#EDA - Análise Exploratória dos dados
qtde_categoria = tabela["Categoria"].value_counts()
print(qtde_categoria)

qtde_categoria_perc = tabela["Categoria"].value_counts(normalize=True)
print(qtde_categoria_perc)

#Geração de visualização de dados
grafico = px.histogram(tabela,x="Idade", color="Categoria")
grafico.show()
