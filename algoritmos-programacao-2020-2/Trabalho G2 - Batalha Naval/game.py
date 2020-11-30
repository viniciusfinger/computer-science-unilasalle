import random

quantidadeJogadores = 1
linhas = 5
colunas = 5
pontos = [0, 0, 0]
jogadorAtual = 0
arrayRodadas = [0]


def iniciaJogo():
    matrizes = iniciaMatrizes()
    setQtdJogadores()

    print('\033[32m' + 'Iniciando Jogo...' + '\033[0;0m')

    while not verificaSeAcabouOJogo(matrizes[0]):
        validaJogador()
        printaPontuacao(jogadorAtual)
        printaMatriz(matrizes[1])
        matrizes = realizaJogada(matrizes, jogadorAtual)

    validaGanhador(pontos)


def setQtdJogadores():
    global arrayRodadas
    while True:
        qtdJogadores = int(input("Insira a quantidade de jogadores: "))
        if qtdJogadores in (1,2,3):
            break
        else:
            print("Somente de 1 a 3 jogadores.")

    if qtdJogadores == 1:
        arrayRodadas = [0]
    if qtdJogadores == 2:
        arrayRodadas = [0, 1]
    if qtdJogadores == 3:
        arrayRodadas = [1, 2]


def validaJogador():
    global jogadorAtual
    if jogadorAtual in arrayRodadas:
        jogadorAtual += 1
    else:
        jogadorAtual = 1


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


def realizaJogada(matrizes, jogadorAtual):
    global pontos
    while True:
        linha = int(input("Insira a linha: "))
        if linha in (0,1,2,3,4):
            break
        else:
            print("Somente números de 0 a 4")

    while True:
        coluna = int(input("Insira a coluna: "))
        if coluna in (0,1,2,3,4):
            break
        else:
            print("Somente números de 0 a 4")

    print('*' * 40)

    valorPosicao = matrizes[0][linha][coluna]
    if valorPosicao == 0:
        matrizes[1][linha][coluna] = 'A'
        print("Seu tiro pegou na água.")

    if valorPosicao == 1:
        pontos[jogadorAtual] += valorPosicao
        matrizes[0][linha][coluna] = 0
        matrizes[1][linha][coluna] = 'N'
        print('\033[32m' + 'Você acertou um navio inimigo.' + '\033[0;0m')
        print('\033[32m' + '+1 pontos' + '\033[0;0m')

    if valorPosicao == 2:
        pontos[jogadorAtual - 1] += valorPosicao
        matrizes[0][linha][coluna] = 0
        matrizes[1][linha][coluna] = 'S'
        print('\033[32m' + 'Você acertou um submarino inimigo.' + '\033[0;0m')
        print('\033[32m' + '+2 pontos' + '\033[0;0m')

    if valorPosicao == 3:
        pontos[jogadorAtual - 1] += valorPosicao
        matrizes[0][linha][coluna] = 0
        matrizes[1][linha][coluna] = 'P'
        print('\033[32m' + 'Belo tiro! Você acertou um porta-aviões inimigo.' + '\033[0;0m')
        print('\033[32m' + '+3 pontos' + '\033[0;0m')

    if valorPosicao == 5:
        pontos[jogadorAtual - 1] -= 5
        matrizes[0][linha][coluna] = 0
        matrizes[1][linha][coluna] = 'O'
        print('\033[31m' + 'Oh não! Você acertou a ONU, -5 pontos.' + '\033[0;0m')

    print('*' * 40)
    return matrizes


def printaPontuacao(jogadorAtual):
    print('\033[32m' + f"Turno do jogador {jogadorAtual}         Pontuação: {pontos[jogadorAtual - 1]}" + '\033[0;0m')


def validaGanhador(pontos):
    ganhador = 'Empate'

    jogador1 = pontos[0]
    jogador2 = pontos[1]
    jogador3 = pontos[2]

    if jogador1 > jogador2 and jogador1 > jogador3:
        ganhador = 'Jogador 1'

    if jogador2 > jogador1 and jogador2 > jogador3:
        ganhador = 'Jogador 2'

    if jogador3 > jogador2 and jogador3 > jogador1:
        ganhador = 'Jogador 3'

    if ganhador == 'Empate':
        print("Fim de jogo. Houve um empate.")

    else:
        print(f"Fim de jogo. O ganhador foi o {ganhador}")
