class Servico:
    def __init__(self, descricao, valor, data_entrega, cliente, freelancer):
        self.descricao = descricao
        self.valor = valor
        self.status = "Pendente"
        self.data_entrega = data_entrega
        self.cliente = cliente
        self.freelancer = freelancer

    def atualizar_status(self, novo_status):
        self.status = novo_status

    def resumo(self):
        return (f"Serviço: {self.descricao}\nStatus: {self.status}\n"
                f"Valor: R${self.valor:.2f}\nEntrega: {self.data_entrega}\n"
                f"Cliente: {self.cliente.nome}\nFreelancer: {self.freelancer.nome}")
