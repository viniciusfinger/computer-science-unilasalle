import math


##formula do volume da esfera -> V = 4/3 * pi * r ao cubo

def inputRaio():
    return int(input("Insira o raio em cm: "))


def calculaVolumeEsfera(raio):
    volume = (4 * math.pi * (raio ** 3)) / 3
    return volume

def printaVolumeEsfera(volume):
    print("O volume da esfera eh %.2f cm cúbicos." %volume)

def main():
    raio = inputRaio()
    volume = calculaVolumeEsfera(raio)
    printaVolumeEsfera(volume)

main()