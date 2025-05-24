class ExibivelMixin:
    def exibir_linha(self):
        if hasattr(self, 'nome'):
            return f"{self.nome} - {self.__class__.__name__}"
        return str(self)
