# Programa que lê valores digitados pelo usuário e informa se o valor é par ou é impar.
# O programa continua solicitando valores ao usuário até que este digite o valor "0".

if __name__ == '__main__':
    valor = int(input('Entre com um número: '))

    while(valor != 0):
        if valor % 2 == 0:
            print(f'{valor} é par.')
        else:
            print(f'{valor} é ímpar.')

        valor = int(input('Entre com um número: '))
