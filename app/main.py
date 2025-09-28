"""
Módulo principal do teste técnico de Analytics da Quod.
Este módulo carrega o dataset, realiza a limpeza dos dados e exibe os resultados.
O dataset é gerado com erros intencionais para simular situações reais de dados incompletos ou duplicados.
O arquivo que gera o dataset fictício está localizado em 'app/models/dataset_generator.py'.
"""

import pandas as pd
import numpy as np
import dotenv as env
import os

# === Configs ===

env.load_dotenv()
pd.set_option("display.float_format", "{:.2f}".format)

# === Constantes ===

CAMINHO_DATASET = os.getenv("DATASET_PATH")

# === Funções ===

def carregar_dataset() -> pd.DataFrame | None:
    try:
        df = pd.read_csv(CAMINHO_DATASET)
        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo no caminho {CAMINHO_DATASET} não foi encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao carregar o dataset: {e}")
        return None
    
def limpar_dataset(df: pd.DataFrame) -> pd.DataFrame:

    precos_unitarios = get_precos_unitarios(df)
    categorias = get_categorias(df)

    # Tipagem
    df["Data"] = pd.to_datetime(df["Data"], errors="coerce")
    df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce")
    df["Preço"] = pd.to_numeric(df["Preço"], errors="coerce")

    # Tratando valores de string vazios
    df.replace("", np.nan, inplace=True)

    # Tratando valores de quantidade nulos
    df = preencher_quantidade(df, precos_unitarios)
    df["Quantidade"] = df["Quantidade"].fillna(df["Quantidade"].median()) # Fallback

    # Tratando valores de preço nulos
    df = preencher_preco(df, precos_unitarios)
    df["Preço"] = df["Preço"].fillna(df["Preço"].median()) # Fallback

    # Tratando datas
    df["Data"] = df["Data"].ffill().bfill() # Preenchendo com o valor mais próximo

    # Tratando valores de produto nulos
    df = preencher_produto(df, precos_unitarios)
    df["Produto"] = df["Produto"].fillna("Produto Desconhecido") # Fallback

    # Tratando valores de categoria nulos
    df = preencher_categoria(df, categorias)
    df["Categoria"] = df["Categoria"].fillna("Categoria Desconhecida") # Fallback

    # Dropando repetidos
    df.drop_duplicates(inplace=True)

    return df

def preencher_categoria(df: pd.DataFrame, categorias: dict) -> pd.DataFrame:
    for indice, linha in df.iterrows():
        produto = linha["Produto"]
        categoria = linha["Categoria"]

        if pd.isna(categoria) and pd.notna(produto):
            if produto in categorias:
                df.at[indice, "Categoria"] = categorias[produto]
    return df

def preencher_produto(df: pd.DataFrame, precos_unitarios: dict) -> pd.DataFrame:
    for indice, linha in df.iterrows():
        produto = linha["Produto"]
        preco = linha["Preço"]
        quantidade = linha["Quantidade"]

        if pd.isna(produto) and pd.notna(preco) and pd.notna(quantidade):
            for prod, preco_unit in precos_unitarios.items():
                if np.isclose(preco, preco_unit * quantidade):
                    df.at[indice, "Produto"] = prod
                    break
    return df

def preencher_quantidade(df: pd.DataFrame, precos_unitarios: dict) -> pd.DataFrame:
    for indice, linha in df.iterrows():
        produto = linha["Produto"]
        preco = linha["Preço"]
        quantidade = linha["Quantidade"]

        if pd.isna(quantidade) and pd.notna(preco) and produto in precos_unitarios:
            df.at[indice, "Quantidade"] = preco / precos_unitarios[produto]
    
    return df

def preencher_preco(df: pd.DataFrame, precos_unitarios: dict) -> pd.DataFrame:
    for indice, linha in df.iterrows():
        produto = linha["Produto"]
        preco = linha["Preço"]
        quantidade = linha["Quantidade"]

        if pd.isna(preco) and pd.notna(quantidade) and produto in precos_unitarios:
            df.at[indice, "Preço"] = quantidade * precos_unitarios[produto]
    
    return df

def get_precos_unitarios(df: pd.DataFrame) -> dict:
    precos_unitarios = {}

    for _, linha in df.iterrows():
        produto = linha["Produto"]
        preco = linha["Preço"]
        quantidade = linha["Quantidade"]

        if pd.notna(produto) and pd.notna(preco) and pd.notna(quantidade) and quantidade != 0:
            if produto not in precos_unitarios:
                precos_unitarios[produto] = preco / quantidade

    return precos_unitarios

def get_categorias(df: pd.DataFrame) -> dict:
    categorias = {}

    for _, linha in df.iterrows():
        produto = linha["Produto"]
        categoria = linha["Categoria"]

        if pd.notna(produto) and pd.notna(categoria):
            if produto not in categorias:
                categorias[produto] = categoria

    return categorias

if __name__ == "__main__":
    dataset = carregar_dataset()

    if dataset is not None:
        print("Dataset carregado com sucesso!")
        print("Limpando dataset...")

        dataset_limpo = limpar_dataset(dataset)

        print("Dataset limpo com sucesso!")
        print(dataset_limpo.head(10))
  
    else:
        print("Falha ao carregar o dataset.")