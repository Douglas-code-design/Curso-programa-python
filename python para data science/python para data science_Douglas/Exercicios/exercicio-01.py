import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Dados para Pessoa A (Marketing)
dados_marketing = pd.DataFrame({
'investimento_ads_dia': [10, 15, 20, 22, 25, 30, 33, 35, 40, 41, 45, 50, 55, 60, 62],
'visitantes_unicos': [1100, 1200, 1500, 1600, 1550, 1800, 1900, 2000, 2200, 2150, 2400, 2800, 3100, 3500, 3400]
})

invest_med = dados_marketing['investimento_ads_dia'].mean()


invest_median = dados_marketing['visitantes_unicos'].median()

visitas_med = dados_marketing['investimento_ads_dia'].mean()

visitas_median = dados_marketing['visitantes_unicos'].median()



# Ele usará a paleta "deep" que definimos globalmente.
sns.barplot(
data=dados_marketing,
x='investimento_ads_dia', # As categorias no eixo X
y='visitantes_unicos' # Os valores (altura das colunas) no eixo Y
)

sns.set_theme(style="darkgrid", palette="viridis")
plt.title('Linha de Regressão (Estilo Avançado)', fontsize=20, fontweight='bold')
plt.xlabel('investimento', fontsize=14)
plt.ylabel('visitantes', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5) # Deixa a grade tracejada e semitransparente
sns.histplot('dados_marketing', kde=True) # kde=True desenha uma linha de densidade
plt.title('Dados Marketing')
plt.xlabel('media(investimentos_do_dia)')
plt.ylabel('Frequência (visitantse_unicos)')
plt.show() # Exibe o gráfico

