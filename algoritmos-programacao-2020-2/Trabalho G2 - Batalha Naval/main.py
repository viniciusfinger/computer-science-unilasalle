from importlib import import_module
game = import_module("game")
import os

def executaMenu():
    print('-' * 40)
    print("Batalha Naval")
    print("1 - Jogar")
    print("2 - Instruções")
    print("3 - Sair")
    print('-' * 40)
    opcaoMenu = int(input("Escolha uma opção: "))
    print('-' * 40)

    if opcaoMenu == 1:
        print('\033[32m' + 'Iniciando Jogo...' + '\033[0;0m')
        game.iniciaJogo()

    elif opcaoMenu == 2:
        print("Instruções......")

    elif opcaoMenu == 3:
        print('\033[31m' + 'Saindo do jogo...' + '\033[0;0m')
        exit()


while True:
    executaMenu()


