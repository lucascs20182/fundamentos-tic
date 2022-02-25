# Os preços das mercadorias expostas apresentam descontos diferenciados.
# Programa para ler o valor da compra e o percentual do desconto
# e imprimir a seguinte mensagem: "PARA xx.xx % DE DESCONTO O VALOR É R$ yy.yy"

def criarMensagemDoJeitoPythonicoHahah(valorCompra, percentualDesconto):
    valorComDesconto = valorCompra - (valorCompra * percentualDesconto) / 100

    return f'PARA {"%.2f" % percentualDesconto} % DE DESCONTO O VALOR É R$ {"%.2f" % valorComDesconto}'

#start point do programa
if __name__ == '__main__':
    valorCompra = float(input('Entre com o valor da compra: '))
    percentualDesconto = float(input('Entre com o percentual do desconto: '))

    print(criarMensagemDoJeitoPythonicoHahah(valorCompra, percentualDesconto))
