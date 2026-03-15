import pandas as pd

import openpyxl as xl



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
# 3. Salvar o DataFrame em um arquivo Excel
# Usamos o método .to_excel()
# O argumento 'index=False' evita que o índice do Pandas (0, 1, 2...)
# seja salvo como uma coluna extra no Excel.
nome_arquivo = 'relatorio_vendas.xlsx'
df.to_excel(nome_arquivo, index=False, sheet_name='Vendas_Jan')
print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")
#'Se você olhar na pasta onde seu script Python está salvo, agora existe um arquivo chamado'
#relatorio_vendas.xlsx.

#cd para mudar o dirertorio no terminal
# arquivo_fil = df[df['preco_unitario']] 
# nome_arquivo = 'relatorio_vendas.xlsx'
# df.to_excel(nome_arquivo, index=False, sheet_name='Vendas_Jan')
# print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")

import pandas as pd
# Ler o arquivo Excel que acabamos de criar
# Usamos a função pd.read_excel()
try:
    df_lido = pd.read_excel('relatorio_vendas.xlsx', sheet_name='Vendas_Jan')
    print("--- Dados Lidos do Excel ---")
    print(df_lido) # .head() mostra apenas as primeiras 5 linhas
    print("\n")
except FileNotFoundError:
    print("Erro: O arquivo 'relatorio_vendas.xlsx' não foi encontrado.")
# Se der esse erro, execute o script da Tarefa 1 primeiro.
df_lido['Total_Venda'] = df_lido['Quantidade'] * df_lido['Preco_Unitario']

vendas_eletronicos = df_lido[df_lido['Categoria'] == 'Eletrônicos']
print(vendas_eletronicos)
print("\n")

vendas_resumidas = vendas_eletronicos.loc[:, ['Vendedor', 'Produto', 'Total_Venda']]
print(vendas_resumidas)

total_por_vendedor = df_lido.groupby('Vendedor')['Total_Venda'].sum()
print("--- Aula 5: Total de vendas (R$) por Vendedor ---")
print(total_por_vendedor)
print("\n")

# 5. Quantos itens (unidades) cada Categoria vendeu?
unidades_por_categoria = df_lido.groupby('Categoria')['Quantidade'].sum()
print("--- Aula 5: Total de itens (unidades) por Categoria ---")
print(unidades_por_categoria)
print("\n")

