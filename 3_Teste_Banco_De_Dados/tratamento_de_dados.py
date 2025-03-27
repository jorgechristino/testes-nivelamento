import os
import pandas as pd

def data_processing(path):
  """
  Função para tratar os dados dos arquivos csv,
  trocar os valores dos campos "VL_SALDO_INICIAL" e 
  "VL_SALDO_FINAL" de "," para "."
  """
  for file in os.listdir(path):
    if file.endswith(".csv"):  # Verifica se é um arquivo CSV
        file_path = os.path.join(path, file)
        
        df = pd.read_csv(file_path, delimiter=";", dtype=str)

        df["VL_SALDO_INICIAL"] = df["VL_SALDO_INICIAL"].str.replace(",", ".", regex=True)
        df["VL_SALDO_FINAL"] = df["VL_SALDO_FINAL"].str.replace(",", ".", regex=True)

        # Salvar o arquivo com as alterações
        df.to_csv(file_path, index=False, sep=";")

        print(f"Arquivo processado: {file}")

if __name__ == "__main__":
  # Caminhos dos arquivos csv
  csv_path_2023 = "downloads/2023"
  csv_path_2024 = "downloads/2024"

  data_processing(csv_path_2023)
  data_processing(csv_path_2024)

