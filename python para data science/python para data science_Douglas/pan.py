import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Vamos usar um novo conjunto de dados, mais adequado para relações
dados_investimento = pd.DataFrame({
'anos_de_experiencia': [1, 2, 3, 4, 5, 8, 10, 12, 15, 20],
'salario_anual_milhar': [45, 50, 60, 65, 70, 90, 100, 110, 120, 150]
})

plt.figure(figsize=(5, 6)) # Define o tamanho da figura
sns.histplot(dados_investimento['salario_anual_milhar'], kde=True) # kde=True desenha uma linha de densidade
plt.title('Distribuição dos Salários Anuais')
plt.xlabel('Salário Anual (em milhares de R$)')
plt.ylabel('Frequência (Contagem)', fontsize=12, color="red", labelpad=10)

plt.show() # Exibe o gráfico
