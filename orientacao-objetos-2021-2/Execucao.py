from Carro import Carro
from Modelo import Modelo
from Montadora import Montadora
import os

def limpaTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def printaLinha():
    print("==============================")

#carro de teste
montadora = Montadora(str(1), "RS", "CHEVROLET")
modelo = Modelo(str(1),"CORSA",montadora)
carro = Carro("IHF-25551", modelo, "1998")

carrosCadastrados = []

carrosCadastrados.append(carro)
limpaTerminal()

while (True):
    printaLinha()
    print("       Sistema de carro")
    printaLinha()

    opcaoValida = False

    while (not opcaoValida):
        print("Opções:")
        print("1 - Cadastrar novo carro")
        print("2 - Exibir carros")
        print("3 - Editar carro")
        print("4 - Sair")
        
        opcao = int(input("insira uma opção: "))

        if (opcao not in [1,2,3,4]):
            limpaTerminal()
            printaLinha()
            print("     Opção inválida")
            printaLinha()
        else:
            opcaoValida = True
        
    if opcao == 1:
        limpaTerminal()
        printaLinha()
        print("    Cadastro de carro:")
        carro = Carro()
        modelo = Modelo()
        montadora = Montadora()

        carro.placa = input("Insira a placa do carro: ")
        carro.anoFabricacao = input("Insira o ano de fabricação do carro: ")
        
        montadora.razaoSocial = input("Qual a razão social da montadora? ")
        montadora.estado = input("Qual a UF da montadora? ")
        montadora.codigo = input("Qual o código da montadora? ")
        
        modelo.nome = input("Qual o nome do modelo? ")
        modelo.codigo = input("Qual o código do modelo? ")
        
        modelo.montadora = montadora
        carro.modelo = modelo
        
        carrosCadastrados.append(carro)
        
        limpaTerminal()
        printaLinha()
        print("Carro cadastrado com sucesso.")


    if opcao == 2:
        limpaTerminal()
        printaLinha()
        print("  Listando todos os carros")
        printaLinha()
        
        print(len(carrosCadastrados))

        for carro in carrosCadastrados:
            print("Montadora: " + carro.modelo.montadora.razaoSocial + "/" + carro.modelo.montadora.estado)
            print("Modelo:" + carro.modelo.nome + "(cód. " + carro.modelo.codigo + ")")
            print("Ano de fabricação: " + carro.anoFabricacao)
            print("Placa: " + carro.placa)
            printaLinha()

    if opcao == 3:
        opcaoValidaEdicao = False
        opcaoValidaEdicaoMontadora = False
        opcaoValidaEdicaoModelo = False
        opcaoValidaEdicaoCarro = False

        placaCarroEditar = input("Insira a placa do carro que você quer editar: ")

        carroEditar = ""

        for carro in carrosCadastrados:
            if carro.placa == placaCarroEditar:
                carroEditar = carro

        limpaTerminal()

        if carroEditar == "":
            printaLinha()
            print("Carro não encontrado. Digite exatamente igual a placa listada na opção de listar veículo.")
            printaLinha()
        
        else: 
            while not opcaoValidaEdicao:
                printaLinha()
                print("Escolha a opção que quer editar:")
                print("1 - Montadora")
                print("2 - Modelo")
                print("3 - Carro")
                opcaoEdicao = int(input("Insira sua opção: "))
                
                if opcaoEdicao not in [1,2,3]:
                    print("Opção inválida.")
                else: 
                    opcaoValidaEdicao = True
            
            if opcaoEdicao == 1:
                while not opcaoValidaEdicaoMontadora:
                    print("Escolha o que quer editar na montadora:")
                    print("1 - Código")
                    print("2 - Estado")
                    print("3 - RazaoSocial")
                    opcaoEdicaoMontadora = int(input("Insira sua opção: "))

                    if opcaoEdicaoMontadora not in [1,2,3]:
                        print("Opção inválida.")
                    else: 
                        opcaoValidaEdicaoMontadora = True       

                if opcaoEdicaoMontadora == 1:
                    carroEditar.modelo.montadora.codigo = input("Insira o novo código da montadora: ")

                if opcaoEdicaoMontadora == 2:
                    carroEditar.modelo.montadora.estado = input("Insira o estado da montadora: ")
                
                if opcaoEdicaoMontadora == 3:
                    carroEditar.modelo.montadora.razaoSocial = input("Insira a razão social da montadora: ")

            if opcaoEdicao == 2:
                while not opcaoValidaEdicaoModelo: 
                    print("insira uma opção: ")
                    print("1 - Codigo")
                    print("2 - Nome")

                    opcaoEdicaoModelo = int(input())

                    if opcaoEdicaoModelo not in [1,2]:
                        print("opção invalida")
                    else: 
                        opcaoValidaEdicaoModelo = True 
                
                if opcaoEdicaoModelo == 1:
                    carroEditar.modelo.codigo = input("Insira o novo código do modelo: ")
                if opcaoEdicaoModelo == 2:
                    carroEditar.modelo.nome = input("Insira o novo nome do modelo: ")

            if opcaoEdicao == 3:
                while not opcaoValidaEdicaoCarro:
                    print("Insira uma opção: ")
                    print("1 - Placa")
                    print("2 - Ano de fabricação")
                    opcaoEdicaoCarro = int(input())
                
                    if opcaoEdicaoCarro not in [1,2]:
                        print("Opção inválida")
                    else:
                        opcaoValidaEdicaoCarro = True
                
                if opcaoEdicaoCarro == 1:
                    carroEditar.placa = input("Insira a nova placa: ")
                if opcaoEdicaoCarro == 2:
                    carroEditar.anoFabricacao = input("Insira o novo ano de fabricação: ")                    

    if opcao == 4:
        exit()
