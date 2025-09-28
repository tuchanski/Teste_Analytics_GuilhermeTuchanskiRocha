-- Consulta SQL para identificar os produtos que venderam menos no mês de junho de 2023.
-- Na requisição do teste técnico está escrito junho/2024, mas todo o contexto do teste é 2023.
-- Portanto, considerei junho de 2023. Mas se for 2024, basta alterar a data no filtro WHERE.
-- Limitei a 5 resultados para facilitar a visualização.

USE Loja;

SELECT Produto, Categoria, SUM(Quantidade * `Preço`) AS Total_Vendas_Junho
FROM Loja.Vendas
WHERE `Data` >= '2023-06-01' AND `Data` < '2023-07-01'
GROUP BY Produto, Categoria
ORDER BY Total_Vendas_Junho ASC
LIMIT 5;