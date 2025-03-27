import os
import requests
from bs4 import BeautifulSoup
import zipfile

def download_files(url, output_folder, current_year):
    """
    Baixa os arquivos zip dos últimos 2 anos de uma URL 
    com base no ano atual e salva na pasta de destino,
    em seguida descompacta os arquivos zip.
    """
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)

    for link in links:
        year = link['href'].split("/")[0]

        # Verifica se o link é dos 2 últimos anos
        if str(current_year-1) in year or str(current_year-2) in year:
            response = requests.get(f"{url}{year}")
            files_path = os.path.join(output_folder, year)

            if not os.path.exists(files_path):
                os.makedirs(files_path) 
            
            soup = BeautifulSoup(response.text, 'html.parser')

            # Faz o download de cada arquivo daquele ano
            for link_year in soup.find_all('a', href=True):
                if link_year['href'].endswith('.zip'):  # Procura por aquivos .zip
                    file_path = os.path.join(files_path, link_year['href'])
                    file_response = requests.get(f"{url}{year}/{link_year['href']}")
                    with open(file_path, 'wb') as file:
                        file.write(file_response.content)
                    
                    print(f"Download concluído: {link_year['href']}")

                    with zipfile.ZipFile(file_path, 'r') as zip_ref:
                        zip_ref.extractall(files_path)

                    print(f"Descompactado: {link_year['href']}")

        

def download_csv(url, output_folder):
    """
    Baixa o arquivo csv de uma URL e salva na pasta de destino.
    """
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder) 

    for link in links:
        csv_name = link['href'].split("/")[-1]
        
        if csv_name.endswith('.csv'):   # Procura por aquivos .csv
            csv_link = f"{url}/{csv_name}"
            csv_response = requests.get(csv_link)
            csv_path = os.path.join(output_folder, csv_name)

            with open(csv_path, 'wb') as file:
                file.write(csv_response.content)
                    
            print(f"Download concluído: {csv_name}")


if __name__ == "__main__":
    output_folder = "downloads"
    current_year = 2025
    url_repository = 'https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/'
    url_dados_cadastrais = 'https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/'
    
    download_files(url_repository, output_folder, current_year)
    download_csv(url_dados_cadastrais, output_folder)