def inputTemperatura():
    try:
        return float(input("Insira a temperatura em celsius: "))
    except ValueError:
        print("Somente numeros.")
        exit()

