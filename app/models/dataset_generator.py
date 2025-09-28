"""
Este script gera um dataset fictício de vendas, incluindo alguns erros intencionais
como valores faltantes e duplicatas, para fins de teste e demonstração.
O dataset é salvo em um arquivo CSV chamado 'dataset_vendas.csv'.
"""

import pandas as pd
import numpy as np
import random

QTDE_PRODUTOS = 50

categorias = {
    "ELETRONICOS": "Eletrônicos",
    "ALIMENTOS": "Alimentos",
    "ACESSORIOS": "Acessórios"
}

# Produto, Categoria, Preço Unitário
produtos = {
    "Notebook": [categorias["ELETRONICOS"], 4500.00],
    "Computador Gamer": [categorias["ELETRONICOS"], 5500.00],
    "Headset Logitech": [categorias["ACESSORIOS"], 190.00],
    "Geforce RTX 2070": [categorias["ELETRONICOS"], 2300.00],
    "Café Pelé 500g": [categorias["ALIMENTOS"], 15.00],
    "Lasanha Congelada 500g": [categorias["ALIMENTOS"], 30.00],
    "Pinhão 1kg": [categorias["ALIMENTOS"], 25.00],
    "Sucrilhos": [categorias["ALIMENTOS"], 12.00]
}

# Escolhendo produtos aleatoriamente
produtos_escolhidos = random.choices(list(produtos.items()), k=QTDE_PRODUTOS)

# Separando os detalhes dos produtos escolhidos
produtos_lista = [nome for nome, _ in produtos_escolhidos]
categorias_lista = [detalhes[0] for _, detalhes in produtos_escolhidos]
preco_unitario_lista = [detalhes[1] for _, detalhes in produtos_escolhidos]

# Gerando quantidades aleatórias entre 1 e 20
quantidades = np.random.randint(1, 20, size=QTDE_PRODUTOS)

# Gerando datas aleatórias em 2023
data_inicial = pd.to_datetime("2023-01-01")
data_final = pd.to_datetime("2023-12-31")

num_dias = (data_final - data_inicial).days + 1 # Quantos dias existem no intervalo entre as datas
datas = data_inicial + pd.to_timedelta(np.random.randint(0, num_dias, size=QTDE_PRODUTOS), unit='D') # Gerando datas aleatórias dentro do intervalo

# Ordenando as datas (pois as compras geralmente são registradas em ordem cronológica)
datas = np.sort(datas)

# # ID, Data, Produto, Categoria, Quantidade, Preço
df = pd.DataFrame(
  {
    "ID": range(1, QTDE_PRODUTOS + 1),
    "Data": datas,
    "Produto": produtos_lista,
    "Categoria": categorias_lista,
    "Quantidade": quantidades,
    "Preço": preco_unitario_lista
  }
)

# Criando erros no dataset

"""
1. Valores faltantes
2. Duplicatas
"""

# 1. Valores faltantes
num_faltantes = int(QTDE_PRODUTOS * 0.1) # 10% dos dados terão valores faltantes
indices_faltantes = random.sample(range(QTDE_PRODUTOS), num_faltantes) # Seleciona índices aleatórios

for indice in indices_faltantes:
    coluna_aleatoria = random.choice(df.columns[1:]) # Evitar a coluna ID
    df.at[indice, coluna_aleatoria] = np.nan

# 2. Duplicatas
num_duplicatas = int(QTDE_PRODUTOS * 0.05) # 5% dos dados serão duplicados
indices_duplicatas = random.sample(range(QTDE_PRODUTOS), num_duplicatas)

for indice in indices_duplicatas:
    df = df.loc[df.index.tolist() + [indice]] # Adiciona a linha duplicada
    df = df.reset_index(drop=True) # Reseta os índices após adicionar duplicatas

# Salvando o dataset em um arquivo CSV
df.to_csv("./dataset/dirty/data_dirty.csv", index=False)
print("Dataset sujo gerado com sucesso em 'dataset/dirty/data_dirty.csv'")