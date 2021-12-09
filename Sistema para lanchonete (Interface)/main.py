from tkinter import *

lanches = [{"Nome_Produto": "BigMac",
           "Preco_Produto": 16.90},
           {"Nome_Produto": "X-Tudo",
            "Preco_Produto": 22.50},
           {"Nome_Produto": "Coca Cola",
            "Preco_Produto": 8},
           {"Nome_Produto": "Fanta",
            "Preco_Produto": 4},
           {"Nome_Produto": "Quarteirão",
            "Preco_Produto": 18.90},
           {"Nome_Produto": "Batata Frita",
            "Preco_Produto": 3}]

valor_total = {}
pedidos = []
pedido = []
controle_pedidos = []

def telaPrincipal():
    telaInicial = Tk()
    telaInicial.geometry('350x260')
    telaInicial.title('Lanchonete')

    label = LabelFrame(telaInicial, text='Menu Principal', padx=5, pady=5)
    label.pack(padx=10, pady=10, ipady=10, ipadx=10)

    botaoIncluirPedido = Button(label, text='Incluir Pedidos', width=15, height=2, command=lambda: [fechar(telaInicial), incluirPedidos()])
    botaoIncluirPedido.pack()

    botaoAtenderPedido = Button(label, text='Atender Pedidos', width=15, height=2, command=lambda: [fechar(telaInicial), atenderPedidos()])
    botaoAtenderPedido.pack()

    botaoListarPedido = Button(label, text='Listar Pedidos', width=15, height=2, command=lambda: [fechar(telaInicial), listarPedidos()])
    botaoListarPedido.pack()

    botaoPesquisarPedido = Button(label, text='Pesquisar Pedidos', width=15, height=2, command=lambda: [fechar(telaInicial), pesquisarPedidos()])
    botaoPesquisarPedido.pack()

    botaoEncerrar = Button(label, text='Encerrar', width=15, height=2, command=lambda: fechar(telaInicial))
    botaoEncerrar.pack()

    telaInicial.mainloop()

def incluirPedidos():
    telaIncluirPedido = Tk()
    telaIncluirPedido.geometry('260x400')
    telaIncluirPedido.title('Incluir Pedido')

    titulo = Label(telaIncluirPedido, text='###Incluir Pedido###', padx=10, pady=10, justify='center')
    titulo.pack()

    produtos = LabelFrame(telaIncluirPedido, text='Produtos', padx=5, pady=5)
    produtos.pack(padx=10, pady=10, ipady=10, ipadx=10)

    produto_1 = Button(produtos, text='BigMac - R$ 16,90', width=20, height=2, command=lambda: [pegarBigMac()])
    produto_1.pack()

    produto_2 = Button(produtos, text='X-Tudo - R$ 22,50', width=20, height=2, command=lambda: [pegarXTudo()])
    produto_2.pack()

    produto_3 = Button(produtos, text='Coca Cola - R$ 8,00', width=20, height=2, command=lambda: [pegarCocaCola()])
    produto_3.pack()

    produto_4 = Button(produtos, text='Fanta - R$ 4,00', width=20, height=2, command=lambda: [pegarFanta()])
    produto_4.pack()

    produto_5 = Button(produtos, text='Quarteirão - R$ 18,90', width=20, height=2, command=lambda: [pegarQuarteirao()])
    produto_5.pack()

    produto_6 = Button(produtos, text='Batata Frita - R$ 3,00', width=20, height=2, command=lambda: [pegarBatataFrita()])
    produto_6.pack()

    encerrarPedido = Button(telaIncluirPedido, text='Finalizar Pedido', command=lambda: [finalizarPedido(), fechar(telaIncluirPedido), telaPrincipal()])
    encerrarPedido.pack()

    telaIncluirPedido.mainloop()

def pegarBigMac():
    pedido.append(dict(lanches[0]))
    telaConfirmacao()

def pegarXTudo():
    pedido.append(dict(lanches[1]))
    telaConfirmacao()

def pegarCocaCola():
    pedido.append(dict(lanches[2]))
    telaConfirmacao()

def pegarFanta():
    pedido.append(dict(lanches[3]))
    telaConfirmacao()

def pegarQuarteirao():
    pedido.append(dict(lanches[4]))
    telaConfirmacao()

def pegarBatataFrita():
    pedido.append(dict(lanches[5]))
    telaConfirmacao()

def telaConfirmacao():
    soma = 0
    for i in range(len(pedido)):
        soma = pedido[i]["Preco_Produto"] + soma
    telaConfirmacao = Tk()
    confirma = Label(telaConfirmacao, text=f'{pedido[len(pedido)-1]["Nome_Produto"]} - R$ {pedido[len(pedido)-1]["Preco_Produto"]:.2f}\n Adicionado com sucesso')
    confirma.pack()
    preco_atual = Label(telaConfirmacao, text=f'Total do Pedido: R$ {soma:.2f}')
    preco_atual.pack()
    certo = Button(telaConfirmacao, text='Fechar', command=lambda:[fechar(telaConfirmacao)], width=20, height=2)
    certo.pack()
    telaConfirmacao.mainloop()

def finalizarPedido():
    if len(pedido) > 0:
        v1 = 0
        vf = 0
        for i in range(len(pedido)):
            v1 = pedido[i]["Preco_Produto"]
            vf = v1 + vf
            valor_total["Valor_Total"] = vf
        pedido.insert(0, dict(valor_total))
        valor_total.clear()
        pedidos.append(pedido[:])
        controle_pedidos.append(pedidos[:])
        pedido.clear()
        v1 = 0
        vf = 0

    print(pedidos, len(pedidos))



def atenderPedidos():
    if len(pedidos) == 0:
        telaAtenderPedidos = Tk()
        telaAtenderPedidos.geometry('200x200')
        telaAtenderPedidos.title('Atender Pedido')
        msg = LabelFrame(telaAtenderPedidos, text='Não há pedidos cadastrados')
        msg.pack(ipady=5, ipadx=5)
        retorno = Button(msg, text='Retornar ao menu principal', command=lambda: [fechar(telaAtenderPedidos), telaPrincipal()], pady=10)
        retorno.pack()
        telaAtenderPedidos.mainloop()
    else:
        telaAtenderPedidos = Tk()
        telaAtenderPedidos.title('Atender Pedido')
        titulo = Label(telaAtenderPedidos, text='###Atender Pedido###')
        titulo.pack()
        cont = 0

        cabeca = LabelFrame(telaAtenderPedidos, text='Pedidos', width=150, height=250, labelanchor='n')
        cabeca.pack(ipady=5)
        tituloCabeca = Label(cabeca, text=f'{"ID"} / Preço Total')
        tituloCabeca.grid(column=1, row=0)
        cont = 1
        for k, v in enumerate(pedidos):
            pedidosAtivos = Label(cabeca, text=f'{k} / {"R$":>} {v[0]["Valor_Total"]:.2f}')
            pedidosAtivos.grid(column=1, row=cont)
            cont += 1

        msg = Label(telaAtenderPedidos, text='Sua escolha \/')
        msg.pack()
        escolha = Entry(telaAtenderPedidos)
        escolha.pack(padx=15, pady=5)

        def retirarPedidoFila():
            pedidos.pop(int(escolha.get()))

        selecionarEscolha = Button(telaAtenderPedidos, text='Confirmar', command=lambda: [retirarPedidoFila(), fechar(telaAtenderPedidos), atenderPedidos()])
        selecionarEscolha.pack()

        retornarMenu = Button(telaAtenderPedidos, text='Retornar ao Menu', command=lambda: [fechar(telaAtenderPedidos), telaPrincipal()])
        retornarMenu.pack()

        telaAtenderPedidos.mainloop()

def listarPedidos():
    if len(pedidos) == 0:
        telaListarPedidos = Tk()
        telaListarPedidos.geometry('200x200')
        telaListarPedidos.title('Atender Pedido')
        msg = LabelFrame(telaListarPedidos, text='Não há pedidos cadastrados')
        msg.pack(ipady=5, ipadx=5)
        retorno = Button(msg, text='Retornar ao menu principal', command=lambda: [fechar(telaListarPedidos), telaPrincipal()], pady=10)
        retorno.pack()
        telaListarPedidos.mainloop()
    else:
        telaListarPedidos = Tk()
        telaListarPedidos.title('Incluir Pedido')
        qtd_pedidos = len(pedidos)
        cont = 1
        cont2 = 0
        coluna = 0

        main_frame = Frame(telaListarPedidos)
        main_frame.pack(fill='both', expand=1)

        my_canvas = Canvas(main_frame)
        my_canvas.pack(side='left', fill='both', expand=1)

        my_rolagem = Scrollbar(main_frame, orient='vertical', command=my_canvas.yview)
        my_rolagem.pack(side='right', fill='y')

        my_canvas.configure(yscrollcommand=my_rolagem.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

        second_frame = Frame(my_canvas)

        my_canvas.create_window((0, 0), window=second_frame, anchor='nw')

        topo = LabelFrame(second_frame, text='Pedidos', labelanchor='n')
        topo.pack()

        while True:
            parte_cima = Label(topo, text=f'{"Nome do Produto":<15} {"Valor":>20}')
            parte_cima.pack()
            while True:
                detalhes = Label(topo, text=f'{pedidos[cont2][cont]["Nome_Produto"]:<35}  {"R$"} {pedidos[cont2][cont]["Preco_Produto"]:.2f}')
                detalhes.pack()
                cont += 1
                if len(pedidos[cont2]) == cont:
                    cont = 1
                    break
            detalhesTotal = Label(topo, text=f'\n{"Valor Total":<20}  {"R$":>5} {pedidos[cont2][0]["Valor_Total"]:.2f}')
            detalhesTotal.pack()
            linha = Label(topo, text='-' * 50)
            linha.pack()
            cont2 += 1
            if qtd_pedidos == cont2:
                break

        retorno = Button(telaListarPedidos, text='Retornar ao menu principal', command=lambda: [fechar(telaListarPedidos), telaPrincipal()], pady=10)
        retorno.pack(ipadx=10, pady=10)

        telaListarPedidos.mainloop()

def pesquisarPedidos():
    if len(pedidos) == 0:
        telaPesquisarPedidos = Tk()
        telaPesquisarPedidos.geometry('200x200')
        telaPesquisarPedidos.title('Pesquisar Pedidos')
        msg = LabelFrame(telaPesquisarPedidos, text='Não há pedidos cadastrados')
        msg.pack(ipady=5, ipadx=5)
        retorno = Button(msg, text='Retornar ao menu principal', command=lambda: [fechar(telaPesquisarPedidos), telaPrincipal()], pady=10)
        retorno.pack()
        telaPesquisarPedidos.mainloop()
    else:
        telaPesquisarPedidos = Tk()
        telaPesquisarPedidos.title('Pesquisar Pedidos')

        msg_1 = Label(telaPesquisarPedidos, text='###Pesquisar Pedidos###')
        msg_1.pack()
        grupo_1 = LabelFrame(telaPesquisarPedidos)
        grupo_1.pack()

        msg_2 = Label(grupo_1, text='Digite o ID do pedido desejado abaixo')
        msg_2.pack()

        msg_3 = Label(grupo_1, text=f'Pedidos cadastradados: {len(pedidos)}')
        msg_3.pack()

        idPedido = Entry(grupo_1)
        idPedido.pack(padx=15, pady=5)

        def pedidoSolicitado():
            if int(idPedido.get()) > len(pedidos):
                pedidonEncontrado = Tk()
                pedidonEncontrado.geometry('200x200')
                pedidonEncontrado.title('Pesquisar Pedidos')
                msg = LabelFrame(pedidonEncontrado, text='Pedido não Encontrado')
                msg.pack(ipady=5, ipadx=5)
                retorno = Button(msg, text='Retornar ao menu principal',
                                 command=lambda: [fechar(pedidonEncontrado), telaPrincipal()], pady=10)
                retorno.pack()
                pedidonEncontrado.mainloop()
            else:
                telaPedidoSolicitado = Tk()
                telaPedidoSolicitado.title('Pedido Solicitado')
                cont = 1
                cont2 = 1

                topo = LabelFrame(telaPedidoSolicitado)
                topo.pack()

                while True:
                    parte_cima = Label(topo, text=f'{"Nome do Produto":<15} {"Valor":>20}')
                    parte_cima.pack()
                    while True:
                        detalhes = Label(topo,
                                             text=f'{pedidos[int(idPedido.get()) - 1][cont]["Nome_Produto"]:<35}  {"R$"} {pedidos[int(idPedido.get()) - 1][cont]["Preco_Produto"]:.2f}')
                        detalhes.pack()
                        cont += 1
                        cont2 += 1
                        if len(pedidos[int(idPedido.get()) - 1]) == cont:
                            cont = 1
                            cont2 = 1
                            break
                    detalhesTotal = Label(topo,
                                            text=f'\n{"Valor Total":<20}  {"R$":>5} {pedidos[int(idPedido.get()) - 1][0]["Valor_Total"]:.2f}')
                    detalhesTotal.pack()
                    retorno = Button(topo, text='Retornar ao menu principal',
                                         command=lambda: [fechar(telaPedidoSolicitado), fechar(telaPesquisarPedidos), telaPrincipal()], pady=10)
                    retorno.pack()
                    break
                telaPedidoSolicitado.mainloop()

        pesquisar = Button(grupo_1, text='Pesquisar', command=lambda: [pedidoSolicitado()])
        pesquisar.pack()

        telaPesquisarPedidos.mainloop()

def fechar(x):
    x.destroy()




telaPrincipal()