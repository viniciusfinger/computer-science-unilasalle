from Editora import Editora

'''
Não faz sentido criar "getter e setter" no python, já que não há como "privar" os seus atributos
sem ser por convenção. Ao utilizar decorators é possível colocar lógica personalizada no setter e evitar 
que um valor seja atribuido diretamente ao atributo

Exemplo do problema:

Vamos supor que a regra do nosso sistema seja que sempre que passe um ID via setter, seja manipulado ese ID e somado + 1
'''   

editora = Editora(1, "Editora Test", "Vinicius", "983043447")
editora.setId(1) #aqui o valor 1 é passado via setter e será somado 1, totalizando 2.
editora.id = 1 #aqui o valor será 1, pois não cairá na regra do setter e será jogado diretamente para o atributo.