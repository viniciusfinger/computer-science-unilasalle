try:
    notaG1 = float(input("Insira nota do G1: "))
    notaG2 = float(input("Insira nota do G2: "))
except ValueError:
    print("Somente numerros.")
    exit(-1)

mediaNotas = (notaG1 + notaG2)/2

if mediaNotas < 6:
    print("a nota eh",mediaNotas,", Reprovado...")
else:
    print("A nota eh", mediaNotas, ", Aprovado...")