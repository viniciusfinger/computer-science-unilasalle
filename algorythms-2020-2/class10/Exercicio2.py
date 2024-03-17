def imprimeTrianguloSequencia(tamanho):
    i = 1
    while i <= tamanho:
        for x in range(1, i + 1):
            print(x, end='')
        print()
        i += 1


def inputTamanhoTriangulo() -> int:
    return int(input("Insira o tamanho do triangulo: "))


tamanhoTriangulo = inputTamanhoTriangulo()
imprimeTrianguloSequencia(tamanhoTriangulo)

