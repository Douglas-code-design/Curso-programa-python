import pandas as pd



dados_alunos = {
'Matricula': [101, 102, 103, 104, 105, 106],
'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Elisa', 'Fábio'],
'Nota_Final': [8.5, 6.0, 9.5, 4.0, 7.0, 5.5],
'Faltas': [2, 5, 0, 10, 1, 3]
}



df_alunos = pd.DataFrame(dados_alunos)
print("\n--- Desempenho Acadêmico ---")
print(df_alunos)


aprovados = df_alunos[df_alunos['Nota_Final'] >= 7]
print(aprovados)


reprovados_falta = df_alunos[df_alunos['Faltas'] > 5]
print(reprovados_falta)