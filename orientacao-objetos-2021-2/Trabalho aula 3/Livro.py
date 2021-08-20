class Livro:
    def __init__(self, codigo, descricao, codigoISBN, editora):
        self.codigo = codigo
        self.descricao = descricao
        self.codigoISBN = codigoISBN
        self.editora = editora

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
         self._codigo = value
    
    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self, value):
        self._descricao = value
    
    @property
    def codigoISBN(self):
        return self._codigoISBN
    
    @codigoISBN.setter
    def codigoISBN(self, value):
        self._codigoISBN = value

    @property 
    def editora(self):
        return self._editora
    
    @editora.setter 
    def editora(self, value):
        self._editora = value