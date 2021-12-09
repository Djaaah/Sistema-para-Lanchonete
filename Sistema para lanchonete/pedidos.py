lanches_temp = {"Nome_Produto": "",
                "Preco_Produto": ""}
lanches = {}

valor_total = {"Valor_Total": ""}
pedidos = []
pedido = []
controle_pedidos = []
soma = 0

#finalizado \/
def sistemaIncluirPedido():
    cont = 0
    soma = 0
    print('-' * 50)
    print('''####INCLUIR PEDIDO####''')
    print('-'*50)
    while True:
        lanches = lanches_temp.copy()
        lanches["Nome_Produto"] = str(input('Digite o nome do Produto: ').strip())
        preco = (input('Digite o preço do Produto: R$ '))
        testador = preco.replace('.', '')
        ve2 = testador.isnumeric()
        while True:
            if ve2:
                if preco.count('.'):
                    preco = float(preco)
                    break
                elif preco.isnumeric():
                    preco = int(preco)
                    break
            elif ve2 == False:
                print('Formato inválido')
                preco = input('Digite o preço do Produto: ')
                testador = preco.replace('.', '')
                ve2 = testador.isnumeric()
            else:
                break
        lanches["Preco_Produto"] = preco
        soma = lanches["Preco_Produto"] + soma
        pedido.append(dict(lanches))
        lanches.clear()
        while True:
            escolha = str(input('Deseja mais itens nesse pedido ?[S/N] ').upper())
            if escolha != 'S' and escolha != 'N':
                print('Opção inválida.')
            else:
                break
        if escolha == 'N':
            round(soma, 2)
            valor_total["Valor_Total"] = soma
            pedidos.append(pedido[:])
            controle_pedidos.append(pedido[:])
            controle_pedidos[len(controle_pedidos) - 1].insert(0, dict(valor_total))
            pedidos[len(pedidos) - 1].insert(0, dict(valor_total))
            pedido.clear()
            soma = 0
            while True:
                escolha = str(input('Deseja inserir mais um pedido ?[S/N] ').upper())
                if escolha != 'S' and escolha != 'N':
                    print('Opção inválida.')
                else:
                    break
            if escolha == 'S':
                sistemaIncluirPedido()
            if escolha == 'N':
                break

    from main import telaPrincipal
    telaPrincipal()

# finalizado\/
def sistemaAtenderPedidos():

    if len(pedidos) == 0:
        print('Não existem pedidos cadastrados.')
        from main import telaPrincipal
        telaPrincipal()
    else:
        print('-'*50)
        print('PEDIDOS')
        print('-' * 50)
        print(f'{"ID":<} | {"Valor Total":<}')
        for k, v in enumerate(pedidos):
            print(f'{k} - R$ {v[0]["Valor_Total"]}')
        print('-' * 50)
        escolha = int(input('Digite o número do pedido que deseja atender [999 - Menu Principal]: '))
        if escolha == 999:
            from main import telaPrincipal
            telaPrincipal()
        elif escolha > len(pedidos)-1:
            print('Pedido não encontrado!')
            sistemaAtenderPedidos()
        else:
            while True:
                final = str(input(f'Deseja mesmo atender o pedido de ID {escolha} [S/N]?').upper())
                if final != 'S' and final != 'N':
                    print('Opção inválida.')
                else:
                    break
            if final == 'S':
                print(f'Pedido de ID {escolha} removido da lista de espera.')
                print('-'*50)
                pedidos.pop(escolha)
                if len(pedidos) == 0:
                    from main import telaPrincipal
                    telaPrincipal()
                else:
                    sistemaAtenderPedidos()
            else:
                from main import telaPrincipal
                telaPrincipal()

def sistemaListarPedidos():
    cont = 1
    if len(pedidos) == 0:
        print('Não existem pedidos cadastrados.')
        from main import telaPrincipal
        telaPrincipal()
    else:
        qtd_pedidos = len(pedidos)
        cont = 1
        cont2 = 0
        while True:
            print(f'{"Nome do Produto":<20} {"Valor":>10}')
            print('-' * 50)
            while True:
                print(f'{pedidos[cont2][cont]["Nome_Produto"]:<20}  {"R$":>5} {pedidos[cont2][cont]["Preco_Produto"]:<}')
                cont += 1
                if len(pedidos[cont2]) == cont:
                    cont = 1
                    break
            print(f'\n{"Valor Total":<20}  {"R$":>5} {pedidos[cont2][0]["Valor_Total"]:<}')
            print('-' * 50)
            cont2 += 1
            if qtd_pedidos == cont2:
                break
        from main import telaPrincipal
        telaPrincipal()

def sistemaPesquisarPedidos():
    if len(pedidos) == 0:
        print('Não existem pedidos cadastrados.')
        from main import telaPrincipal
        telaPrincipal()
    else:
        cont = 1
        print(f'Número de pedidos cadastrados: {len(pedidos)}')
        while True:
            escolha = input('Digite o número do pedido que deseja visualizar: ')
            escolha.isnumeric()
            escolha = int(escolha)
            if escolha:
                if escolha > len(pedidos):
                    print('Pedido não encontrado!')
                else:
                    break
            else:
                print('Pedido não encontrado!')
        escolha -= 1
        print('-' * 50)
        print(f'{"Nome do Produto":<20} {"Valor":>10}')
        print('-' * 50)
        while True:
            print(
                f'{pedidos[escolha][cont]["Nome_Produto"]:<20}  {"R$":>5} {pedidos[escolha][cont]["Preco_Produto"]:<}')
            cont += 1
            if len(pedidos[escolha]) == cont:
                break
        print('-' * 50)
        print(f'{"Valor Total":<20}  {"R$":>5} {pedidos[escolha][0]["Valor_Total"]:<}')
        while True:
            decisao = str(input('Deseja voltar ao menu principal ? [S/N]').upper().strip())
            if decisao != 'S' and decisao != 'N':
                print('Opção inválida')
            else:
                break
        if decisao == 'S':
            from main import telaPrincipal
            telaPrincipal()
        else:
            sistemaPesquisarPedidos()