import operator

from commons.processaArquivo import processaArquivo

# Escalonamento SHORTEST JOB FIRST

arquivo = open("commons/processos.txt", 'r')
processos = processaArquivo(arquivo)
processosOrdenados = sorted(processos, key=operator.attrgetter('tamanho'))

for processo in processosOrdenados:
    processo.executa()
