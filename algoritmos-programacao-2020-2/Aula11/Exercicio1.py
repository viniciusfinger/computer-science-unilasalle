def calculaMediaInfectados(cidades):
    total = 0

    for cidade in cidades:
        total += cidade.get("infectados")

    return total / len(cidades)


def calculaMediaObitosCidadeGrande(cidades):
    cidadesGrandes = 0
    totalObitos = 0

    for cidade in cidades:
        if cidade.get("habitantes") > 50000:
            totalObitos += cidade.get("obitos")
            cidadesGrandes += 1

    if cidadesGrandes == 0:
        return 0
    else:
        return totalObitos / cidadesGrandes


def calculaMediaObitosCidadesPequenas(cidades):
    cidadesPequenas = 0
    totalObitos = 0

    for cidade in cidades:
        if cidade.get("habitantes") <= 50000:
            totalObitos += cidade.get("obitos")
            cidadesPequenas += 1

    if cidadesPequenas == 0:
        return 0
    else:
        return totalObitos / cidadesPequenas


def printaLinha():
    print("-" * 40)


i = 0
cidades = []

while i < 3:
    cidade = {
        "nome": "",
        "habitantes": 0,
        "infectados": 0,
        "obitos": 0
    }

    printaLinha()

    nomeCidade = input("Insira o nome da cidade: ")
    cidade["nome"] = nomeCidade

    habitantes = int(input(f"Insira o número de habitantes de {nomeCidade}: "))
    cidade["habitantes"] = habitantes

    while True:

        while True:
            infectados = int(input(f"Insira o número de infectados de {nomeCidade}: "))
            if infectados < 0:
                print('\033[31m' + 'Erro: Número de infectados não pode ser menor do que zero.' + '\033[0;0m')
            else:
                break

        cidade["infectados"] = infectados

        if infectados <= habitantes:
            break
        else:
            print('\033[31m' + 'Erro: Número de infectados maior que o número de habitantes.' + '\033[0;0m')

    while True:

        while True:
            obitos = int(input(f"Insira o número de óbitos em {nomeCidade}: "))
            if obitos < 0:
                print('\033[31m' + 'Erro: Número de óbitos não pode ser menor que zero.' + '\033[0;0m')
            else:
                break

        cidade["obitos"] = obitos

        if obitos <= infectados:
            break
        else:
            print('\033[31m' + 'Erro: Número de óbitos não pode ser maior do que o número de infectados.' + '\033[0;0m')

    cidades.append(cidade.copy())
    i += 1

mediaInfectados = calculaMediaInfectados(cidades)
MediaObitosCidadesGrandes = calculaMediaObitosCidadeGrande(cidades)
MediaObitosCidadesPequenas = calculaMediaObitosCidadesPequenas(cidades)

printaLinha()
print(f"a média de infectados de todas as cidades é de {mediaInfectados}")
print(f"a média de óbitos em cidades com mais de 50.000 habitantes é de {MediaObitosCidadesGrandes}")
print(f"a média de óbitos em cidades com menos de 50.000 habitantes é de {MediaObitosCidadesPequenas}")
