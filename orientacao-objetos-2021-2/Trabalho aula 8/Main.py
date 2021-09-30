from Assalariado import Assalariado
from Horista import Horista

funcionarios = []
opcaoInvalida = True

while opcaoInvalida:
    print("Folha de pagamento")
    print("------------------")
    print("Inserir:")
    print("1 - Assalariado ")
    print("2 - Horista ")
    print("3 - Calcular folha de pagamento ")
    print("4 - Sair")
    opcao = input()

    if opcao not in ["1","2","3","4"]:
        print("Opção inválida.")
    else:
        opcaoInvalida = False

    if opcao == "1":
        nome = input("Insira o nome do funcionário: ")
        salario = int(input("Insira o salário: "))
        funcionario = Assalariado(nome, salario)
        funcionarios.append(funcionario)
        opcaoInvalida = True

    if opcao == "2":
        nome = input("Insira o nome do funcionário: ")
        valorHora = int(input("Insira o valor da hora: "))
        horasTrabalhadas = int(input("Insira quantas horas foram trabalhadas: "))
        funcionario = Horista(nome, valorHora, horasTrabalhadas)
        funcionarios.append(funcionario)
        opcaoInvalida = True

    if opcao == "3":
        for funcionario in funcionarios:
            valorTotal = 0
            valorTotal += funcionario.retornaPagamento()
            print("O valor total é R$" + str(valorTotal))
            opcaoInvalida = True    
    
    if opcao == "4":
        exit()        