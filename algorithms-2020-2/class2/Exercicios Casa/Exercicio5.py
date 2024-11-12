def printLinha():
    print("---------------------------------------------")

def inputValores():
    dadosConsumo = []
    dadosConsumo.append(float(input("Insira quantos litros foram gastos: ")))
    dadosConsumo.append(float(input("Insira a quilometragem feita: ")))

    return dadosConsumo

def calculaConsumo(dadosConsumo):
    consumoMedio = dadosConsumo[1]/dadosConsumo[0]
    return consumoMedio

def printConsumo(consumoMedio):
    print("O consumo medio foi de %.2f kilometros por litro" %consumoMedio)


def main():
    print("-----------CALCULADORA DE CONSUMO------------")
    dadosConsumo = inputValores()
    printLinha()
    consumoMedio = calculaConsumo(dadosConsumo)
    printConsumo(consumoMedio)
    printLinha()

main()