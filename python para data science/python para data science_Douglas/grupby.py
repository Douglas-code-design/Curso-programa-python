# Criamos nossos dados de vendas diretamente em um DataFrame.
# Esta é a nossa fonte de dados para esta aula.
df_vendas = pd.DataFrame({
'produto': ['Café', 'Açúcar', 'Leite', 'Pão', 'Manteiga', 'Café', 'Leite', 'Pão', 'Açúcar', 'Café'],
'valor_venda': [5.50, 4.20, 8.00, 6.50, 12.00, 5.50, 8.50, 7.00, 4.00, 6.00],
'comissao_vendedor': [0.55, 0.42, 0.80, 0.65, 1.20, 0.55, 0.85, 0.70, 0.40, 0.60]
})
print("--- Nossos Dados de Vendas ---")
print(df_vendas)
print("\n" + "-"*50 + "\n")
 # --- Pergunta 1: Qual o TOTAL vendido de CADA PRODUTO? ---

#  1. Agrupar por 'produto'

# 2. Selecionar a coluna 'valor_venda'

# 3. Aplicar a função .sum()

print("--- Total de Vendas (R$) por Produto ---")
total_por_produto = df_vendas.groupby('produto')['valor_venda'].sum()
print(total_por_produto)