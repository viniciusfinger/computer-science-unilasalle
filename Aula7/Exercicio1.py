# matriz de 1 a 100 usando dois laços.

linha = [''] * 10
matriz = []

num = 1
i = 0

while i < 10:
    matriz.append(linha.copy())
    j = 0

    while j < 10:
        matriz[i][j] = num
        j += 1
        num += 1

    print(matriz[i])
    i += 1

