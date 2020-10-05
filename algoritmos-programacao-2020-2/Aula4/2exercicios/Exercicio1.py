# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E


def inputNotas():
    notas = []
    try:
         notas.append(float(input("Insira a primeira nota: ")))
         notas.append(float(input("Insira a segunda nota: ")))
         if (notas[0] >=0 and notas[1] >=0):
             return notas
         else:
             print("somente números maiores ou iguais a 0.")
             exit()
    except ValueError:
        print("Somente numeros.")
        exit()

def calculaMediaNotas(notas):
    return (sum(notas)/len(notas))

def classificaNota(notaMedia):
    if 9 < notaMedia <= 10:
        return 'A'
    if 8 < notaMedia <= 9:
        return 'B'
    if 6 < notaMedia <= 7.5:
        return 'C'
    if 4 < notaMedia <= 6:
        return 'D'
    if 0 <= notaMedia <= 6:
        return 'E'

def printaConceito(conceito):
    (f"O conceito é {conceito}")

notas = inputNotas()
notaMedia = calculaMediaNotas(notas)
conceito = classificaNota(notaMedia)
printaConceito(conceito) 