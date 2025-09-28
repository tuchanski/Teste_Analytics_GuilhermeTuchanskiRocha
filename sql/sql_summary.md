# 📊 Consultas SQL

```sql
USE Loja;
```

## 1) Total de Vendas por Produto em Ordem Decrescente
Consulta:

```sql
SELECT Produto, Categoria, SUM(Quantidade * `Preço`) AS Total_Vendas
FROM Vendas
GROUP BY Produto, Categoria
ORDER BY Total_Vendas DESC;
```

Resultado:

| Produto                 | Categoria    | Total_Vendas   |
|-------------------------|--------------|----------------|
| NOTEBOOK                | ELETRONICOS  | R$ 445.500,00  |
| COMPUTADOR GAMER        | ELETRONICOS  | R$ 231.000,00  |
| GEFORCE RTX 2070        | ELETRONICOS  | R$ 128.800,00  |
| HEADSET LOGITECH        | ACESSORIOS   | R$ 18.050,00   |
| LASANHA CONGELADA 500G  | ALIMENTOS    | R$ 1.530,00    |
| CAFE PELE 500G          | ALIMENTOS    | R$ 1.470,00    |
| PINHAO 1KG              | ALIMENTOS    | R$ 925,00      |
| SUCRILHOS               | ALIMENTOS    | R$ 312,00      |

---

## 2) Produtos que venderam menos em Junho/2023
Consulta:

```sql
SELECT Produto, Categoria, SUM(Quantidade * `Preço`) AS Total_Vendas_Junho
FROM Vendas
WHERE `Data` >= '2023-06-01' AND `Data` < '2023-07-01'
GROUP BY Produto, Categoria
ORDER BY Total_Vendas_Junho ASC
```

Resultado:

| Produto                 | Categoria    | Total_Vendas_Junho |
|-------------------------|--------------|--------------------|
| CAFE PELE 500G          | ALIMENTOS    | R$ 195,00          |
| LASANHA CONGELADA 500G  | ALIMENTOS    | R$ 720,00          |
| HEADSET LOGITECH        | ACESSORIOS   | R$ 3.420,00        |
| GEFORCE RTX 2070        | ELETRONICOS  | R$ 36.800,00       |
