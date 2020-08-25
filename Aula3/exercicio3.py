def entradaNumeros():
    retornoNumeros = []
    try:
        retornoNumeros.append(float(input("Insira um número: ")))
        retornoNumeros.append(float(input("Insira outro número: ")))

    except ValueError:
        print("Somente números.")
        exit()

    return retornoNumeros

def somaNumeros(numeros):
    return numeros[0] + numeros[1]

def printaSoma(soma):
    print(f"a soma é: {soma}")

numeros = entradaNumeros()
printaSoma(somaNumeros(numeros))