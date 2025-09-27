import pandas as pd
import numpy as np
import random

qtde_produtos = 50

# ID, Data, Produto, Categoria, Quantidade, Preço

categorias = {
    "ELETRONICOS": "Eletrônicos",
    "ALIMENTOS": "Alimentos",
    "ACESSORIOS": "Acessórios"
}

produtos = {
    "Notebook": categorias["ELETRONICOS"],
    "Computador Gamer": categorias["ELETRONICOS"],
    "Headset Logitech": categorias["ACESSORIOS"],
    "Geforce RTX 5090": categorias["ELETRONICOS"],
    "Café Pelé 500g": categorias["ALIMENTOS"],
    "Lasanha Congelada 500g": categorias["ALIMENTOS"],
    "Pinhão 1kg": categorias["ALIMENTOS"],
    "Sucrilhos": categorias["ALIMENTOS"]
}

produtos_escolhidos = random.choices(list(produtos.items()), k=qtde_produtos)
produtos_lista, categorias_lista = zip(*produtos_escolhidos)

df = pd.DataFrame(
  {
    "ID": range(1, qtde_produtos + 1),
    "Produto": produtos_lista,
    'Categoria': categorias_lista
  }
)

print(df)

