def inputTemperatura():
    try:
        return float(input("Insira a temperatura em fahrenheit: "))
    except ValueError:
        print("Somente numeros.")
        exit()

def validaTemperatura(temperatura):
    if temperatura < -459.67:
        return False
    else:
        return True

def converteFahrenheitToCelsius(temperatura):
    return 5 * ((temperatura -32) /9)

def printaTemperaturaCelsius(temperaturaCelsius):
    print(f"a temperatura em °C é " + ("%.2f" % temperaturaCelsius))

temperatura = inputTemperatura()

if validaTemperatura(temperatura):
    temperaturaCelsius = converteFahrenheitToCelsius(temperatura)
    printaTemperaturaCelsius(temperaturaCelsius)
else:
    print("Esta temperatura excede o zero absoluto (-459.67F), logo é inválida.")