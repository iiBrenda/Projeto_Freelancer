import tkinter as tk
from tkinter import ttk, messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Freelancer")
        self.root.geometry("800x600")

        self.clientes = []
        self.freelancers = []
        self.servicos = []

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        self.create_freelancer_tab()
        self.create_cliente_tab()
        self.create_servico_tab()
        self.create_relatorios_tab()

    def create_freelancer_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Freelancers")

        # Nome
        ttk.Label(tab, text="Nome:").pack()
        self.nome_freelancer = ttk.Entry(tab)
        self.nome_freelancer.pack()

       
        # Contato (novo)
        ttk.Label(tab, text="Contato:").pack()
        self.contato_freelancer = ttk.Entry(tab)
        self.contato_freelancer.pack()

        # Área de atuação
        ttk.Label(tab, text="Área de Atuação:").pack()
        self.habilidade_freelancer = ttk.Entry(tab)
        self.habilidade_freelancer.pack()

        ttk.Button(tab, text="Cadastrar Freelancer", command=self.cadastrar_freelancer).pack(pady=5)

        self.lista_freelancers = tk.Listbox(tab)
        self.lista_freelancers.pack(expand=True, fill='both')

        ttk.Button(tab, text="Remover Freelancer", command=self.remover_freelancer).pack(pady=5)

    def create_cliente_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Clientes")

        # Nome
        ttk.Label(tab, text="Nome:").pack()
        self.nome_cliente = ttk.Entry(tab)
        self.nome_cliente.pack()

       
        # Contato (novo)
        ttk.Label(tab, text="Contato:").pack()
        self.contato_cliente = ttk.Entry(tab)
        self.contato_cliente.pack()

        # Email 
        ttk.Label(tab, text="Email:").pack()
        self.email_cliente = ttk.Entry(tab)
        self.email_cliente.pack()

        ttk.Button(tab, text="Cadastrar Cliente", command=self.cadastrar_cliente).pack(pady=5)

        self.lista_clientes = tk.Listbox(tab)
        self.lista_clientes.pack(expand=True, fill='both')

        ttk.Button(tab, text="Remover Cliente", command=self.remover_cliente).pack(pady=5)

    def create_servico_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Serviços")

        # Descrição
        ttk.Label(tab, text="Descrição:").pack()
        self.descricao_servico = ttk.Entry(tab)
        self.descricao_servico.pack()

        # Valor
        ttk.Label(tab, text="Valor (R$):").pack()
        self.valor_servico = ttk.Entry(tab)
        self.valor_servico.pack()

        # Data de entrega (novo)
        ttk.Label(tab, text="Data de Entrega (YYYY-MM-DD):").pack()
        self.data_servico = ttk.Entry(tab)
        self.data_servico.pack()

        # Combobox para Cliente (novo)
        ttk.Label(tab, text="Cliente:").pack()
        self.cb_cliente = ttk.Combobox(tab, values=[c[0] for c in self.clientes])
        self.cb_cliente.pack()

        # Combobox para Freelancer (novo)
        ttk.Label(tab, text="Freelancer:").pack()
        self.cb_freelancer = ttk.Combobox(tab, values=[f[0] for f in self.freelancers])
        self.cb_freelancer.pack()

        ttk.Button(tab, text="Registrar Serviço", command=self.cadastrar_servico).pack(pady=5)

        self.lista_servicos = tk.Listbox(tab)
        self.lista_servicos.pack(expand=True, fill='both')

        ttk.Button(tab, text="Concluir Serviço", command=self.concluir_servico).pack(pady=2)
        ttk.Button(tab, text="Editar Serviço", command=self.editar_servico).pack(pady=2)
        ttk.Button(tab, text="Remover Serviço", command=self.remover_servico).pack(pady=2)

    def create_relatorios_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Relatórios")

        # Botões de relatório 
        ttk.Button(tab, text="Listar Serviços", 
                  command=lambda: messagebox.showinfo("Serviços", self.listar_servicos())).pack(pady=10)
        
        ttk.Button(tab, text="Listar Freelancers", 
                  command=lambda: messagebox.showinfo("Freelancers", self.listar_freelancers())).pack(pady=10)
        
        ttk.Button(tab, text="Listar Clientes", 
                  command=lambda: messagebox.showinfo("Clientes", self.listar_clientes())).pack(pady=10)

    def cadastrar_freelancer(self):
        nome = self.nome_freelancer.get()
        documento = self.doc_freelancer.get()
        contato = self.contato_freelancer.get()
        area = self.habilidade_freelancer.get()
        
        if nome and documento and contato and area:
            self.freelancers.append((nome, documento, contato, area))
            self.lista_freelancers.insert(tk.END, nome)
            self.cb_freelancer['values'] = [f[0] for f in self.freelancers]
            messagebox.showinfo("Cadastro", f"Freelancer {nome} cadastrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos.")

    def cadastrar_cliente(self):
        nome = self.nome_cliente.get()
        documento = self.doc_cliente.get()
        contato = self.contato_cliente.get()
        email = self.email_cliente.get()
        
        if nome and documento and contato and email:
            self.clientes.append((nome, documento, contato, email))
            self.lista_clientes.insert(tk.END, nome)
            self.cb_cliente['values'] = [c[0] for c in self.clientes]
            messagebox.showinfo("Cadastro", f"Cliente {nome} cadastrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos.")

    def cadastrar_servico(self):
        descricao = self.descricao_servico.get()
        valor = self.valor_servico.get()
        data = self.data_servico.get()
        cliente_nome = self.cb_cliente.get()
        freelancer_nome = self.cb_freelancer.get()
        
        if descricao and valor and data and cliente_nome and freelancer_nome:
            # Encontra cliente e freelancer
            cliente = next((c for c in self.clientes if c[0] == cliente_nome), None)
            freelancer = next((f for f in self.freelancers if f[0] == freelancer_nome), None)
            
            if cliente and freelancer:
                self.servicos.append([descricao, valor, data, cliente, freelancer, False])  # False = não concluído
                self.lista_servicos.insert(tk.END, f"{descricao} - {cliente[0]} - {freelancer[0]}")
                messagebox.showinfo("Cadastro", f"Serviço '{descricao}' registrado com sucesso!")
            else:
                messagebox.showerror("Erro", "Cliente ou Freelancer não encontrado!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos.")

    def remover_freelancer(self):
        selecionado = self.lista_freelancers.curselection()
        if selecionado:
            self.lista_freelancers.delete(selecionado)
            del self.freelancers[selecionado[0]]
            self.cb_freelancer['values'] = [f[0] for f in self.freelancers]

    def remover_cliente(self):
        selecionado = self.lista_clientes.curselection()
        if selecionado:
            self.lista_clientes.delete(selecionado)
            del self.clientes[selecionado[0]]
            self.cb_cliente['values'] = [c[0] for c in self.clientes]

    def concluir_servico(self):
        selecionado = self.lista_servicos.curselection()
        if selecionado:
            idx = selecionado[0]
            self.servicos[idx][5] = True  # Marca como concluído
            item = self.lista_servicos.get(idx)
            self.lista_servicos.delete(idx)
            self.lista_servicos.insert(idx, item + " (Concluído)")

    def editar_servico(self):
        selecionado = self.lista_servicos.curselection()
        if selecionado:
            idx = selecionado[0]
            nova_desc = self.descricao_servico.get()
            novo_valor = self.valor_servico.get()
            nova_data = self.data_servico.get()
            if nova_desc and novo_valor and nova_data:
                self.servicos[idx][0] = nova_desc
                self.servicos[idx][1] = novo_valor
                self.servicos[idx][2] = nova_data
                self.lista_servicos.delete(idx)
                status = " (Concluído)" if self.servicos[idx][5] else ""
                self.lista_servicos.insert(idx, f"{nova_desc} - {self.servicos[idx][3][0]} - {self.servicos[idx][4][0]}{status}")

    def remover_servico(self):
        selecionado = self.lista_servicos.curselection()
        if selecionado:
            self.lista_servicos.delete(selecionado)
            del self.servicos[selecionado[0]]

    def listar_servicos(self):
        return [f"{s[0]} - Cliente: {s[3][0]} - Freelancer: {s[4][0]} - Valor: R${s[1]} - Data: {s[2]}" for s in self.servicos]

    def listar_freelancers(self):
        return [f"{f[0]} - {f[3]} - Contato: {f[2]}" for f in self.freelancers]

    def listar_clientes(self):
        return [f"{c[0]} - Email: {c[3]} - Contato: {c[2]}" for c in self.clientes]

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
