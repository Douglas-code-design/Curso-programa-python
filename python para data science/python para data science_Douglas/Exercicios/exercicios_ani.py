import pandas as pd

dados_pets ={
'NomePet': ['Floco', 'Rex', 'Mia', 'Thor', 'Bolinha', 'Luna'],
'Especie': ['Cachorro', 'Cachorro', 'Gato', 'Cachorro', 'Gato', 'Cachorro'],
'Idade': [3, 8, 2, 12, 5, 1],
'Peso_kg': [15, 25, 4, 30, 6, 8],
'Vacinado': [True, True, False, True, True, False]

}

df_pets = pd.DataFrame(dados_pets)
print("--- Clínica Veterinária ---")
print(df_pets)


# Agora, passamos essa "peneira" (condicao) para o DataFrame
pets_gatos = df_pets[df_pets['Especie'] == 'Gato']
print(pets_gatos)
# (Você pode fazer isso em uma linha: df_vendas[df_vendas['valor_venda'] > 7.0])


pets_pesados = df_pets[df_pets ['Peso_kg'] > 20 ]

print(pets_pesados)


pets_pesados = df_pets[(df_pets ['Idade']  > 7) &   (df_pets['Especie']  == 'Cachorro')]
print(pets_pesados)