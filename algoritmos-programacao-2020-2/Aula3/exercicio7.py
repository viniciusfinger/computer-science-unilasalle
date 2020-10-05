def inputDadosQuadrado():
    dadosQuadrado = []
    try:
        dadosQuadrado.append(float(input("Insira a base do quadrado:")))
        dadosQuadrado.append(float(input("Insira a altura do quadrado:")))
    except ValueError:
        print("somente números.")
        exit()
    return dadosQuadrado

def calculaAreaQuadrado(dadosQuadrado):
    return dadosQuadrado[0] * dadosQuadrado[1]

def printaDobroAreaQuadrado(areaQuadrado):
    print(f"o dobro da area do quadrado é: {areaQuadrado * 2}")

dadosQuadrado = inputDadosQuadrado()
areaQuadrado = calculaAreaQuadrado(dadosQuadrado)
printaDobroAreaQuadrado(areaQuadrado)