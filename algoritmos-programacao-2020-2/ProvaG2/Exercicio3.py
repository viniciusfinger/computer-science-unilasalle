import random


def inputFuncaoPrograma():
    while True:
        print("1 - Mostra números pares do número de entrada até 0")
        print("2 - Gera um array de 25 posições aleatórias e depois inverte ele.")
        print('-' * 40)

        funcaoPrograma = int(input("Insira a funcao do programa: "))

        if funcaoPrograma in (1,2):
            return funcaoPrograma
        else:
            print("Somente as opções mostradas na tela.")

def printaNumerosPares():
        numero = int(input("Insira o número: "))

        while numero > 0:
            if (numero % 2) == 0:
                print(f"{numero} é par")
            numero -= 1

def geraEInverteArray():
    i = 0
    array = []
    while i < 25:
        array.append(random.randint(0 , 100))
        i += 1

    print(array)
    print(array[::-1])

opcao = inputFuncaoPrograma()

if opcao == 1:
    printaNumerosPares()

if opcao == 2:
    geraEInverteArray()
