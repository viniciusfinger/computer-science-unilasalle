from Livro import Livro
from Editora import Editora

editoraTest = Editora(1, "Editora Test", "Vinicius", "983043447")
editoraSegunda = Editora(2, "Editora Segunda", "André", "999999999")

livroConto = Livro(1, "Um conto de terror baseado em fatos reais", 1342423, editoraTest)
livroTecnico = Livro(2, "Arquitetura Limpa: uma introdução a arquitetura de software", 109444, editoraSegunda)

print("Livro de conto: ")
print("Id: {}, Código ISBN: {}, Editora: {}, Descrição: {}".format(livroConto.codigo, livroConto.codigoISBN ,livroConto.editora.razaoSocial, livroConto.descricao))
print("Contato {}(Cód.: {}):".format(livroConto.editora.razaoSocial, livroConto.editora.codigo))
print("Responsável: {}, Fone: {}".format(livroConto.editora.nomeContato, livroConto.editora.telefone))
print("------------------------")
print("Livro técnico:")
print("Id: {}, Código ISBN: {}, Editora: {}, Descrição: {}".format(livroTecnico.codigo, livroTecnico.codigoISBN, livroTecnico.editora.razaoSocial, livroTecnico.descricao))
print("Contato {}(Cód.: {}):".format(livroTecnico.editora.razaoSocial, livroTecnico.editora.codigo))
print("Responsável: {}, Fone: {}".format(livroTecnico.editora.nomeContato, livroTecnico.editora.telefone))

