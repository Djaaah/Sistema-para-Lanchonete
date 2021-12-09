from pedidos import controle_pedidos
def sistemaFaturamento():
    pedidosTotais = len(controle_pedidos)
    faturamentoTotal = 0
    faturamentoMedioPorPedido = 0
    cont = 0
    if len(controle_pedidos) > 0:
        while True:
            faturamentoTotal = controle_pedidos[cont][0]["Valor_Total"] + faturamentoTotal
            cont += 1
            if pedidosTotais == cont:
                break
        faturamentoMedioPorPedido = faturamentoTotal / pedidosTotais

        print(f'Total de pedidos atendidos: {pedidosTotais}')
        print('-' * 50)
        print(f'Faturamento Total:')
        print(f'R$ - {faturamentoTotal:.2f}')
        print('-' * 50)
        print(f'Faturamento médio por pedido:')
        print(f'R$ - {faturamentoMedioPorPedido:.2f}')
    else:
        print(f'Total de pedidos atendidos: {pedidosTotais}')
        print('-' * 50)
        print(f'Faturamento Total:')
        print(f'R$ - {faturamentoTotal:.2f}')
        print('-' * 50)
        print(f'Faturamento médio por pedido:')
        print(f'R$ - {faturamentoMedioPorPedido:.2f}')