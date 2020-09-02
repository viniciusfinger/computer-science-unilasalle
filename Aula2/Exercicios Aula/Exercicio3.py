def entradaNumeros():
    numeros = []
    try:
        numeros.append(float(input("Insira o primeiro numero: ")))
        numeros.append(float(input("Insira o segundo numero: ")))
        numeros.append(float(input("Insira o terceiro numero: ")))
    except ValueError:
        print("Somente numeros.")
        exit()

    return numeros

def mediaNumeros(numeros):
    media = (numeros[0] + numeros[1] + numeros[2])/3
    return media

def printaMedia(media):
    print("A media eh", media)

def main():
    numeros = entradaNumeros()
    media = mediaNumeros(numeros)
    printaMedia(media)

main()