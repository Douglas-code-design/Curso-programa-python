import pandas as pd
dados_estoque = {
'Produto': ['Arroz', 'Feijão', 'Óleo', 'Sal', 'Macarrão', 'Café'],
'Categoria': ['Grãos', 'Grãos', 'Mercearia', 'Mercearia', 'Massas', 'Mercearia'],
'Qtd_Estoque': [50, 15, 10, 100, 40, 5],
'Preco_Unit': [25.00, 8.00, 7.50, 3.00, 6.00, 15.00]
}
df_estoque = pd.DataFrame(dados_estoque)
print("\n--- Controle de Estoque ---")
print(df_estoque)


estoque_baixo = df_estoque [df_estoque['Qtd_Estoque'] <= 10]
print(estoque_baixo)

reposição_urgente = df_estoque [(df_estoque['Categoria' ] == 'Grãos') | (df_estoque['Categoria'] == 'Mercearia' ) ]
print(reposição_urgente)

oferta_graos = df_estoque [(df_estoque['Categoria'] == 'Grãos') & (df_estoque['Preco_Unit'] < 10.00 )] 
print(oferta_graos)
print(oferta_graos)