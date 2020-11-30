#Desenvolvido por Vinícius Finger (201920133) e Thaynara Fumegali (201920132)

from importlib import import_module
game = import_module("game")

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
        game.iniciaJogo()

    elif opcaoMenu == 2:
        print("Insira o número da linha e da coluna desejados para realizar um tiro. O jogo acaba quando não houver mais embarcações inimigas.")
        print("Você ganha um ponto ao acertar um navio, dois ao acertar um submarino, três ao acertar um porta-aviões e perde 5 pontos se acertar a ONU.")
        print("O vencedor será quem ganhar mais pontos.")

    elif opcaoMenu == 3:
        print('\033[31m' + 'Saindo do jogo...' + '\033[0;0m')
        exit()

    else:
        print("Opção inválida, selecione outra.")


while True:
    executaMenu()


