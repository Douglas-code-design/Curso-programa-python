# .sdt()"desvio padrão"

# .mean()" média"
# import pandas as pd

# # Dados de comprimento (em mm) de parafusos produzidos por duas máquinas.
# # O alvo é 50mm.
# dados_maquinas = pd.DataFrame({
# 'maquina_A': [50.1, 50.0, 49.9, 50.0, 49.8, 50.2, 50.0, 50.1, 49.9, 50.0],
# 'maquina_B': [52.5, 47.0, 50.0, 51.5, 48.0, 46.5, 53.0, 50.5, 49.0, 52.0]
# })
# print("--- Medidas dos Parafusos (em mm) ---")
# print(dados_maquinas)
# # Tarefa 1: Calcule a média de produção de cada máquina.
# media_originalMA = dados_maquinas['maquina_A'].mean()
# media_originalMB = dados_maquinas['maquina_B'].mean()
# # Tarefa 2: Calcule o desvio padrão de cada máquina.
# std_originalMA = dados_maquinas['maquina_A'].std()
# std_originalMB = dados_maquinas['maquina_B'].std()


# print(f"--- Máquina A ---")
# print(f"Média: {media_originalMA:.2f}")
# print(f"Desvio Padrão: {std_originalMA:.2f}")
# print("\n")
# print(f"--- Máquina B ---")
# print(f"Média: {media_originalMB:.2f}")
# print(f"Desvio Padrão: {std_originalMB:.2f}")


# Criar uma tabela (DataFrame) com notas e faltas de alunos.
import pandas as pd

# dados_notas = pd.DataFrame({
# 'aluno': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Elisa', 'Fábio', 'Gabi', 'Hugo', 'Inês', 'João'],
# 'nota_final': [8.5, 7.0, 9.0, 5.5, 10.0, 7.0, 6.5, 8.0, 9.5, 4.0],
# })
# media_alunos = dados_notas['nota_final'].mean()
# print(f"A nota MÉDIA da turma é: {media_alunos:.2f}")

# media_alunos = dados_notas['nota_final'].median()
# print(f" A nota mediana da turma é: {media_alunos:.2f}")


# moda_notas = dados_notas['nota_final'].mode()[0]
# print(f"A nota mais comum (MODA) foi: {moda_notas:.2f}")

salarios = pd.DataFrame({'funcionario': ['Zeca', 'Maria', 'Pedro', 'Bia'], 'salario': [2000, 2500, 2200, 3000]})

print("\n--- Salários da Equipe (Situação Normal) ---")
# Na situação normal, média e mediana são próximas.
print(f"Salário MÉDIO (normal): R$ {salarios['salario'].mean():.2f}")
print(f"Salário MEDIANO (normal): R$ {salarios['salario'].median():.2f}")

novo_salario = pd.DataFrame({'funcionario': ['CEO'], 'salario': [50000]})
salarios_com_outlier = pd.concat([salarios, novo_salario], ignore_index=True)


print("\n--- Salários da Equipe (com Outlier) ---")
print(f"Salário MÉDIO (com outlier): R$ {salarios_com_outlier['salario'].mean():.2f}")
print(f"Salário MEDIANO (com outlier): R$ {salarios_com_outlier['salario'].median():.2f}")
print("\n>>> CONCLUSÃO: A MÉDIA disparou e deixou de representar a equipe.")
print(">>> A MEDIANA permaneceu estável, provando sua robustez!")