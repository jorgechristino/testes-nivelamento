import os
import tabula
import pandas as pd
import zipfile

def extract_table_from_pdf(pdf_path):
  """
  Extrai todas as tabelas do PDF e retorna um DataFrame único
  """
  tables = tabula.read_pdf(pdf_path, pages='all', lattice=True)

  if tables:
    df = pd.concat(tables[2:], ignore_index=True) # Remove as duas primeiras tabelas e junta as demais
    print("Tabelas extraídas do PDF.")
    return df
  else:
    print("Não foi possível extrair os dados do PDF.")
    return
  
def save_data_to_csv(df, csv_name):
  """
  Salva os dados em uma tabela estruturada, em formato csv. 
  """
  df.to_csv(csv_name)
  print(f"Arquivo CSV criado: {csv_name}.")

def zip_csv(zip_name):
  """
  Compacta o arquivo csv
  """
  with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(csv_name, os.path.basename(csv_name))
  
  print(f"Arquivo ZIP criado: {zip_name}.")

def transform_data(df):
  """
  Substitui as abreviações OD e AMB pelas descrições completas.
  """
  df.rename(columns={"OD": "SEG. ODONTOLÓGICA", "AMB": "SEG. AMBULATORIAL"}, inplace=True)
  return df

if __name__ == "__main__":
  pdf_path = "../1_Teste_Web_Scraping/downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"  # Caminho do PDF extraído no Teste 1
  csv_name = "Rol_de_Procedimentos.csv"
  zip_name = "Teste_Jorge.zip"

  df = extract_table_from_pdf(pdf_path)
  save_data_to_csv(df, csv_name)
  zip_csv(zip_name)
  df = transform_data(df)
  save_data_to_csv(df, "Dados_Transformados.csv")
  print(df)
  

