from commons.processaArquivo import processaArquivo

#Escalonamento FIRST IN - FIRST OUT

arquivo = open("commons/processos.txt", 'r')
processos = processaArquivo(arquivo)

for processo in processos:
    processo.executa()