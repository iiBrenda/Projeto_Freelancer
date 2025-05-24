from .pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, documento, contato):
        super().__init__(nome, documento, contato)

    def exibir_info(self):
        return f"Cliente - {super().exibir_info()}"
