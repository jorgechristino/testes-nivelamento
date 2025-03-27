-- Importar os dados do CSV para a tabela (PostgreSQL)

COPY operadoras(registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, regiao_de_comercializacao, data_registro_ans)
FROM '.../3_Teste_Banco_De_Dados/downloads/Relatorio_cadop.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

COPY demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM '...\3_Teste_Banco_De_Dados\downloads\2023\1T2023.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

COPY demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM '...\3_Teste_Banco_De_Dados\downloads\2023\2t2023.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

COPY demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM '...\3_Teste_Banco_De_Dados\downloads\2024\3T2023.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

COPY demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM '...\3_Teste_Banco_De_Dados\downloads\2024\4T2023.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

COPY demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM '...\3_Teste_Banco_De_Dados\downloads\2024\1T2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

COPY demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM '...\3_Teste_Banco_De_Dados\downloads\2024\2T2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

COPY demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM '...\3_Teste_Banco_De_Dados\downloads\2024\3T2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';

COPY demonstracoes_contabeis(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM '...\3_Teste_Banco_De_Dados\downloads\2024\4T2024.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';
