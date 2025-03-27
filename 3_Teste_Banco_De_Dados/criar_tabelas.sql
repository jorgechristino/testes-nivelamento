-- Criar tabelas para armazenar os dados do CSV (PostgreSQL)

CREATE TABLE operadoras (
    id  SERIAL PRIMARY KEY,
    registro_ans VARCHAR(6) UNIQUE NOT NULL,
    cnpj VARCHAR(14) NOT NULL,
    razao_social VARCHAR(140) NOT NULL,
    nome_fantasia VARCHAR(140),
    modalidade VARCHAR(40),
    logradouro VARCHAR(40),
    numero VARCHAR(20),
    complemento VARCHAR(40),
    bairro VARCHAR(30),
    cidade VARCHAR(30),
    uf VARCHAR(2),
    cep VARCHAR(8),
    ddd VARCHAR(4),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(50),
    cargo_representante VARCHAR(40),
    regiao_de_comercializacao SMALLINT,
    data_registro_ans DATE
);

CREATE TABLE demonstracoes_contabeis (
    id  SERIAL PRIMARY KEY,
    data DATE,
    reg_ans VARCHAR(6) NOT NULL,
    cd_conta_contabil BIGINT NOT NULL,
    descricao VARCHAR(150),
    vl_saldo_inicial DOUBLE PRECISION,
    vl_saldo_final DOUBLE PRECISION
);