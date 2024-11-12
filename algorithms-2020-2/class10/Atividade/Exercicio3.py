def somaImposto(taxaImposto, custo):
    taxaImposto = taxaImposto/100
    return (taxaImposto * custo) + custo


valor = somaImposto(10, 1000)
print(f"O valor do imposto é de {valor}")
