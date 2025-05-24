class Pessoa:
    def __init__(self, nome: str, documento: str, contato: str):
        self._nome = nome
        self._documento = documento
        self._contato = contato

    @property
    def nome(self):
        return self._nome

    @property
    def documento(self):
        return self._documento

    @property
    def contato(self):
        return self._contato

    def exibir_info(self):
        return f"Nome: {self.nome}, Contato: {self.contato}"
