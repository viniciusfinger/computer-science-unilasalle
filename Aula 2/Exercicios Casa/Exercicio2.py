try:
    num1 = float(input("Insira um numero: "))
    num2 = float(input("Insira outro numero: "))
except ValueError:
    print("Somente numeros.")
    exit()
numMult = num1 * num2
print("A multiplicacao de",num1,"por",num2,"eh",numMult)