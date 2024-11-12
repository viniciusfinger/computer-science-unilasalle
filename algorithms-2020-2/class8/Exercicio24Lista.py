import random


# Lançar dados 100 vezes e contar quantas vezes caiu cada número.

def jogaDado():
    return random.randint(1, 6)


def contaRepeticoes(resultados):
    vetorContagem = [0, 0, 0, 0, 0, 0]
    for resultado in resultados:
        if resultado == 1:
            vetorContagem[0] = vetorContagem[0] + 1
        if resultado == 2:
            vetorContagem[1] = vetorContagem[1] + 1
        if resultado == 3:
            vetorContagem[2] = vetorContagem[2] + 1
        if resultado == 4:
            vetorContagem[3] = vetorContagem[3] + 1
        if resultado == 5:
            vetorContagem[4] = vetorContagem[4] + 1
        if resultado == 6:
            vetorContagem[5] = vetorContagem[5] + 1
    return vetorContagem


def rodaDados():
    i = 0
    resultado = []

    while i < 100:
        resultado.append(jogaDado())
        i += 1
    return resultado


def printaResultados(resultado, quantidadeRepeticoes):
    num = 1

    print(f"Resultados: {resultado}\n")
    print(f"Repetições:")

    while num <= 6:
        print(f"Número {num}: {quantidadeRepeticoes[(num - 1)]} vezes")
        num += 1

    print(f"       = {sum(quantidadeRepeticoes)} repetições")


resultado = rodaDados()
quantidadeRepeticoes = contaRepeticoes(resultado)
printaResultados(resultado, quantidadeRepeticoes)
