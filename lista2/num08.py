# Programa que lê 3 números inteiros e mostra o maior deles

def definirMaiorValor(valor1, valor2, valor3):
    return max(valor1, valor2, valor3)

#start point do programa
if __name__ == '__main__':
    valor1 = int(input('Entre com o 1º valor inteiro: '))
    valor2 = int(input('Entre com o 2º valor inteiro: '))
    valor3 = int(input('Entre com o 3º valor inteiro: '))

    print(f'Maior valor: {definirMaiorValor(valor1, valor2, valor3)}')
