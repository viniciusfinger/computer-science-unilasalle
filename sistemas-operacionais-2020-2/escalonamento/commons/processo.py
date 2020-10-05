class Processo:

    def __init__(self, nome, tamanho, prioridade):
        self.nome = nome
        self.tamanho = tamanho
        self.prioridade = prioridade
        self.estado = 'apto'

    def executa(self):
        print(f'executando {self.getNome()}, tamanho {self.getTamanho()}, prioridade {self.getPrioridade()}')

    def getNome(self):
        return self.nome

    def getTamanho(self):
        return self.tamanho

    def getPrioridade(self):
        return self.prioridade

    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

    def __str__(self):
        return self.nome
