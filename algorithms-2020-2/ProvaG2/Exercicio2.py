registroEmpregado = {'codigo': 0, 'dataNascimento': '30/10/2001', 'nome': 'Vinicius Finger', 'rg': '04685212098', 'salario': 15000.00}

funcionarios = []

def inputQtdFuncionarios():
    while True:
        qtdFuncionarios = int(input("Insira a quantidade de funcionários: "))
        if qtdFuncionarios > 0:
            return qtdFuncionarios
        else:
            print("Quantidade de funcionários deve ser maior que zero.")


qtdFuncionarios = inputQtdFuncionarios()
i = 0

while i < qtdFuncionarios:
    codigo = {'codigo': i}
    nomeFuncionario = {'nome': input("Insira o nome do funcionário: ")}
    dataNascimento = {'dataNascimento': input("Insira a data de nascimento do funcionário: ")}
    rgFuncionario = {'rg': input("Insira o rg do funcionário: ")}
    salarioFuncionario = {'salario': input("Insira o salário do funcionário: ")}

    registroEmpregado.update(codigo)
    registroEmpregado.update(nomeFuncionario)
    registroEmpregado.update(dataNascimento)
    registroEmpregado.update(rgFuncionario)
    registroEmpregado.update(salarioFuncionario)

    funcionarios.append(registroEmpregado.copy())

    i += 1

for funcionario in funcionarios:
    print(funcionario)