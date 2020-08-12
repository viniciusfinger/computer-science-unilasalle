def entradaDadosCurso():
    dadosCursoRetorno = []
    dadosCursoRetorno.append(input("Insira seu curso: "))
    dadosCursoRetorno.append(input("Insira o tempo de duracao: "))
    return dadosCursoRetorno

def printaFrase(dadosCurso):
    print("Voce estuda " + dadosCurso[0] + " que dura " + dadosCurso[1] + " semestres.")


dadosCurso = entradaDadosCurso()
printaFrase(dadosCurso)
