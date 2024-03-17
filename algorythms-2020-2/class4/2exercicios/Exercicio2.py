# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

def inputProduto():
    print("Produtos: ")
    print("1 - Morango")
    print("2 - Maçã")
    produto = float(input("Insira o código do produto: "))
    if produto in [1,2]:
        return produto
    else:
        print("Produto não cadastrado.")
        exit()

def inputQuantidade():
    return float(input("Insira quantos Kg: "))

def calculaPreco(produto, quantidade):
    if produto == 1:
        if quantidade < 5:
            return 2.5 * quantidade
        if quantidade >= 5:
            return 2.2 * quantidade
    if produto == 2:
        if quantidade < 5:
            return 1.8 * quantidade
        if quantidade >= 5:
            return 1.5 * quantidade

def printaPreco(preco, produto, quantidade):
    if produto == 1:
        nomeProduto = "Morango"
    if produto == 2:
        nomeProduto = "Maçã"

    print(f"{quantidade}kg de {nomeProduto} custa R${preco}")


produto = inputProduto()
quantidade = inputQuantidade()
preco = calculaPreco(produto, quantidade)
printaPreco(preco, produto, quantidade)


