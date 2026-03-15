import pandas as pd
# Criamos nossos dados de vendas diretamente em um DataFrame.
# Esta é a nossa fonte de dados para esta aula.
df_vendas = pd.DataFrame({
'produto': ['Café', 'Açúcar', 'Leite', 'Pão', 'Manteiga', 'Café', 'Leite', 'Pão', 'Açúcar', 'Café'],
'valor_venda': [5.50, 4.20, 8.00, 6.50, 12.00, 5.50, 8.50, 7.00, 4.00, 6.00],
'comissao_vendedor': [0.55, 0.42, 0.80, 0.65, 1.20, 0.55, 0.85, 0.70, 0.40, 0.60]
})
print("--- Nossos Dados de Vendas ---")
print(df_vendas)
print( "\n" +"-"*50+"\n")

print("--- Passo 1: A Pergunta (Série Booleana) ---")
# Pergunta: Quais linhas têm 'valor_venda' maior que 7.0?
condicao = df_vendas['valor_venda'] > 7.0
print(condicao)

print("\n--- Passo 2: A Peneira (Aplicando o Filtro) ---")
# Agora, passamos essa "peneira" (condicao) para o DataFrame
vendas_altas = df_vendas[condicao]
print(vendas_altas)
# (Você pode fazer isso em uma linha: df_vendas[df_vendas['valor_venda'] > 7.0])

# --- Filtro de Texto (Igualdade) ---
print("\n--- Filtro 2: Apenas Vendas de 'Café' ---")
# Pergunta: Quais linhas têm o produto IGUAL a 'Café'?
filtro_cafe = df_vendas['produto'] == 'Café'
print(df_vendas[filtro_cafe])

# --- Filtro Composto ( & = "E") ---
# Pergunta: Quais vendas foram de 'Leite' E tiveram valor acima de 8.0?
print("\n--- Filtro 3: 'Leite' E valor > 8.0 ---")
condicao1 = df_vendas['produto'] == 'Leite'
condicao2 = df_vendas['valor_venda'] > 8.0
# (Note os parênteses obrigatórios ao redor de cada condição!)
vendas_leite_caro = df_vendas[condicao1 & condicao2]
print(vendas_leite_caro)
# --- Filtro Composto ( | = "OU") ---
# Pergunta: Quais vendas foram de 'Manteiga' OU 'Pão'?
print("\n--- Filtro 4: 'Manteiga' OU 'Pão' ---")
condicao_pao = df_vendas['produto'] == 'Pão'
condicao_manteiga = df_vendas['produto'] == 'Manteiga'
vendas_padaria = df_vendas[condicao_pao | condicao_manteiga]
print(vendas_padaria)

echo "# Curso-programa-o-em-python" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Douglas-code-design/Curso-programa-o-em-python.git
git push -u origin main