class Carro:
    def __init__(self, placa = "", modelo = "", anoFabricacao = ""):
        self.placa = placa
        self.modelo = modelo
        self.anoFabricacao = anoFabricacao
        
    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, placa):
         self._placa = placa

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def anoFabricacao(self):
        return self._anoFabricacao

    @anoFabricacao.setter
    def anoFabricacao(self, anoFabricacao):
        self._anoFabricacao = anoFabricacao

