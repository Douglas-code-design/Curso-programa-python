import pandas as pd # Importamos a biblioteca pandas para manipulação de dados
# ------------------------------------------------------
# Tabela 1 - CLIENTES
# ------------------------------------------------------
# Criamos um DataFrame contendo informações dos clientes:
# ID_Cliente → identificador único
# Nome → nome do cliente
# Cidade → localidade do cliente
clientes = pd.DataFrame({
"ID_Cliente": [1, 2, 3, 4, 5],
"Nome": ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"],
"Cidade": ["SP", "RJ", "SP", "BH", "Curitiba"]
})
print("\n--- CLIENTES ---")
print(clientes) # Exibe o DataFrame de clientes

# ------------------------------------------------------
# Tabela 2 - PRODUTOS
# ------------------------------------------------------
# Informações sobre os produtos
# ID_Produto → identificador único
# Produto → nome do produto
# Categoria → tipo do produto
# Preco → valor unitário
produtos = pd.DataFrame({
"ID_Produto": [101, 102, 103, 104],
"Produto": ["Notebook", "Mouse", "Teclado", "Monitor"],
"Categoria": ["Eletrônicos", "Eletrônicos", "Eletrônicos", "Eletrônicos"],
"Preco": [3500, 80, 120, 900]
})

print("\n--- PRODUTOS ---")
print(produtos) # Exibe o DataFrame de produtos
# ------------------------------------------------------
# Tabela 3 - VENDAS
# ------------------------------------------------------
# Informações das vendas
# ID_Venda → identificador da venda
# ID_Cliente → referência ao cliente comprador
# ID_Produto → referência ao produto vendido
# Quantidade → quantidade comprada
vendas = pd.DataFrame({
"ID_Venda": [1, 2, 3, 4, 5, 6],
"ID_Cliente": [1, 3, 2, 4, 5, 1],
"ID_Produto": [101, 102, 104, 103, 101, 102],
"Quantidade": [1, 2, 1, 3, 1, 2]
})
print("\n--- VENDAS ---")
print(vendas) # Exibe o DataFrame de vendas

# Fazemos a junção (merge) das tabelas vendas + clientes
# Usando como chave a coluna ID_Cliente
df = vendas.merge(clientes, on="ID_Cliente") \
.merge(produtos, on="ID_Produto") # Depois juntamos com produtos usando ID_Produto
# Criamos uma nova coluna "Total" multiplicando quantidade * preço
df["Total"] = df["Quantidade"] * df["Preco"]
print("\n--- RELATÓRIO COMPLETO ---")
print(df) # Exibe o DataFrame resultante com todas as informações unificadas
# Agrupa por nome do cliente e soma o total gasto
# groupby → organiza os dados por cliente
# sum() → soma os valores de Total
total_por_cliente = df.groupby("Nome")["Total"].sum()
print("\n--- Total Vendido por Cliente ---")
print(total_por_cliente)
# Agrupa por nome do produto e soma o total vendido
total_por_produto = df.groupby("Produto")["Total"].sum()
print("\n--- Total Vendido por Produto ---")
print(total_por_produto)
# Agrupa pelos nomes das cidades e soma a quantidade vendida
qtd_por_cidade = df.groupby("Cidade")["Quantidade"].sum()
print("\n--- Quantidade Vendida por Cidade ---")
print(qtd_por_cidade)
# Agrupa por categoria e soma as quantidades vendidas
qtd_por_categoria = df.groupby("Categoria")["Quantidade"].sum()

print("\n--- Quantidade Vendida por Categoria ---")
print(qtd_por_categoria)
# Filtra apenas as linhas em que o Nome é "Ana"
filtro_ana = df[df["Nome"] == "Ana"]
print("\n--- Vendas de Ana ---")
print(filtro_ana)
# Salva o DataFrame completo em um arquivo Excel
# index=False → evita que o índice seja salvo como coluna
df.to_excel("vendas_completas.xlsx", index=False)
print("Arquivo criado com sucesso!")