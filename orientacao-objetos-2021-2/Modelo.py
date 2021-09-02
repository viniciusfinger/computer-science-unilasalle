class Modelo:
    def __init__(self, codigo = "", nome = "", montadora = ""):
        self.codigo = codigo
        self.nome = nome
        self.montadora = montadora
    
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
         self._codigo = codigo

    @property
    def nome(self):
        return self._nome
    
    @nome.setter 
    def nome(self, nome):
        self._nome = nome
    
    @property
    def montadora(self):
        return self._montadora

    @montadora.setter
    def montadora(self, montadora):
        self._montadora = montadora
    