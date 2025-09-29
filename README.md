# 📊 Teste_Analytics_GuilhermeTuchanskiRocha

Este repositório contém a solução para o Teste de Estagiário de Analytics da Quod.
O objetivo foi criar um conjunto fictício de dados sujo, tratá-lo e realizar uma série de análises utilizando ferramentas de ciência de dados.

A linguagem escolhida para o desafio foi Python, devido à experiência prévia em projetos pessoais e acadêmicos com Pandas, Matplotlib e Numpy.

---

## 📂 Estrutura do Repositório

```
├── dataset/
│   ├── clean/
│   │   └── data_clean.csv         # Dataset simulado (limpo)
│   └── dirty/
│       └── data_dirty.csv         # Dataset simulado original (sujo)
├── src/
│   ├── analysis/
│   │   ├── pt1-analysis.py        # Script de análise e visualização dos dados
│   │   └── plots/
│   │       └── monthly_sales_amount.png # Gráfico de tendência mensal de vendas
│   └── app/
│       ├── main.py                # Script de limpeza do dataset
│       └── models/
│           └── dataset_generator.py # Simulação do dataset de vendas sujo
├── sql/
│   ├── consultas_sql.sql          # Consultas SQL solicitadas no teste
│   └── README.md                  # Explicação das consultas SQL
├── insights/
│   └── relatorio_insights.pdf     # Relatório com principais insights e recomendações
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Como Executar os Scripts

> ℹ️ As análises utilizam o dataset limpo (data_clean.csv), obtido a partir do arquivo original dataset/dirty/data_dirty.csv.
> Como o script `dataset_generator.py` gera um conjunto de dados novo, ao ser executado novamente produzirá resultados diferentes, e o estudo disponibilizado não se aplicará ao novo dataset.

1. **Instalar as dependências**

   ```powershell
   pip install -r requirements.txt
   ```

2. **Simular os dados**

   ```powershell
   python src/app/models/dataset_generator.py
   ```

3. **Limpar os dados**

   ```powershell
   python src/app/main.py
   ```

   O dataset limpo será salvo em `dataset/clean/data_clean.csv`.

4. **Analisar e visualizar os dados**

   ```powershell
   python src/analysis/pt1-analysis.py
   ```

   O gráfico será salvo em `src/analysis/plots/`.

5. **Executar as consultas SQL**

   As queries estão disponíveis em `sql/consultas_sql.sql`.  
   É importante que, nesse contexto, haja um banco de dados real com os dados do `data_clean.csv`.

6. **Consultar o Relatório de Insights**

   O relatório final está em `insights/relatorio_insights.pdf`.

---

## 📦 Dependências

- Python
- pandas
- matplotlib
- numpy
- python-dotenv

---

## 📑 Observações e Suposições

- O dataset de vendas foi simulado conforme solicitado, abrangendo o período de **01/01/2023 a 31/12/2023**, com pelo menos 50 registros e as colunas especificadas.
- Os nomes das colunas foram mantidos conforme solicitado no teste. Em um projeto real, aplicaria padronização para maior consistência.
- Valores faltantes e duplicados foram tratados conforme as instruções.
- As análises e visualizações consideram o dataset **limpo**.
- As consultas SQL assumem que os dados estejam estruturados de acordo com `data_clean.csv`.
- O relatório de insights foi elaborado com base nos resultados das análises e consultas.

---

## 🧑‍💻 Autor

- Guilherme Tuchanski Rocha
- [LinkedIn](https://www.linkedin.com/in/tuchanski)
