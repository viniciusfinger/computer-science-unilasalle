def soma(n1,n2,n3):
    return n1 + n2 + n3

try:
    n1 = float(input("Insira o primeiro número: "))
    n2 = float(input("Insira o segundo número: "))
    n3 = float(input("Insira o terceiro número: "))
except ValueError:
    print("Somente números.")
    exit()

somaNumeros = soma(n1,n2,n3)
print(f"A soma dos 3 números é {somaNumeros}")
