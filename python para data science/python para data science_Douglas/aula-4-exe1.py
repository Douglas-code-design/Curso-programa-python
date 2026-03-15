import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# --- Início do Código da Aula ---
dados_investimento = pd.DataFrame({
'anos_de_experiencia': [1, 2, 3, 4, 5, 8, 10, 12, 15, 20],
'salario_anual_milhar': [45, 50, 60, 65, 70, 90, 100, 110, 120, 150]
})


# --- NOVO: Definindo o estilo GERAL ---

# Isso mudará a aparência de todos os gráficos seguintes
sns.set_theme(style="darkgri", palette="mako")


# 'palette' muda a sequência de cores padrão


# --- Código da Aula para o gráfico de dispersão ---
plt.figure(figsize=(10,6))
sns.scatterplot(x='anos_de_experiencia', y='salario_anual_milhar', data=dados_investimento, s=100)
plt.title('Relação entre Experiência e Salário (Estilo "whitegrid")')
plt.xlabel('Anos de Experiência')
plt.ylabel('Salário Anual (em milhares de R$)')
# plt.grid(True) # Não é mais necessário, o estilo "whitegrid" já inclui a grade
plt.show()