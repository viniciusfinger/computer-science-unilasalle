#Vinícius Finger - 201920133


def encerraPrograma():
    print("Somente números inteiros e positivos.")
    exit()


i = 0
qtdSim = 0
qtdNao = 0

try:
    quantidadeParticipantes = int(input("Insira a quantidade de participantes da pesquisa: "))
    if quantidadeParticipantes <= 0:
        encerraPrograma()
except ValueError:
    encerraPrograma()

while i < quantidadeParticipantes:
    voto = int(input("Você gostou? Digite 1 para SIM ou 0 para NÃO: "))
    if voto not in (0, 1):
        print("somente 0 ou 1.")
        exit()
    if voto == 1:
        qtdSim += 1
    if voto == 0:
        qtdNao += 1
    i += 1

porcentSim = ((100 * qtdSim) / quantidadeParticipantes)
porcentNao = (100 - porcentSim)

print(f"Sim: {qtdSim} Não: {qtdNao}")
print(f"{porcentSim}% gostaram, {porcentNao}% não gostaram.")
