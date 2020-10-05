import operator

from commons.processaArquivo import processaArquivo

#Escalonamento por prioridade

arquivo = open("commons/processos.txt", 'r')
processos = processaArquivo(arquivo)
processosOrdenados = sorted(processos, key=operator.attrgetter('prioridade'))

for processo in processosOrdenados:
    processo.executa()