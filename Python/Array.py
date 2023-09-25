# Lista para armazenar os dados dos funcionários
funcionarios = []

# Loop para coletar os dados de múltiplos funcionários
while True:
    nome = input("Qual o seu nome? (ou digite 'sair' para encerrar)")
    if nome.lower() == 'sair':
        break

    produtividade = int(input("Qual a sua produtividade?"))
    classificacao = int(input("Qual a sua classificação?"))
    encerrado_outros = int(input("Quantos encerrado_outros?"))

    # Metas
    meta_produtividade = 87
    meta_classificacao = 94
    meta_encerrado_outros = 16

    # Verificar os dados para saber se o funcionário bateu a meta
    if produtividade >= meta_produtividade and classificacao >= meta_classificacao and encerrado_outros >= meta_encerrado_outros:
        resultado = f"O funcionário {nome} bateu a meta do mês."
    else:
        resultado = f"O funcionário {nome} não bateu a meta do mês."

    # Armazenar os dados em um dicionário
    funcionario = {
        "nome": nome,
        "produtividade": produtividade,
        "classificacao": classificacao,
        "encerrado_outros": encerrado_outros,
        "resultado": resultado
    }

    # Adicionar o dicionário à lista de funcionários
    funcionarios.append(funcionario)

# Imprimir os resultados
for funcionario in funcionarios:
    print(funcionario["resultado"])