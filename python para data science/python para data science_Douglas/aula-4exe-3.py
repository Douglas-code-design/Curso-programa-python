import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# --- Início do Código da Aula ---
dados_investimento = pd.DataFrame({
'anos_de_experiencia': [1, 2, 3, 4, 5, 8, 10, 12, 15, 20],
'salario_anual_milhar': [45, 50, 60, 65, 70, 90, 100, 110, 120, 150]
})

# DADO 1: Para o Gráfico de Linha.
dados_investimento = pd.DataFrame({
'anos_de_experiencia': [1, 2, 3, 4, 5, 8, 10, 12, 15, 20],
'salario_anual_milhar': [45, 50, 60, 65, 70, 90, 100, 110, 120, 150]
})
# DADO 2: Para o Gráfico de Colunas (Comparação entre categorias).
dados_departamento = pd.DataFrame({
'departamento': ['TI', 'Recursos Humanos', 'Vendas', 'Marketing'],
'funcionarios': [80, 35, 120, 50]
})
# DADO 3: Para o Gráfico de Pizza (Proporções de um todo).
dados_portfolio = {
'tipo_investimento': ['Ações', 'Renda Fixa', 'Imóveis', 'Caixa'],
'valor_percentual': [45, 25, 20, 10]
}
print("Todos os conjuntos de dados foram criados.")
print("---")







# ==============================================================================
# --- GRÁFICO 1: GRÁFICO DE LINHA (Tendência Sequencial) ---
# Objetivo: Mostrar a progressão dos dados como uma sequência.
# # ==============================================================================
# print("Exibindo Gráfico 4: Linha...")
# # 1. Cria uma nova tela.
# plt.figure(figsize=(10, 6))
# # 2. Desenha o gráfico de linha.
# sns.lineplot(
# data=dados_investimento,
# x='anos_de_experiencia',
# y='salario_anual_milhar',
# marker='o', # Adiciona um marcador de "bolinha" em cada ponto
# linewidth=2.5 # Aumenta a espessura da linha
# )
# # 3. Adiciona títulos e rótulos.
# plt.title('Progressão Salarial por Experiência', fontsize=16, fontweight='bold')
# plt.xlabel('Anos de Experiência', fontsize=12)
# plt.ylabel('Salário Anual (em R$ mil)', fontsize=12)
# # 4. Exibe o gráfico.
# plt.show()


# ==============================================================================
# --- GRÁFICO 2: GRÁFICO DE COLUNAS (Comparação de Categorias) ---
# Objetivo: Comparar valores numéricos entre categorias distintas.
# # ==============================================================================
# print("Exibindo Gráfico 5: Colunas (Bar Chart)...")
# # 1. Cria uma nova tela.
# plt.figure(figsize=(10, 6))
# # 2. Desenha o gráfico de colunas (ou barras).
# # Ele usará a paleta "deep" que definimos globalmente.
# sns.barplot(
# data=dados_departamento,
# x='departamento', # As categorias no eixo X
# y='funcionarios' # Os valores (altura das colunas) no eixo Y
# )
# # 3. Adiciona títulos e rótulos.
# plt.title('Número de Funcionários por Departamento', fontsize=16, fontweight='bold')
# plt.xlabel('Departamento', fontsize=12)
# plt.ylabel('Total de Funcionários', fontsize=12)
# # 4. Exibe o gráfico.
# plt.show()

# # ==============================================================================
# # --- GRÁFICO 3: GRÁFICO DE PIZZA (Proporções de um Todo) ---
# # Objetivo: Mostrar como um valor total é dividido em partes.
# # Nota: Seaborn não tem .pie(), por isso usamos o Matplotlib (plt) diretamente.
# # ==============================================================================
print("Exibindo Gráfico 6: Pizza (Pie Chart)...")
# 1. Prepara os dados para o plt.pie() (ele prefere listas)
labels = dados_portfolio['tipo_investimento']
sizes = dados_portfolio['valor_percentual']
# 2. Pega 4 cores da nossa paleta "deep" do Seaborn para manter a consistência
colors = sns.color_palette('deep')[0:4]
# 3. "Explode" (destaca) a primeira fatia (Ações)
explode = (0, 0, 0, 0)
# 4. Cria a tela (quadrada é melhor para pizza)
plt.figure(figsize=(8, 8))
# 5. Desenha o gráfico de pizza.
plt.pie(
sizes, # Os valores (tamanho de cada fatia)
explode=explode, # O quanto cada fatia "sai" do centro
labels=labels, # Os rótulos de cada fatia
colors=colors, # As cores que pegamos do Seaborn
autopct='%1.1f%%', # Formato para exibir a porcentagem (ex: "45.0%")
shadow=True, # Adiciona uma sombra
startangle=90 # Gira o gráfico para começar a primeira fatia no topo
)
# 6. Adiciona o título.
plt.title('Composição da Carteira de Investimentos', fontsize=16, fontweight='bold')
# 7. Garante que o gráfico seja um círculo perfeito.
plt.axis('equal')
# 8. Exibe o gráfico.
plt.show()