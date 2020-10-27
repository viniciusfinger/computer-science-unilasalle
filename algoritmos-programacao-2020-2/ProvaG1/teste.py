vetor = []
x = 0


tamanhoC = int(input("Insira a quantidade de valores que terá o conjunto: "))

print ('\n')

while x < tamanhoC:
    vetor.append(float(input("Digite um valor: ")))
    x += 1

print('Os seus resultados encontrados foram:\n')
print(f"O seu menor valor digitado foi: {min(vetor)}, Maior valor: {max(vetor)}")
print(f"A média dos seus valores é: {sum(vetor)/len(vetor)}")
print(f"A soma dos seus valores: {sum(vetor)}")
print(f"O conjunto digitado foi: {vetor}")