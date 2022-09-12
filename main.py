# Dicionário para armazenar as informações dos lutadores
info_lutadores = {}

# Dicionário para armazenar cada lutador e sua categoria
categoria_lutadores = {}

sair = 1

while sair == 1:
    # Solicita os dados ao usuário
    lutador = input("Nome do lutador:\n")
    peso = float(input("Peso do lutador (kg):\n"))

    # Acrescenta os dados do lutador ao dicionário
    info_lutadores[lutador] = peso

    # Pergunta se o usuário deseja encerrar o cadastro
    sair = int(input("Deseja cadastrar mais um lutador?\n1-Sim\n2-Não\n"))


def descobrir_categoria(info_lutadores):
    # Percorre as entradas do dicionário
    for lutador, peso in info_lutadores.items():
        if peso >= 100:
            categoria = "Pesado"
        elif peso >= 93:
            categoria = "Meio-pesado"
        elif peso >= 86:
            categoria = "Médio"
        elif peso >= 79:
            categoria = "Meio-médio"
        elif peso >= 72:
            categoria = "Ligeiro"
        elif peso >= 65:
            categoria = "Leve"
        else:
            categoria = "Pena"

        # Acrescenta o lutador(chave) e seu peso(valor) ao dicionário
        categoria_lutadores[lutador] = categoria

    return categoria_lutadores


# Chama a função
descobrir_categoria(info_lutadores)

# Cabeçalho da tabela
print("-" * 47)
print("| {:^20} | {:^20} |".format("LUTADOR", "CATEGORIA"))
print("-" * 47)

# Percorre as entradas do dicionário com os lutadores e suas respectivas categorias
for lutador, categoria in categoria_lutadores.items():
    print("| {:<20} | {:<20} |".format(lutador, categoria))
    print('-' * 47)
