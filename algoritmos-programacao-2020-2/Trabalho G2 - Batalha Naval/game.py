import random

linhas = 5
colunas = 5
pontos = 0


def iniciaJogo():
    matrizes = iniciaMatrizes()
    while not verificaSeAcabouOJogo(matrizes[0]):
        printaPontuacao()
        printaMatriz(matrizes[1])
        matrizes = realizaJogada(matrizes)

    print("Fim de jogo.")


def iniciaMatrizes():
    matrizes = [0, 0]
    matrizes[0] = geraMatriz()
    matrizes[1] = geraMatrizInterface()
    return matrizes


def geraMatriz():
    cont = 0
    vet = [0] * colunas
    matriz = []

    while cont < linhas:
        matriz.append(vet.copy())
        cont += 1

    matriz = geraPosicoes(matriz)

    return matriz


def geraMatrizInterface():
    cont = 0
    vet = ["X"] * colunas
    matriz = []

    while cont < linhas:
        matriz.append(vet.copy())
        cont += 1

    return matriz


def geraPosicoes(matriz):
    matriz = geraPosicaoNavios(matriz)
    matriz = geraPosicaoSubmarino(matriz)
    matriz = geraPosicaoPortaAviao(matriz)
    matriz = geraPosicaoOnu(matriz)
    return matriz


def geraPosicaoNavios(matriz):
    linha = random.randint(0, linhas - 1)
    coluna = random.randint(0, colunas - 1)
    matriz[linha][coluna] = 1
    return matriz


def geraPosicaoSubmarino(matriz):
    i = 0
    while i < 2:
        linha = random.randint(0, linhas - 1)
        coluna = random.randint(0, colunas - 1)
        if matriz[linha][coluna] == 0:
            matriz[linha][coluna] = 2
            i += 1
        else:
            i = i
    return matriz


def geraPosicaoPortaAviao(matriz):
    i = 0
    while i < 3:
        linha = random.randint(0, linhas - 1)
        coluna = random.randint(0, colunas - 1)
        if matriz[linha][coluna] == 0:
            matriz[linha][coluna] = 3
            i += 1
        else:
            i = i
    return matriz


def geraPosicaoOnu(matriz):
    i = 0
    while i < 5:
        linha = random.randint(0, linhas - 1)
        coluna = random.randint(0, colunas - 1)
        if matriz[linha][coluna] == 0:
            matriz[linha][coluna] = 5
            i += 1
        else:
            i = i
    return matriz


def printaMatriz(matriz):
    i = 0
    print("    0    1    2    3    4")
    for linha in matriz:
        print(f"{i} {linha}")
        i += 1


def verificaSeAcabouOJogo(matriz):
    pontosRestantesAFazer = 0

    for linha in matriz:
        for elemento in linha:
            if elemento in (1, 2, 3):
                pontosRestantesAFazer += elemento

    if pontosRestantesAFazer <= 0:
        return True
    else:
        return False


def realizaJogada(matrizes):
    global pontos
    linha = int(input("Insira a linha: "))
    coluna = int(input("Insira a coluna: "))
    print('*' * 40)

    valorPosicao = matrizes[0][linha][coluna]
    if valorPosicao == 0:
        matrizes[1][linha][coluna] = 'A'

    if valorPosicao == 1:
        pontos += valorPosicao
        matrizes[0][linha][coluna] = 0
        matrizes[1][linha][coluna] = 'N'
        print('\033[32m' + 'Você acertou um navio inimigo.' + '\033[0;0m')
        print('\033[32m' + '+1 pontos' + '\033[0;0m')


    if valorPosicao == 2:
        pontos += valorPosicao
        matrizes[0][linha][coluna] = 0
        matrizes[1][linha][coluna] = 'S'
        print('\033[32m' + 'Você acertou um submarino inimigo.' + '\033[0;0m')
        print('\033[32m' + '+2 pontos' + '\033[0;0m')

    if valorPosicao == 3:
        pontos += valorPosicao
        matrizes[0][linha][coluna] = 0
        matrizes[1][linha][coluna] = 'P'
        print('\033[32m' + 'Belo tiro! Você acertou um porta-aviões inimigo.' + '\033[0;0m')
        print('\033[32m' + '+3 pontos' + '\033[0;0m')

    if valorPosicao == 5:
        pontos = pontos - 5
        matrizes[0][linha][coluna] = 0
        matrizes[1][linha][coluna] = 'O'
        print('\033[31m' + 'Oh não! Você acertou a ONU, -5 pontos.' + '\033[0;0m')

    if valorPosicao == 0:
        print("Seu tiro não acertou nada.")

    return matrizes


def printaPontuacao():
    print('\033[32m' + f"Pontuação: {pontos}" + '\033[0;0m')
