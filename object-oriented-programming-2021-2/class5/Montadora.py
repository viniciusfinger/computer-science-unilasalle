class Montadora:
    def __init__(self, codigo = "", estado = "", razaoSocial = ""):
        self.codigo = codigo
        self.estado = estado
        self.razaoSocial = razaoSocial
        
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
         self._codigo = codigo

    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, value):
        self._estado = value
    
    @property
    def razaoSocial(self):
        return self._razaoSocial

    @razaoSocial.setter
    def razaoSocial(self, razaoSocial):
        self._razaoSocial = razaoSocial
    