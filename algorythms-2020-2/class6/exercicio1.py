
notas = []
i = 1;

try:
    tamanhoTurma = int(input("Insira a quantidade de alunos na turma: "))
    if tamanhoTurma < 1:
        print("a turma precisa ter pelo menos uma pessoa.")
        exit()
except ValueError:
    print("somente números.")
    exit()

try:
    while i <= tamanhoTurma:
        nota = float(input(f"insira a média das notas do aluno {i}: "))
        if nota > 10 or nota < 0:
            print("somente valores positivos e menores ou iguais a 10.")
            exit()
        else:
            notas.append(nota)
        i += 1
except ValueError:
    print("somente números.")
    exit()

mediaNotas = sum(notas) / tamanhoTurma
print(f"a média da turma é {mediaNotas}")