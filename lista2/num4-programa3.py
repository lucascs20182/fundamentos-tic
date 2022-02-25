# Os preços das mercadorias apresentam descontos diferenciados pela forma de pagamento.
# O programa atual recebe como entrada o tipo de pagamento e o preço da mercadoria
# e imprime o resultado com desconto de acordo com a tabela abaixo:
# Forma de pagamento   | código      | percentual
# Cartão de crédito    | 5           | -10%
# À vista              | 6           | -20%
# 3 vezes              | 7           | -5%

def calcularPrecoComDesconto(tipoPagamento, precoMercadoria):
    valorComDesconto = precoMercadoria

    if(tipoPagamento == 1):
        valorComDesconto -= precoMercadoria * 0.1

    if(tipoPagamento == 2):
        valorComDesconto -= precoMercadoria * 0.2

    if(tipoPagamento == 3):
        valorComDesconto -= precoMercadoria * 00.5

    return valorComDesconto

#start point do programa
if __name__ == '__main__':
    print('Entre com o tipo de pagamento\n1. Cartão de crédito\n2. À vista\n3. 3 vezes')
    tipoPagamento = int(input('Opção: '))

    while(tipoPagamento != 1 and tipoPagamento != 2 and tipoPagamento != 3):
        print('Opção inválida. Tente novamente!')
        tipoPagamento = int(input('Opção: '))

    precoMercadoria = float(input('Entre com o preço da mercadoria: '))

    print(f'Valor a ser pago: {calcularPrecoComDesconto(tipoPagamento, precoMercadoria)}')
