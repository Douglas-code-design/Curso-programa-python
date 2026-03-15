import pandas as pd
import matplotlib.pyplot as plt

# --- TAREFA 1: LER O EXCEL (DA AULA ANTERIOR) ---
nome_arquivo = 'relatorio_vendas.xlsx'
nome_da_aba = 'Vendas_Jan'
print(f"Tentando ler o arquivo '{nome_arquivo}', aba '{nome_da_aba}'...")
try:
    # 1. Lendo os dados do arquivo
    df_lido = pd.read_excel(nome_arquivo, sheet_name=nome_da_aba)
    print("\n--- Dados lidos do Excel ---")
    print(df_lido)
    print("\n")
    # --- TAREFA 2: APLICAR REGRAS (
    # 2. Criar a coluna 'Total_Venda'
    df_lido['Total_Venda'] = df_lido['Quantidade'] * df_lido['Preco_Unitario']
    # 3. Agrupar os dados para os gráficos
    # Agregação 1: Total de vendas (R$) por Vendedor
    total_por_vendedor = df_lido.groupby('Vendedor')['Total_Venda'].sum()
    print("--- Dados para o Gráfico 1 (Vendas por Vendedor) ---")
    print(total_por_vendedor)
    print("\n")
    # Agregação 2: Total de itens (unidades) por Categoria
    unidades_por_categoria = df_lido.groupby('Categoria')['Quantidade'].sum()
    print("--- Dados para o Gráfico 2 (Itens por Categoria) ---")
    print(unidades_por_categoria)
    print("\n")

    # --- TAREFA 3: GERAR OS GRÁFICOS (AULA 7) ---
    print("Gerando gráficos...")
    # 1. Gráfico 1: Total de Vendas por Vendedor (Gráfico de Barras)
    total_por_vendedor.plot(
    kind='bar',
    title='Total de Vendas (R$) por Vendedor',
    rot=0 # Deixa os nomes dos vendedores na horizontal
    )
    plt.xlabel("Vendedor")
    plt.ylabel("Total Vendido (R$)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show() # Exibe o primeiro gráfico

    # 2. Gráfico 2: Proporção de Unidades por Categoria (Gráfico de Pizza)
    unidades_por_categoria.plot(
    kind='pie',
    title='Proporção de Unidades Vendidas por Categoria',
    autopct='%1.1f%%', # Adiciona o percentual
    startangle=90
    )
    plt.ylabel("") # Remove o label lateral
    plt.axis('equal') # Garante que seja um círculo
    plt.tight_layout()
    plt.show() # Exibe o segundo gráfico
except FileNotFoundError:
    print(f"\nERRO: O arquivo '{nome_arquivo}' não foi encontrado.")
    print("Por favor, verifique se o arquivo está na mesma pasta do script.")
except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")