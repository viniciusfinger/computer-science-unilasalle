vetor = [1,2,3,73,5,6,66,7,73,9]

maiorValor = 0
posicaoMaiorValor = 0

for valor in vetor:
    if valor > maiorValor:
        maiorValor = valor
        posicaoMaiorValor = vetor.index(valor)

print(f'Maior valor {maiorValor} na posição {posicaoMaiorValor}')
