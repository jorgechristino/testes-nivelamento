# Backend do Sistema

Utilizando FastAPI e SQLAlchemy foi desenvolvido uma API para um sistema de operadoras de plano de saúde, com as seguintes rotas:

- POST /operadoras : Cria uma operadora no banco de dados.
- GET /operadoras : Retorna uma lista das operadoras no banco de dados.
- GET /operadoras/:id : Retorna os dados da operadora pelo id.
- PUT /operadoras/:id : Atualiza os dados de uma operadora do banco de dados.
- DELETE /operadoras/:id : Deleta os dados de uma operadora do banco de dados.
- GET /operadoras/search?termo : Busca as operadoras mais relevantes com base no termo passado como parâmetro.

## Inicializando a aplicação

Dentro do diretório 4_Teste_API, digite os seguintes comandos:

Navegue até o diretório do backend

```sh
cd backend
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

### Configurando o bando de dados

No arquivo [configs.py](core/configs.py) altere a url do database com as informações do seu banco de dados criado previamente.

```python
DB_URL: str = "postgresql+asyncpg://user:password@localhost:5432/database_name"
```

### Executando o servidor

```sh
python main.py
```

Visualize as rotas em http://localhost:8000/docs

### Testando rotas com Postman

Importe a coleção do postman [Teste API.postman_collection](postman/Teste%20API.postman_collection.json).
