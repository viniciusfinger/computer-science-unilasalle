vetor = [1,2,3,4,5,6,7,8,9,10]
vetorPares = []
contagemPares = 0

for valor in vetor:
    if (valor % 2 == 0):
        vetorPares.append(valor)
        contagemPares += 1
        
print(vetorPares)


