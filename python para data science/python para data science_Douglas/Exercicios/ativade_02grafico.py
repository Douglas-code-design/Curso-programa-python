import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import openpyxl


#Etapa 1

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
#etapa 2
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


#Etapa 3
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
gb_Alunos_cidade = df_edutech.groupby('Cidade')['Preco'].sum().reset_index(name="Total")
print("--- Agrupamento por Cidade ---")
print(gb_cidade)
print("\n")

# --- Filtro ---

# Contagem de alunos
print("--- Contagem de Alunos ---")
qtd_alunos = df_edutech["Nome"].nunique()
print(f"Alunos Ativos: {qtd_alunos}")
print("\n")

# Curso
print("--- Contagem de Cursos ---")
qtd_curso = df_edutech["Curso"].nunique()
print(f"Cursos Ativos: {qtd_curso}")
print("\n")

# Categoria
print("--- Contagem de Categorias ---")
qtd_categoria = df_edutech["Categoria"].nunique()
print(f"Categorias Ativas: {qtd_categoria}")
print("\n")

# Cidade
print("--- Contagem de Cidades ---")
qtd_cidade = df_edutech["Cidade"].nunique()
print(f"Cidades Ativas: {qtd_cidade}")
print("\n")

# Gráficos

#1 Barra
#Grafico 1

plt.figure(figsize=(10, 6))
sns.barplot(data=gb_curso, x='Curso', y='Total', palette='viridis')
plt.title('Faturamento Total por Curso', fontsize=14, fontweight='bold')
plt.ylabel('Receita (R$)')
plt.xlabel('Cursos')
plt.show()
print("\n")

#Area Grafico 2

plt.figure(figsize=(10, 5))
plt.plot(gb_aluno['Nome'], gb_aluno['Total'], marker='o', color='darkorange', linewidth=2)
plt.title('Investimento Total por Aluno', fontsize=14, fontweight='bold')
plt.ylabel('Total Pago (R$)')
plt.grid(True, alpha=0.3)
plt.show()
plt.show()
print("\n")

plt.figure(figsize=(10, 5))
plt.plot(tabela_cursos['Curso'], tabela_cursos['Preco'], marker='o', linestyle='-', color='b')
plt.title('Comparativo de Preço Unitário por Curso', fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.6)
plt.ylabel('Preço (R$)')
plt.show()
print("\n")

#3 Pizza
labels = gb_categoria['Categoria']
sizes = gb_categoria['Total']
explode = (0.1, 0) # Destaca a primeira categoria (Programação)
colors = sns.color_palette('viridis')[0:2]
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)

plt.title('Participação no Faturamento por Categoria', fontsize=15, fontweight='bold')
plt.axis('equal')
plt.show()
print("\n")


#4 Área

plt.figure(figsize=(10, 5))
plt.fill_between(gb_cidade['Cidade'], gb_cidade['Total'], color="skyblue", alpha=0.4)
plt.plot(gb_cidade['Cidade'], gb_cidade['Total'], color="Slateblue", alpha=0.6, linewidth=2)
plt.title('Distribuição de Faturamento por Cidade', fontsize=14, fontweight='bold')
plt.ylabel('Total Acumulado (R$)')
plt.show()
print("\n")


#5 Dispersão

plt.figure(figsize=(10, 6))
sns.boxplot(data=df_edutech, x='Categoria', y='Preco', palette='viridis')
plt.title('Dispersão de Preços por Categoria', fontsize=14, fontweight='bold')
plt.xlabel('Categoria do Curso')
plt.ylabel('Preço Unitário (R$)')
plt.grid(axis='y', alpha=0.3)
plt.show()
print("\n")

# Nome do arquivo de saída
nome_arquivo = 'Relatorio_EduTech.xlsx'

# Criando o escritor do Excel
with pd.ExcelWriter(nome_arquivo, engine='openpyxl') as writer:
    # 1. Exporta o DataFrame principal (Base completa)
    df_edutech.to_excel(writer, sheet_name='Base_Completa', index=False)

    # 2. Exporta os agrupamentos para abas separadas
    gb_aluno.to_excel(writer, sheet_name='Faturamento_Alunos', index=False)
    gb_curso.to_excel(writer, sheet_name='Faturamento_Cursos', index=False)
    gb_categoria.to_excel(writer, sheet_name='Faturamento_Categorias', index=False)
    gb_cidade.to_excel(writer, sheet_name='Faturamento_Cidades', index=False)

    # 3. Criando uma aba de resumo rápido (KPIs)
    faturamento_total = df_edutech['Preco'].sum()
    resumo_kpis = pd.DataFrame({
        'Métrica': ['Alunos Ativos', 'Cursos Ativos', 'Categorias Ativas', 'Cidades Ativas', 'Faturamento Total'],
        'Valor': [qtd_alunos, qtd_curso, qtd_categoria, qtd_cidade, faturamento_total]
    })
    resumo_kpis.to_excel(writer, sheet_name='Resumo_Executivo', index=False)

print(f"✅ Relatório '{nome_arquivo}' gerado com sucesso!")
