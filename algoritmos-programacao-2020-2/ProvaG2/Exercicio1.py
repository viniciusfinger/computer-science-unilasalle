def inputDiaSemana():
    while True:
        print("1 - Segunda-feira")
        print("2 - Terça-feira")
        print("3 - Quarta-feira")
        print("4 - Quinta-feira")
        print("5 - Sexta-feira")
        print("6 - Sábado")
        print("7 - Domingo")
        print('-' * 35)

        diaSemana = int(input("Insira o dia da semana: "))
        if diaSemana in (1, 2, 3, 4, 5, 6, 7):
            return diaSemana


def inputQtdConvidados():
    while True:
        qtdConvidados = int(input("Insira a quantidade de pessoas: "))
        if qtdConvidados >= 0:
            return qtdConvidados
        else:
            print("Quantidade de pessoas deve ser maior ou igual 0.")


def calculaLotacaoPandemia(diaSemana):
    lotacaoMaxima = 5000
    taxaDiaSemana = 0.3333
    taxaFimSemana = 0.5
    convidadosExcedentes = 0

    if diaSemana in (1, 2, 3, 4, 5):
        lotacaoMaximaPandemia = int(lotacaoMaxima * taxaDiaSemana)

    if diaSemana in (6, 7):
        lotacaoMaximaPandemia = int(lotacaoMaxima * taxaFimSemana)

    return lotacaoMaximaPandemia

def calculaConvidadosExcedentes(lotacaoMaximaPandemia, qtdConvidados):

    if lotacaoMaximaPandemia < qtdConvidados:
        return (lotacaoMaximaPandemia - qtdConvidados) * -1

    else:
        return 0

def printaMensagemExcedentes(lotacaoMaximaPandemia, qtdConvidadosExcedentes):
    if diaSemana == 1:
        diaSemanaTexto = 'Segunda-feira'
    if diaSemana == 2:
        diaSemanaTexto = 'Terça-feira'
    if diaSemana == 3:
        diaSemanaTexto = 'Quarta-feira'
    if diaSemana == 4:
        diaSemanaTexto = 'Quinta-feira'
    if diaSemana == 5:
        diaSemanaTexto = 'Sexta-feira'
    if diaSemana == 6:
        diaSemanaTexto = 'Sábado'
    if diaSemana == 7:
        diaSemanaTexto = 'Domingo'

    if qtdConvidadosExcedentes == 0:
        print(f"{lotacaoMaximaPandemia} pessoas são permitidas na casa de eventos em {diaSemanaTexto}. Você não excedeu esse limite. ")
    if qtdConvidadosExcedentes > 0:
        print(f"{lotacaoMaximaPandemia} pessoas são permitidas na casa de eventos em {diaSemanaTexto}. Você excedeu em {qtdConvidadosExcedentes} pessoas esse limite.")


diaSemana = inputDiaSemana()
qtdConvidados = inputQtdConvidados()
lotacaoMaximaPandemia = calculaLotacaoPandemia(diaSemana)
qtdConvidadosExcedentes = calculaConvidadosExcedentes(lotacaoMaximaPandemia, qtdConvidados)
printaMensagemExcedentes(lotacaoMaximaPandemia, qtdConvidadosExcedentes)
