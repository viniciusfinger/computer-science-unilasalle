import math

def inputRaioEsfera():
    raio = float(input("Insira o raio: "))
    return raio

def calculaArea(raio):
    area = 4 * math.pi * (raio ** 2)
    return area

def printaArea(area):
    print("A area eh de %.2f cm quadrados." %area)


def main():
    raio = inputRaioEsfera()
    area = calculaArea(raio)
    printaArea(area)

main()