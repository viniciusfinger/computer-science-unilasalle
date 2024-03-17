def printLinha():
    print("---------------------------------------------")

def inputValores():
    dadosPessoa = []
    dadosPessoa.append(float(input("Insira qual o seu peso: ")))
    dadosPessoa.append(float(input("Insira a sua altura: ")))

    return dadosPessoa

def calculaIMC(dadosPessoa):
    IMC = dadosPessoa[0] / (dadosPessoa[1]**2)
    return IMC

def printConsumo(IMC):
    print("O seu IMC eh %.2f" %IMC)

def main():
    print("-----------CALCULADORA DE IMC------------")
    dadosPessoa = inputValores()
    printLinha()
    IMC = calculaIMC(dadosPessoa)
    printConsumo(IMC)
    printLinha()

main()