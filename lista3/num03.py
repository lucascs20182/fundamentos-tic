# Programa que lê um valor do usuário e apresenta em seguida
# a soma de todos os números inteiros de 1 até o valor informado

if __name__ == '__main__':
    valor = int(input('Entre com um valor: '))
    soma = 0

    for numero in range(1, valor):
        soma += numero

    print(f'Soma de todos os números inteiros de 1 até {valor}: {soma}')
