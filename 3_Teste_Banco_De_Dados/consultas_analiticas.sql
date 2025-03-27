-- Consultas analíticas

-- 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU 
-- AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre 
SELECT o.razao_social, SUM(d.vl_saldo_final - d.vl_saldo_inicial) AS despesas_trimestre
FROM demonstracoes_contabeis d
JOIN operadoras o ON d.reg_ans = o.registro_ans
WHERE d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
AND d.data >= '2024-10-01'
GROUP BY o.razao_social
ORDER BY despesas_trimestre DESC
LIMIT 10;


-- 10 operadoras com maiores despesas nessa categoria no último ano (2024)
SELECT o.razao_social, SUM(d.vl_saldo_final - d.vl_saldo_inicial) AS despesas_trimestre
FROM demonstracoes_contabeis d
JOIN operadoras o ON d.reg_ans = o.registro_ans
WHERE d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
AND d.data >= '2024-01-01'
GROUP BY o.razao_social
ORDER BY despesas_trimestre DESC
LIMIT 10;