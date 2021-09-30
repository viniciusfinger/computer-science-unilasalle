from Empregado import Empregado

class Horista(Empregado):
    def __init__(self, nome, valorHora, horasTrabalhadas):
        super().__init__(nome)
        self.valorHora = valorHora
        self.horasTrabalhadas = horasTrabalhadas
    
    def retornaPagamento(self):
        return (self.valorHora * self.horasTrabalhadas * 4.5)