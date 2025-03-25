import os
import requests
import zipfile
from bs4 import BeautifulSoup

def download_pdfs(url, output_folder):
    """
    Acessa a página fornecida, encontra os links dos PDFs Anexo I e II,
    faz o download e salva os arquivos no diretório especificado.
    """
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Cria a pasta de destino caso não exista

    pdf_paths = []
    for link in links:
        pdf_link = link['href']

        # Verifica se o link termina com ".pdf" e se é o "Anexo_I" ou "Anexo_II"
        if pdf_link.endswith('.pdf') and ('Anexo_I' in pdf_link or 'Anexo_II' in pdf_link):
            pdf_name = pdf_link.split("/")[-1]  # Obtém o nome do arquivo
            pdf_path = os.path.join(output_folder, pdf_name)  # Define o caminho de download

            pdf_response = requests.get(pdf_link)

            with open(pdf_path, 'wb') as file:
                file.write(pdf_response.content)  # Salva o PDF no diretório
            
            print(f"Baixado: {pdf_name}")
            pdf_paths.append(pdf_path)  # Adiciona o caminho do arquivo à lista

    return pdf_paths

def zip_files(file_paths, zip_name):
    """
    Compacta os arquivos baixados em um único arquivo ZIP.
    """
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in file_paths:
            zipf.write(file, os.path.basename(file)) 
    print(f"Arquivo ZIP criado: {zip_name}")

if __name__ == "__main__":
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    output_folder = "downloads"  # Diretório para salvar os PDFs
    zip_filename = "Anexos.zip"  # Nome do arquivo ZIP final

    pdfs = download_pdfs(url, output_folder)
    
    if pdfs:
        zip_files(pdfs, zip_filename)
    else:
        print("Nenhum anexo encontrado para download.")

