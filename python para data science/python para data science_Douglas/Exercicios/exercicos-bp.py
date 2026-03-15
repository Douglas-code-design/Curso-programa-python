# # exercico 1

# import pandas as pd

# notas = pd.DataFrame([10.0 , 5.4, 3.5])



# print(f"A nota MÉDIA da turma é: {notas}").mean()

# media = nota_geral/3
# print(f"f"A media aritimetica é: {media}")


# --- Início do Código da Aula 3 ---
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# # Vamos usar um novo conjunto de dados, mais adequado para relações
# dados_investimento = pd.DataFrame({
# 'anos_de_experiencia': [1, 2, 3, 4, 5, 8, 10, 12, 15, 20],
# 'salario_anual_milhar': [45, 50, 60, 65, 70, 90, 100, 110, 120, 150]
# })

# plt.figure(figsize=(10, 6)) # Define o tamanho da figura
# sns.histplot(dados_investimento['salario_anual_milhar'], kde=True) # kde=True desenha uma linha de densidade
# plt.title('Distribuição dos Salários Anuais')
# plt.xlabel('Salário Anual (em milhares de R$)')
# plt.ylabel('Frequência (Contagem)')
# plt.show() # Exibe o gráfico

import pandas as pd
# Dados de preços de imóveis em um bairro (em milhares de R$)
# Note a mansão de R$ 8 milhões que é um outlier.
dados_imoveis = pd.DataFrame({
'tipo': ['Apartamento', 'Casa', 'Apartamento', 'Casa', 'Studio', 'Casa', 'Mansao'],
'preco_milhar': [300, 450, 350, 400, 250, 500, 8000]
})

print("\n--- Preços dos Imóveis no Bairro (em milhares de R$) ---")
print(dados_imoveis)
# 1. Calcule a média dos preços.
# print(f"Média de preços: R$ {dados_imoveis['preco_milhar'].mean():.2f}")
#2. Calcule a mediana dos preços.
print(f"Mediana de precos: R$ {dados_imoveis['preco_milhar'].median():.2f}")
#  3. Responda à pergunta do cenário.
print("A Mediana esta mais atrativa")
