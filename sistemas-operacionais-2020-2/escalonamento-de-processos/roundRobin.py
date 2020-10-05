from commons.processaArquivo import processaArquivo

# Escalonamento Round Robin

arquivo = open("commons/processos.txt", 'r')
processos = processaArquivo(arquivo)
fila = []
ciclo = 0
quantum = 10


def verificaFilaProcessos(processos):
    tamanho = 0
    for processo in processos:
        tamanho = tamanho + processo.tamanho
    if tamanho > 0:
        return True
    else:
        return False


while verificaFilaProcessos(processos):
    ciclo += 1
    print(f'ciclo: {ciclo}')
    for processo in processos:
        if processo.tamanho > 0:
            print(f"processando {processo.getNome()}, tamanho atual: {processo.getTamanho()}")
            processo.tamanho = processo.tamanho - quantum