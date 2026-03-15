import pandas as pd
import matplotlib.pyplot as plt

tabela_alunos = pd.DataFrame({
'ID_Aluno': [1, 2, 3, 4, 5],
'Nome': ['Lucas','Mariana', 'Pedro', 'Juliana', 'Rafael'],
'Cidade': ['São Paulo', 'Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'Curitiba']
})

tabela_cursos = pd.DataFrame({
'ID_Curso': [201, 202, 203, 204],
'Curso': ['Python', 'Excel Avançado', 'Power BI', 'Java'],
'Categoria': ['Programação', 'Dados', 'Dados', 'Programação'],
'Preco': [800, 500, 900, 1000],
})

tabela_matriculas = pd.DataFrame({
'ID_Matricula': [1, 2, 3, 4 ,5 ,6],
'ID_Aluno': [1, 2, 3, 1 ,5 ,4],
'ID_Curso': [201, 202, 203, 202, 201, 204],
'Quantidade': [1, 1, 1, 1 ,1 ,1]
})

# --- O MERGE ---
# Vamos mesclar as duas tabelas usando a coluna 'ID_Cliente'
# Por padrão, o 'merge' faz um 'inner join' (só inclui quem está nas duas tabelas)
df_merged = pd.merge(tabela_alunos, tabela_matriculas, on='ID_Aluno')
print("--- Resultado do Merge (Inner Join) ---")
print(df_merged)

# --- O MERGE ---
# Vamos mesclar as duas tabelas usando a coluna 'ID_Cliente'
# Por padrão, o 'merge' faz um 'inner join' (só inclui quem está nas duas tabelas)
df_edutech = pd.merge(df_merged, tabela_cursos, on='ID_Curso')
print("--- Resultado do Merge (Inner Join) ---")
print(df_edutech)

# --- Agrupamento (groupby) ---
# Nome
gb_aluno = df_edutech.groupby('Nome')['Preco'].sum().reset_index(name="Total")
print("--- Agrupamento por Aluno ---")
print(gb_aluno)
print("\n")

# Curso
gb_curso = df_edutech.groupby('Curso')['Preco'].sum().reset_index(name="Total")
print("--- Agrupamento por Curso ---")
print(gb_curso)
print("\n")

# Categoria
gb_categoria = df_edutech.groupby('Categoria')['Preco'].sum().reset_index(name="Total")
print("--- Agrupamento por Categoria ---")
print(gb_categoria)
print("\n")

# Cidade

gb_cidade = df_edutech.groupby('Cidade')['Preco'].sum().reset_index(name="Total")
print("--- Agrupamento por Cidade ---")
print(gb_cidade)
print("\n")

# --- Filtro ---
# Contagem de alunos
qtd_alunos = df_edutech["Nome"].nunique()
print(f"contagem de alunos..{qtd_alunos}")
# Curso
qtd_Curso = df_edutech["Curso"].nunique()
print(f"contagem de cursos..{qtd_Curso}")

# Categoria
qtd_Categoria = df_edutech["categoria"].nunique()
print(f"contagem de categoria..{qtd_Categoria}")

# Cidade
qtd_Cidade = df_edutech["aluno"].nunique()
print(f"contagem de Cidade..{qtd_Cidade}")

#Grafico de aluos por matricula

x = [1, 2, 3, 4, 5]  # Eixo horizontal
y = [10, 20, 25, 30, 50]  # Eixo vertical

# 3. Criando o gráfico
plt.plot( df_edutech [ "categoria"], df_edutech['Curso'], marker='o')  # Gerando grafico de linha com marcadores nos pontos

# 4. Adicionando detalhes (opcional, mas recomendado)
plt.title("Categgoria x curso")
plt.xlabel("Tempo (segundos)")
plt.ylabel("Velocidade (km/h)")

# 5. Exibindo
plt.show()