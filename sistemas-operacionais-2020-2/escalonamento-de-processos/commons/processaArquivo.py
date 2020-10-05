from commons.processo import Processo

def processaArquivo(arquivo):

    linhas = []
    processos = []

    for linha in arquivo:
        linha = linha.rstrip()
        linhas.append(linha)

    #print(f'processos: {linhas}')

    for linha in linhas:
        obj = linha.split(' ')
        processos.append(Processo(obj[0], int(obj[1]),int(obj[2])))

    return processos