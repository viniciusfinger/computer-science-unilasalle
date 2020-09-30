matriz = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]] #matriz 3x3

vetorPares = []
contagemPares = 0

for vetor in matriz:
    for valor in vetor:
        if valor % 2 == 0:
            vetorPares.append(valor)
            contagemPares += 1

print(f'números pares na matriz: {vetorPares}, totalizando {contagemPares} números.')


