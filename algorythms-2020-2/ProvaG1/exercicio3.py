#Vinícius Finger - 201920133

conjunto = []
i = 0

def encerraPrograma():
    print("Somente números inteiros e positivos.")
    exit()

def printLn():
    print("|" + ("-"*49) + "|")


try:
    tamanhoConjunto = int(input("Insira a quantidade de valores que terá o conjunto: "))
    if tamanhoConjunto <= 0:
        encerraPrograma()
except ValueError:
    encerraPrograma()

while i < tamanhoConjunto:
    try:
        conjunto.append(float(input("Insira um valor: ")))
        i += 1
    except ValueError:
        print("Somente números.")
        exit()

printLn()
print(f"Menor valor: {min(conjunto)}, Maior valor: {max(conjunto)}")
print(f"Média dos valores: {sum(conjunto)/len(conjunto)}")
print(f"Soma dos valores: {sum(conjunto)}")
print(f"Conjunto: {conjunto}")
printLn()
