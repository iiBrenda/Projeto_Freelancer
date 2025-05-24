import pickle

class BancoDados:
    def __init__(self, caminho_arquivo='data/db.pkl'):
        self.caminho = caminho_arquivo

    def salvar(self, objeto):
        with open(self.caminho, 'wb') as f:
            pickle.dump(objeto, f)

    def carregar(self):
        try:
            with open(self.caminho, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return None
