def entradaMetro():
    try:
        return(float(input("Insira quantos metros você deseja converter para centímetro: ")))
    except ValueError:
        print("somente números.")
        exit()

def converteMetroToCentimetro(metros):
    return metros * 100

def printaCentimetros(centimetros):
    print(f"{centimetros} centímetros.")


metros = entradaMetro()
centimetros = converteMetroToCentimetro(metros)
printaCentimetros(centimetros)