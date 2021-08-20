class Editora:
    def __init__(self, codigo, razaoSocial, nomeContato, telefone):
        self.codigo = codigo
        self.razaoSocial = razaoSocial
        self.nomeContato = nomeContato
        self.telefone = telefone

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
         self._codigo = value

    @property 
    def razaoSocial(self):
        return self._razaoSocial
    
    @razaoSocial.setter
    def razaoSocial(self, value):
        self._razaoSocial = value

    @property
    def nomeContato(self):
        return self._nomeContato

    @nomeContato.setter
    def nomeContato(self, value):
        self._nomeContato = value

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, value):
        self._telefone = value
