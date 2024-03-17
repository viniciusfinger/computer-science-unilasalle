# Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
programaExecuta = True
valorTotal = 0
qtdPrestacoes = 0


def valorPagamento(valorPrestacao, diasAtraso):
    if diasAtraso == 0:
        return valorPrestacao
    else:
        return valorPrestacao + (valorPrestacao * 0.03) + ((diasAtraso * 0.001) * valorPrestacao)


while programaExecuta:
    inputPrestacao = float(input("Insira o valor da prestação: "))
    if inputPrestacao < 0:
        print("Prestação deve ser maior do que zero.")
        exit()

    if inputPrestacao == 0:
        programaExecuta = False

    else:
        inputDiasAtraso = int(input("Insira a quantos dias está atrasado: "))

        if inputDiasAtraso < 0:
            print("Os dias em atraso devem ser maiores ou iguais a zero.")
            exit()

        valorDivida = valorPagamento(inputPrestacao, inputDiasAtraso)
        valorTotal += valorDivida
        qtdPrestacoes += 1

        print(f"Deverá ser pago R${valorDivida}")

print(f"Valor total R${valorTotal}")
print(f"Quantidade de prestações: {qtdPrestacoes}")
