import pandas as pd
import numpy as np

# Criando dados fictícios
data = {
    'ID_Pedido': range(101, 111),
    'Data': pd.to_datetime(['2026-01-10', '2026-01-12', '2026-01-15', '2026-02-01', 
                            '2026-02-05', '2026-02-10', '2026-03-01', '2026-03-05', 
                            '2026-03-10', '2026-03-12']),
    
    
    'Produto': ['Smartphone', 'Monitor 4K', 'Teclado Mecânico', 'Smartphone', 
                'Fone Bluetooth', 'Monitor 4K', 'Mouse Gamer', 'Smartphone', 
                'Teclado Mecânico', 'Fone Bluetooth'],
    
    
    
    'Categoria': ['Celulares', 'Hardware', 'Periféricos', 'Celulares', 
                  'Áudio', 'Hardware', 'Periféricos', 'Celulares', 
                  'Periféricos', 'Áudio'],
    
    
    'Preco_Unitario': [2500, 1800, 350, 2500, 200, 1800, 150, 2500, 350, 200],
    
    
    'Quantidade': [1, 2, 5, 1, 3, 1, 10, 2, 4, 2],
    
    
    'Regiao': ['Sudeste', 'Sul', 'Norte', 'Sudeste', 'Nordeste', 
               'Sul', 'Sudeste', 'Centro-Oeste', 'Norte', 'Sul']
}

df = pd.DataFrame(data)

# # Criando uma coluna calculada para treinar
# df['Total_Venda'] = df['Preco_Unitario'] * df['Quantidade']

# print("--- Primeiras 5 linhas do DataFrame ---")
# print(df.head())


televisao = df[df['Preco_Unitario'] == 350].reset_index(drop=True)
print("\n--- Pedidos de Smartphone ---")
print(televisao)

df_limpo = df.drop(columns=['ID_Pedido', 'Data'])
print("\n--- DataFrame Limpo ---")
print(df_limpo.head())