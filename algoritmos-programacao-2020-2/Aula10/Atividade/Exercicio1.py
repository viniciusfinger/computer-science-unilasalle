#Exercício 1 da lista de exercícios de funções da PythonBrasil

#Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def retornaNomeMes(mes):
    if mes == '01':
        return 'Janeiro'
    if mes == '02':
        return 'Fevereiro'
    if mes == '03':
        return 'Março'
    if mes == '04':
        return 'Abril'
    if mes == '05':
        return 'Maio'
    if mes == '06':
        return 'Junho'
    if mes == '07':
        return 'Julho'
    if mes == '08':
        return 'Agosto'
    if mes == '09':
        return 'Setembro'
    if mes == '10':
        return 'Outubro'
    if mes == '11':
        return 'Novembro'
    if mes == '12':
        return 'Dezembro'

def dataPorExtenso(data):
    dataSeparada = data.split('/')

    dia = dataSeparada[0]
    mes = dataSeparada[1]
    ano = dataSeparada[2]

    mes = retornaNomeMes(mes)

    return f"{dia} de {mes} de {ano}"


dataInput = input("Insira uma data no formato 'dd/MM/yyyy': ")
print(dataPorExtenso(dataInput))