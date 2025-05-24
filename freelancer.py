from .pessoa import Pessoa

class Freelancer(Pessoa):
    def __init__(self, nome, documento, contato, area_atuacao):
        super().__init__(nome, documento, contato)
        self._area_atuacao = area_atuacao

    @property
    def area_atuacao(self):
        return self._area_atuacao

    def exibir_info(self):
        return f"Freelancer - {super().exibir_info()}, Área: {self.area_atuacao}"
