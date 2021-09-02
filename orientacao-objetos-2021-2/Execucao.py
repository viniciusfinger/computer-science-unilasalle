from Carro import Carro
from Modelo import Modelo
from Montadora import Montadora
import os

def limpaTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#carro de teste
montadora = Montadora(str(1), "RS", "CHEVROLET")
modelo = Modelo(str(1),"CORSA",montadora)
carro = Carro("IHF-25551", modelo, "1998")

carrosCadastrados = []

carrosCadastrados.append(carro)

while (True):
    print("==============================")
    print("       Sistema de carro")
    print("==============================")

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
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("     Opção inválida")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        else:
            opcaoValida = True
        
    if opcao == 1:
        limpaTerminal()
        print("==============================")
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
        print("==============================")
        print("Carro cadastrado com sucesso.")


    if opcao == 2:
        limpaTerminal()
        print("==============================")
        print("  Listando todos os carros")
        print("==============================")
        
        print(len(carrosCadastrados))

        for carro in carrosCadastrados:
            print("Montadora: " + carro.modelo.montadora.razaoSocial + "/" + carro.modelo.montadora.estado)
            print("Modelo:" + carro.modelo.nome + "(cód. " + carro.modelo.codigo + ")")
            print("Ano de fabricação: " + carro.anoFabricacao)
            print("Placa: " + carro.placa)
            print("==============================")        

    if opcao == 3:
        '''TO-DO: IMPLEMENTAR AQUI A EDIÇÃO DE CARRO. PARA ISSO, O ID VAI TER QUE SER ÚNICO DENTRO DO ARRAY DE VEÍCULOS E VAI TER
        QUE SER FEITA UMA BUSCA PELO ID NO ARRAY. APÓS ISSO, PERGUNTAR QUAL ATRIBUTO QUER EDITAR. '''


    if opcao == 4:
        exit()


