def inputInformacaoRenda():
    dadosRenda = []
    try:
        dadosRenda.append(float(input("Insira quanto você ganha por hora em Reais: ")))
        dadosRenda.append(float(input("Insira quantas horas você trabalha por dia: ")))
    except ValueError:
        print("Somente números.")
        exit()

    return dadosRenda

def calculaSalario(dadosRenda):
    #admitindo que um mês de trabalho = 30 dias.
    return (dadosRenda[0]*dadosRenda[1]) * 30

def printaSalario(salario):
    print(f"O salário é de R${salario}")

dadosRenda = inputInformacaoRenda()
salario = calculaSalario(dadosRenda)
printaSalario(salario)