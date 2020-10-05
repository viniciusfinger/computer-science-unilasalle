def entradaNotas():
    retornoNotas = []
    try:
        retornoNotas.append(float(input("Insira a primeira nota:")))
        retornoNotas.append(float(input("Insira a segunda nota:")))
        retornoNotas.append(float(input("Insira a terceira nota:")))
        retornoNotas.append(float(input("Insira a quarta nota:")))
    except ValueError:
        print("Somente números.")
        exit()

    return retornoNotas

def calculaMediaNotas(notas):
    return sum(notas) / len(notas)

def printaMensagemMediaNotas(mediaNota):
    print(f"A média das notas é: {mediaNota}")

notas = entradaNotas()
mediaNotas = calculaMediaNotas(notas)
printaMensagemMediaNotas(mediaNotas)