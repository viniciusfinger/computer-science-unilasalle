from Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, departamento, senha, numeroFuncionariosGerenciados):
        super().__init__(nome, cpf, salario, departamento)
        self.senha = senha
        self.numeroFuncionariosGerenciados = numeroFuncionariosGerenciados
        
    def autenticarSenha(self, senha):
        return self.senha == senha
    
    def bonificar(self):
        self.salario = self.salario + (self.salario*0.15)
        return self.salario