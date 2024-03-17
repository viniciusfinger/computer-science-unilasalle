from Empregado import Empregado

class Assalariado(Empregado):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.salario = salario

    def retornaPagamento(self):
        return self.salario
    