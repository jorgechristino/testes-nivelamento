# Testes IntuitiveCare

Repositório para resolução dos testes.

## Ferramentas utilizadas

- Python
- PostgreSQL
- Vue.js
- Postman

## Resquisitos de instalação

- Python
- NPM
- Java
- PostgreSQL

## 1. Teste de Web Scraping

Navegue até o diretório do teste

```sh
cd 1_Teste_Web_Scraping
```

### Ativando o ambiente virtual e instalando dependências

1. Criação do ambiente virtual

```sh
python -m venv venv
```

2. Ative o ambiente virtual

```sh
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

3. Instalando as dependências

```sh
pip install -r requirements.txt
```

### Executando o arquivo principal

```sh
python main.py
```

## 2. Teste de Transformação de Dados

Para este teste é necessário instalar o java para o funcionamento da biblioteca tabula.

Navegue até o diretório do teste

```sh
cd 2_Teste_Transformacao_Dados
```

### Ativando o ambiente virtual e instalando dependências

1. Criação do ambiente virtual

```sh
python -m venv venv
```

2. Ative o ambiente virtual

```sh
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

3. Instalando as dependências

```sh
pip install -r requirements.txt
```

### Executando o arquivo principal

```sh
python main.py
```

## 3. Teste de Banco de Dados

Navegue até o diretório do teste

```sh
cd 3_Teste_Banco_De_Dados
```

### Ativando o ambiente virtual e instalando dependências

1. Criação do ambiente virtual

```sh
python -m venv venv
```

2. Ative o ambiente virtual

```sh
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

3. Instalando as dependências

```sh
pip install -r requirements.txt
```

### Tarefas de Preparação

Execute o arquivo para baixar os dados dos repositórios

```sh
python baixar_dados.py
```

Execute o arquivo para tratar os dados baixados. Trocou-se os números com "," para ".", para que o Postgre entenda os valores como números reais (float).

```sh
python tratamento_de_dados.py
```

### Tarefas de Código

1. Crie o seu banco de dados no Postgre.

2. Execute as queries presente no arquivo [criar_tabelas.sql](3_Teste_Banco_De_Dados/criar_tabelas.sql) para criar as tabelas no banco de dados.

3. Em seguida importe os dados .csv, executando as queries presente no arquivo [importar_dados.sql](3_Teste_Banco_De_Dados/importar_dados.sql). Substitua o caminho completo nas importações nas queries em:

```sql
FROM '...\3_Teste_Banco_De_Dados\downloads\Relatorio_cadop.csv'
```

4. Para fazer as consultas, execute as queries do arquivo [consultas_analiticas.sql](3_Teste_Banco_De_Dados/consultas_analiticas.sql)

## 4. Teste de API

Navegue até o diretório do teste

```sh
cd 4_Teste_API
```

1. [Backend](4_Teste_API/backend/): Siga os comandos para executar a API
2. [Frontend](4_Teste_API/frontend/): Siga os comandos para executar o frontend da aplicação
