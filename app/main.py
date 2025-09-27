import pandas as pd
import numpy as np
import dotenv as env
import os

# === Configs ===

# Carregando variáveis de ambiente do arquivo .env
env.load_dotenv()
DATASET_PATH = os.getenv("DATASET_PATH")

# === Funções ===

def load_dataset():
    try:
        df = pd.read_csv(DATASET_PATH)
        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo no caminho {DATASET_PATH} não foi encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao carregar o dataset: {e}")
        return None

if __name__ == "__main__":
    dataset = load_dataset()

    if dataset is not None:
        print("Dataset carregado com sucesso!")
        print(dataset.head())
  
    else:
        print("Falha ao carregar o dataset.")