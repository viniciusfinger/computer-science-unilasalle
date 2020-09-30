vetor = [1,2,3,4,5,6,7,8,9,10]
vetorNaoDuplicados = []

for valor in vetor:
    if valor not in vetorNaoDuplicados:
        vetorNaoDuplicados.append(valor)

if len(vetor) != len(vetorNaoDuplicados):
    print('há repetidos')
else:
    print('não há repetidos.')
