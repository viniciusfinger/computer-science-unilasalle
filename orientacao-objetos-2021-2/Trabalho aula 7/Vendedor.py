from Funcionario import Funcionario

class Vendedor(Funcionario):
    def __init__(self, nome, cpf, salario, departamento, quantidadeVendas, comissao):
        super().__init__(nome, cpf, salario, departamento)
        self.quantidadeVendas = quantidadeVendas
        self.comissao = comissao
        
    def atualizaQuantidadeVendas(self, quantidade):
        self.quantidadeVendas += quantidade
        return self.quantidadeVendas
    
    def calculaSalario(self):
        return self.salario + self.comissao