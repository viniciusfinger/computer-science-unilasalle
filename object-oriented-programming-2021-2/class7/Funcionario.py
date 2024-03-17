class Funcionario:
    def __init__(self, nome, cpf, salario, departamento):
        self.nome = nome 
        self.cpf = cpf
        self.salario = salario
        self.departamento = departamento

    def bonificar(self):
        self.salario = self.salario + (self.salario*0.1)
        return self.salario
    