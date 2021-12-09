from pedidos import pedidos
from time import sleep as s
def telaPrincipal():
    print('''####### LANCHONETE ######
# 1 - INCLUIR PEDIDO    # 
# 2 - ATENDER PEDIDO    #
# 3 - LISTAR PEDIDOS    #
# 4 - PESQUISAR PEDIDOS #
# 5 - ENCERRAR          #
#########################''')
    menu = str(input('Sua escolha: ').strip())
    if menu.isdigit():
        while True:
            if menu != '1' and menu != '2' and menu != '3' and menu != '4' and menu != '5':
                print(f'Opção não encontrada!')
                telaPrincipal()
            break
        if menu == '1':
            from pedidos import sistemaIncluirPedido
            sistemaIncluirPedido()
        if menu == '2':
            from pedidos import sistemaAtenderPedidos
            sistemaAtenderPedidos()
        if menu == '3':
            from pedidos import sistemaListarPedidos
            sistemaListarPedidos()
        if menu == '4':
            from pedidos import sistemaPesquisarPedidos
            sistemaPesquisarPedidos()
        if menu == '5':
            if len(pedidos) > 0:
                print('Ainda possuem pedidos a serem atendidos.')
                from pedidos import sistemaAtenderPedidos
                sistemaAtenderPedidos()
            else:
                print('ENCERRANDO', end=''); s(1); print('.', end=''); s(1); print('.', end=''); s(1); print('.')
                s(1)
                from faturamento import sistemaFaturamento
                sistemaFaturamento()
                s(1)
                print('##PROGRAMA ENCERRADO##')
                quit()
    else:
        print(f'Digite apenas valores númericos.')
        telaPrincipal()


telaPrincipal()