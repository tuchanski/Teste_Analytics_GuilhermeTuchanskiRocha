-- Consulta SQL para calcular o total de vendas por produto e categoria
-- Ordenado pelo total de vendas em ordem decrescente
-- Partindo do princípio que utilizamos o banco de dados Loja e a tabela Vendas.

USE Loja;

SELECT Produto, Categoria, SUM(Quantidade * `Preço`) AS Total_Vendas
FROM Loja.Vendas
GROUP BY Produto, Categoria
ORDER BY Total_Vendas DESC;