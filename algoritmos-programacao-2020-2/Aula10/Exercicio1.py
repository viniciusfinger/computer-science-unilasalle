def imprimeTriangulo(tamanho):
    i = 1
    while i <= tamanho:
        for x in range(i):
            print(i, end='')
        print()
        i += 1


def inputTamanhoTriangulo() -> int:
    return int(input("Insira o tamanho do triangulo: "))


tamanhoTriangulo = inputTamanhoTriangulo()
imprimeTriangulo(tamanhoTriangulo)
