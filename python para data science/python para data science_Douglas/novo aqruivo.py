import pandas as pd
# 1. Criar os dados (Como na Aula 3)
dados_vendas = {
'Data': ['2025-01-05', '2025-01-05', '2025-01-06', '2025-01-06', '2025-01-07', '2025-01-07'],
'Vendedor': ['Ana', 'Bruno', 'Ana', 'Carla', 'Bruno', 'Carla'],
'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Notebook', 'Mouse'],
'Categoria': ['Eletrônicos', 'Acessórios', 'Acessórios', 'Eletrônicos', 'Eletrônicos', 'Acessórios'],
'Quantidade': [1, 5, 2, 1, 2, 3],
'Preco_Unitario': [3500, 80, 150, 1200, 3500, 80]
}
# 2. Criar o DataFrame
df = pd.DataFrame(dados_vendas)
print("--- DataFrame Original ---")
print(df)
print("\n")


nome_arquivo = 'relatorio_vendas.xlsx'
df.to_excel(nome_arquivo, index=False, sheet_name='Vendas_Jan')
print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")