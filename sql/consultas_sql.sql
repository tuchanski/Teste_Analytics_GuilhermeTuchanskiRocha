-- Partindo do princípio que utilizamos o banco de dados Loja e a tabela Vendas.

USE Loja;

-- Consulta SQL para calcular o total de vendas por produto e categoria
-- Ordenado pelo total de vendas em ordem decrescente

SELECT Produto, Categoria, SUM(Quantidade * `Preço`) AS Total_Vendas
FROM Vendas
GROUP BY Produto, Categoria
ORDER BY Total_Vendas DESC;

-- Consulta SQL para identificar os produtos que venderam menos no mês de junho de 2023.
-- Na requisição do teste técnico está escrito junho/2024, mas todo o contexto do teste é 2023.
-- Portanto, considerei junho de 2023. Mas se for 2024, basta alterar a data no filtro WHERE.

SELECT Produto, Categoria, SUM(Quantidade * `Preço`) AS Total_Vendas_Junho
FROM Vendas
WHERE `Data` >= '2023-06-01' AND `Data` < '2023-07-01'
GROUP BY Produto, Categoria
ORDER BY Total_Vendas_Junho ASC;
