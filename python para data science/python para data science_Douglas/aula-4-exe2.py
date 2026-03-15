import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Início do Código da Aula ---
dados_investimento = pd.DataFrame({
'anos_de_experiencia': [1, 2, 3, 4, 5, 8, 10, 12, 15, 20],
'salario_anual_milhar': [45, 50, 60, 65, 70, 90, 100, 110, 120, 150]
})


# Definindo um tema base
sns.set_theme(style="darkgrid")


# --- Código da Aula para o gráfico de regressão
plt.figure(figsize=(10,6))



# --- Customização DENTRO do regplot ---
sns.regplot(
x='anos_de_experiencia',
y='salario_anual_milhar',
data=dados_investimento,


# Estiliza os pontos (scatter)
scatter_kws={
's': 0.9, # Tamanho do ponto (s=100)
'color': 'darkblue', # Cor dos pontos
'marker': 'X', # Formato do marcador
'edgecolor': 'white' # Cor da borda do marcador
},


# Estiliza a linha de regressão
line_kws={
'color': 'red', # Cor da linha
'linewidth': 6 # Espessura da linha
}
)


# --- Customização FINA com Matplotlib ---
plt.title('Linha de Regressão (Estilo Avançado)', fontsize=20, fontweight='bold', color_palet;'green')
plt.xlabel('Anos de Experiência no Mercado', fontsize=14)
plt.ylabel('Expectativa Salarial (em R$ mil)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.9) # Deixa a grade tracejada e semitransparente
plt.show()