def converteHora(hora, minutos):
    if hora < 0 or hora > 24:
        print("Hora inválida.")
        return
    if hora > 12:
        horaFormatada = hora - 12
    if hora <= 12:
        print(f"{hora}:{minutos} A.M")
    else:
        print(f"{horaFormatada}:{minutos} P.M")


hora = int(input("insira a hora: "))
minutos = int(input("insira os minutos: "))
converteHora(hora, minutos)
