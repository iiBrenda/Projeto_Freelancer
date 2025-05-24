from .freelancer import Freelancer
from .cliente import Cliente
from .servico import Servico
from .banco_dados import BancoDados

class Sistema:
    def __init__(self):
        self.db = BancoDados()
        dados = self.db.carregar()
        if dados:
            self.freelancers, self.clientes, self.servicos = dados
        else:
            self.freelancers = []
            self.clientes = []
            self.servicos = []

    def salvar_dados(self):
        self.db.salvar((self.freelancers, self.clientes, self.servicos))

    def cadastrar_freelancer(self, nome, doc, contato, area):
        f = Freelancer(nome, doc, contato, area)
        self.freelancers.append(f)
        self.salvar_dados()

    def cadastrar_cliente(self, nome, doc, contato):
        c = Cliente(nome, doc, contato)
        self.clientes.append(c)
        self.salvar_dados()

    def criar_servico(self, descricao, valor, entrega, cliente, freelancer):
        s = Servico(descricao, valor, entrega, cliente, freelancer)
        self.servicos.append(s)
        self.salvar_dados()

    def listar_servicos(self):
        return [s.resumo() for s in self.servicos]

    def listar_freelancers(self):
        return [f.exibir_info() for f in self.freelancers]

    def listar_clientes(self):
        return [c.exibir_info() for c in self.clientes]
