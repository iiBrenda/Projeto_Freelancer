import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from tkinter import messagebox

def iniciar_interface(sistema):
    app = tk.Tk()
    app.title("Gerenciador de Freelancers")
    app.geometry("700x500")

    style = Style("cosmo")
    aba = ttk.Notebook(app)

    frame_freelancer = ttk.Frame(aba)
    frame_cliente = ttk.Frame(aba)
    frame_servico = ttk.Frame(aba)
    frame_listagem = ttk.Frame(aba)

    aba.add(frame_freelancer, text='Cadastrar Freelancer')
    aba.add(frame_cliente, text='Cadastrar Cliente')
    aba.add(frame_servico, text='Criar Serviço')
    aba.add(frame_listagem, text='Relatórios')
    aba.pack(expand=True, fill='both')

    def atualizar_opcoes():
        cb_cliente['values'] = [c.nome for c in sistema.clientes]
        cb_freelancer['values'] = [f.nome for f in sistema.freelancers]

    # Freelancer
    ttk.Label(frame_freelancer, text="Nome:").pack()
    nome_f = ttk.Entry(frame_freelancer)
    nome_f.pack()

    ttk.Label(frame_freelancer, text="CPF/CNPJ:").pack()
    doc_f = ttk.Entry(frame_freelancer)
    doc_f.pack()

    ttk.Label(frame_freelancer, text="Contato:").pack()
    contato_f = ttk.Entry(frame_freelancer)
    contato_f.pack()

    ttk.Label(frame_freelancer, text="Área de Atuação:").pack()
    area_f = ttk.Entry(frame_freelancer)
    area_f.pack()

    def salvar_freelancer():
        sistema.cadastrar_freelancer(nome_f.get(), doc_f.get(), contato_f.get(), area_f.get())
        atualizar_opcoes()
        messagebox.showinfo("Sucesso", "Freelancer cadastrado!")

    ttk.Button(frame_freelancer, text="Salvar", command=salvar_freelancer).pack(pady=10)

    # Cliente
    ttk.Label(frame_cliente, text="Nome:").pack()
    nome_c = ttk.Entry(frame_cliente)
    nome_c.pack()

    ttk.Label(frame_cliente, text="CPF/CNPJ:").pack()
    doc_c = ttk.Entry(frame_cliente)
    doc_c.pack()

    ttk.Label(frame_cliente, text="Contato:").pack()
    contato_c = ttk.Entry(frame_cliente)
    contato_c.pack()

    def salvar_cliente():
        sistema.cadastrar_cliente(nome_c.get(), doc_c.get(), contato_c.get())
        atualizar_opcoes()
        messagebox.showinfo("Sucesso", "Cliente cadastrado!")

    ttk.Button(frame_cliente, text="Salvar", command=salvar_cliente).pack(pady=10)

    # Serviço
    ttk.Label(frame_servico, text="Descrição:").pack()
    desc = ttk.Entry(frame_servico)
    desc.pack()

    ttk.Label(frame_servico, text="Valor (R$):").pack()
    valor = ttk.Entry(frame_servico)
    valor.pack()

    ttk.Label(frame_servico, text="Data de Entrega (YYYY-MM-DD):").pack()
    data = ttk.Entry(frame_servico)
    data.pack()

    ttk.Label(frame_servico, text="Cliente:").pack()
    cb_cliente = ttk.Combobox(frame_servico, values=[])
    cb_cliente.pack()

    ttk.Label(frame_servico, text="Freelancer:").pack()
    cb_freelancer = ttk.Combobox(frame_servico, values=[])
    cb_freelancer.pack()

    def salvar_servico():
        cli = next((c for c in sistema.clientes if c.nome == cb_cliente.get()), None)
        free = next((f for f in sistema.freelancers if f.nome == cb_freelancer.get()), None)
        if cli and free:
            sistema.criar_servico(desc.get(), float(valor.get()), data.get(), cli, free)
            messagebox.showinfo("Sucesso", "Serviço criado!")

    ttk.Button(frame_servico, text="Criar Serviço", command=salvar_servico).pack(pady=10)

    # Relatórios
    ttk.Button(frame_listagem, text="Listar Serviços", command=lambda:
               messagebox.showinfo("Serviços", "\n\n".join(sistema.listar_servicos()))).pack(pady=10)

    ttk.Button(frame_listagem, text="Listar Freelancers", command=lambda:
               messagebox.showinfo("Freelancers", "\n".join(sistema.listar_freelancers()))).pack(pady=10)

    ttk.Button(frame_listagem, text="Listar Clientes", command=lambda:
               messagebox.showinfo("Clientes", "\n".join(sistema.listar_clientes()))).pack(pady=10)

    atualizar_opcoes()
    app.mainloop()
