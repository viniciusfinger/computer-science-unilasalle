def entradaNumero():
    try:
        return float(input("Insira um número: "))
    except ValueError:
        print("Somente números.")
        exit()

def printaFrase(num):
    print(f"O número informado é: {num}")

num = entradaNumero()
printaFrase(num)
