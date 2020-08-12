def printLinha():
    print("---------------------------")

def entradaDadosNascimento():
    retornoDadosNascimento = []
    try:
        retornoDadosNascimento.append(int(input("Informe o dia do seu nascimento: ")))
        retornoDadosNascimento.append(int(input("Informe o mes do seu nascimento: ")))
        retornoDadosNascimento.append(int(input("Informe o ano do seu nascimento: ")))
    except ValueError:
        print("Somente numeros inteiros sao permitidos.")
        exit()

    return retornoDadosNascimento

def setNomeMes(dadosNascimento):
    mes = dadosNascimento[1]
    mes = mes - 1
    meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
             'novembro', 'dezembro']
    dadosNascimento[1] = meses[mes]
    return dadosNascimento

def printaFraseNascimento(dadosNascimento):
    print("Voce nasceu em " + str(dadosNascimento[0]) + " de " + str(dadosNascimento[1]) + " de " + str(dadosNascimento[2]))

def validaDadosNascimento(dadosNascimento):
    if (dadosNascimento[0] <= 0):
        print("Dia invalido.")
        exit()

    if (dadosNascimento[1] > 12 or dadosNascimento[1] <= 0):
        print("mes invalido.")
        exit()

    if (dadosNascimento[2] <= 0):
        print("Ano invalido.")
        exit()

    return dadosNascimento

def main():
    print("Favor colocar somente numeros.")
    printLinha()
    dadosNascimento = entradaDadosNascimento()
    dadosNascimento = validaDadosNascimento(dadosNascimento)
    dadosNascimento = setNomeMes(dadosNascimento)
    printLinha()
    printaFraseNascimento(dadosNascimento)
    printLinha()

main()