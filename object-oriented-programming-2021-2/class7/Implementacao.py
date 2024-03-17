from Gerente import Gerente
from Vendedor import Vendedor

gerente = Gerente("Valdecir", "046.852.120-33", 9000, "Vendas geral", "123456", 10)
vendedor = Vendedor("Cleber", "230.409.103-00", 1200, "Vendas domésticas", 5, 50)

print("Tentando autenticar gerente com a senha 244: ")
print("Resultado: " + str(gerente.autenticarSenha("244")))

print("o salário do gerente é " + str(gerente.salario) + " e com a bonificação fica " + str(gerente.bonificar()))
print("----------")
print("vendedor começou o mês com " + str(vendedor.quantidadeVendas) + " mas fechou o mês com " + str(vendedor.atualizaQuantidadeVendas(50)))
print("E o salário do vendedor é " + str(vendedor.calculaSalario()))

