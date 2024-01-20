from random import choice
while True:
    print("JOGO DOS PAÌSES")
    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "K", "W", "X", "Y", "Z"]
    pontos = 0
    op = choice(letras)
    print("Letra escolhida:")
    print(op)
    pais = input("Pais-")
    cidade = input("Cidade-")
    comida = input("Comida-")
    marca = input("Marca-")
    jogosdecomputador = input("Jogos de computador-")

    if pais[0].lower() == op.lower():
        pontos = pontos + 1
    else:
        pontos = pontos + 0

    if comida[0].lower() == op.lower():
        pontos = pontos + 1
    else:
        pontos = pontos + 0

    if cidade[0].lower() == op.lower():
        pontos = pontos + 1
    else:
        pontos = pontos + 0

    if marca[0].lower() == op.lower():
        pontos = pontos + 1
    else:
        pontos = pontos + 0

    if jogosdecomputador[0].lower() == op.lower():
        pontos = pontos + 1
    else:
        pontos = pontos + 0

    print(f"Pontuacão:\n{pontos}")
    jogaroutravez = input("Tentar de novo:\n"
          "pressione y para jogar de novo e n para saír >")
    if jogaroutravez == "y":
        continue

    elif jogaroutravez == "n":
        break

    else:
        print("Letra incorrefta")
        jogaroutravez = input("\nTentar de novo:\n"
                             "pressione y para jogar de novo e n para saír >")