"""
Módulo principal do teste técnico de Analytics da Quod.
Este módulo carrega o dataset, realiza a limpeza dos dados e exibe os resultados.
O dataset é gerado com erros intencionais para simular situações reais de dados incompletos ou duplicados.
O arquivo que gera o dataset fictício está localizado em 'app/models/dataset_generator.py'.
"""

import unicodedata
import pandas as pd
import numpy as np
import dotenv as env
import os

# === Configs ===

env.load_dotenv()
pd.set_option("display.float_format", "{:.2f}".format)

# === Constantes ===

CAMINHO_DATASET = os.getenv("DIRTY_DATASET_PATH")

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

    # Normalizando texto
    df["Produto"] = df["Produto"].apply(normalizar_texto)
    df["Categoria"] = df["Categoria"].apply(normalizar_texto)

    precos_unitarios = get_precos_unitarios(df)
    categorias = get_categorias(df)

    # Tipagem
    df["Data"] = pd.to_datetime(df["Data"], errors="coerce")
    df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce")
    df["Preço"] = pd.to_numeric(df["Preço"], errors="coerce")

    # Tratando valores de string vazios
    df.replace("", np.nan, inplace=True)

    # Tratando valores de quantidade
    df = preencher_quantidade(df) # Preenchendo com a mediana
    df["Quantidade"] = df["Quantidade"].fillna(1) # Fallback

    # Tratando valores de preço nulos
    df = preencher_preco(df, precos_unitarios)
    df["Preço"] = df["Preço"].fillna(df["Preço"].median()) # Fallback

    # Tratando datas
    df = preencher_data(df) # Preenchendo com o valor anterior ou posterior
    df["Data"] = df["Data"].fillna(pd.to_datetime("2023-01-01")) # Fallback

    # Tratando valores de produto nulos
    df = preencher_produto(df, precos_unitarios)
    df["Produto"] = df["Produto"].fillna("PRODUTO DESCONHECIDO") # Fallback

    # Tratando valores de categoria nulos
    df = preencher_categoria(df, categorias)
    df["Categoria"] = df["Categoria"].fillna("CATEGORIA DESCONHECIDA") # Fallback

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

        if pd.isna(produto) and pd.notna(preco):
            for prod, preco_unit in precos_unitarios.items():
                if np.isclose(preco, preco_unit):
                    df.at[indice, "Produto"] = prod
                    break
    return df

def preencher_preco(df: pd.DataFrame, precos_unitarios: dict) -> pd.DataFrame:
    for indice, linha in df.iterrows():
        produto = linha["Produto"]
        preco = linha["Preço"]

        if pd.isna(preco) and produto in precos_unitarios:
            df.at[indice, "Preço"] = precos_unitarios[produto]
    
    return df

def preencher_data(df: pd.DataFrame) -> pd.DataFrame:
    df["Data"] = df["Data"].ffill().bfill()
    return df

def preencher_quantidade(df: pd.DataFrame) -> pd.DataFrame:
    if df["Quantidade"].notna().any():
        df["Quantidade"] = df["Quantidade"].fillna(df["Quantidade"].median())
    else:
        df["Quantidade"] = df["Quantidade"].fillna(0)
    return df

def normalizar_texto(texto: str) -> str:
    if pd.isna(texto):
        return texto
    
    texto = texto.strip().upper()
    texto = "".join(
        char for char in unicodedata.normalize("NFD", texto)
        if unicodedata.category(char) != "Mn"
    )

    return texto

def get_precos_unitarios(df: pd.DataFrame) -> dict:
    precos_unitarios = {}

    for _, linha in df.iterrows():
        produto = linha["Produto"]
        preco = linha["Preço"]

        if pd.notna(produto) and pd.notna(preco):
            if produto not in precos_unitarios:
                precos_unitarios[produto] = preco

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

def salvar_dataset(df: pd.DataFrame, caminho: str) -> None:
    try:
        df.to_csv(caminho, index=False)
        print(f"Dataset limpo salvo com sucesso em {caminho}")
    except Exception as e:
        print(f"Erro ao salvar o dataset: {e}")

if __name__ == "__main__":
    dataset = carregar_dataset()

    if dataset is not None:
        print("Dataset carregado com sucesso!")
        print("Limpando dataset...")

        dataset_limpo = limpar_dataset(dataset)

        print("Dataset limpo com sucesso!")
        print(dataset_limpo.head(10))

        salvar_dataset(dataset_limpo, "./dataset/clean/data_clean.csv")
  
    else:
        print("Falha ao carregar o dataset.")