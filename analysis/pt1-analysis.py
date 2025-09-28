import dotenv as env
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# === Configs ===
env.load_dotenv()
pd.set_option("display.float_format", "{:.2f}".format)

# === Constantes ===
CAMINHO_DATASET_LIMPO = os.getenv("CLEANED_DATASET_PATH")
CAMINHO_PLOTS = os.getenv("PLOTS_PATH")

# === Funções ===
def carregar_dataset(caminho: str) -> pd.DataFrame | None:
    try:
        df = pd.read_csv(caminho)
        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo no caminho {caminho} não foi encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao carregar o dataset: {e}")
        return None

def get_quantidade_vendas_por_produto(df: pd.DataFrame) -> pd.DataFrame:
    df["Total_Vendas"] = df["Quantidade"] * df["Preço"]
    resultado = df.groupby("Produto")["Total_Vendas"].sum().reset_index()
    return resultado

def get_produto_com_mais_vendas(vendas_totais_df: pd.DataFrame) -> pd.Series:
    produto_top = vendas_totais_df.loc[vendas_totais_df["Total_Vendas"].idxmax()]
    return produto_top

def get_quantidade_vendas_por_produto_individual(df: pd.DataFrame) -> pd.DataFrame:
    total_vendas_por_produto = df.groupby("Produto")["Quantidade"].sum().reset_index()
    total_vendas_por_produto.rename(columns={"Quantidade": "Total_Quantidade"}, inplace=True)
    return total_vendas_por_produto

def plotar_grafico_vendas_mensais(df: pd.DataFrame):
    df['Data'] = pd.to_datetime(df['Data'])
    df['AnoMes'] = df['Data'].dt.to_period('M')
    vendas_mensais = df.groupby('AnoMes')['Quantidade'].sum().reset_index()
    vendas_mensais['AnoMes'] = vendas_mensais['AnoMes'].dt.to_timestamp()

    plt.figure(figsize=(10, 6))
    plt.plot(vendas_mensais['AnoMes'], vendas_mensais['Quantidade'], marker='o')
    plt.title('Tendência de Vendas Mensais ao Longo do Tempo')
    plt.xlabel('Mês')
    plt.ylabel('Quantidade Vendida')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(CAMINHO_PLOTS)

if __name__ == "__main__":
    print(f"\n====================================\n")
    print("Análise de Dados - Parte 1")

    df_limpo = carregar_dataset(CAMINHO_DATASET_LIMPO)

    if df_limpo is not None:

        vendas_por_produto = get_quantidade_vendas_por_produto(df_limpo)
        print(vendas_por_produto)
        print(f"\n====================================\n")

        produto_top_series = get_produto_com_mais_vendas(vendas_por_produto)

        produto = produto_top_series["Produto"]
        total_vendas = produto_top_series["Total_Vendas"]

        print(f"Produto com maior número de vendas totais:")
        print(f"Produto: {produto}")
        print(f"Total de Vendas: R$ {total_vendas:.2f}")

        print(f"\n====================================\n")

        vendas_por_produto_individual = get_quantidade_vendas_por_produto_individual(df_limpo)
        print(vendas_por_produto_individual)

        print(f"\n====================================\n")

        plotar_grafico_vendas_mensais(df_limpo)

    else:
        print("Não foi possível carregar o dataset limpo para análise.")
