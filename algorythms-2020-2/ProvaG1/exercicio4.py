#Vinícius Finger - 201920133

def encerraPrograma():
    print("Somente números inteiros e positivos.")
    exit()

def calculaProgressao(tamanho):
    numerador = 1
    denominador = 1
    total = 0

    while denominador <= tamanho:
        total += (numerador / denominador)
        numerador += 2
        denominador += 1
    return total


try:
    tamanho = int(input("Insira o valor de N da progressão: "))
    if tamanho <= 0:
        encerraPrograma()
except ValueError:
    encerraPrograma()

resultado = calculaProgressao(tamanho)

print("\n")
print(f"Resultado da soma da progressão: {resultado}")

