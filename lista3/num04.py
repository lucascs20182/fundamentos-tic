# Programa que apresenta a tabuada de determinado valor informado.

if __name__ == '__main__':
    valor = int(input('Entre com um número: '))

    for numero in range(1, 11):
        print(f'{valor} x {numero} = {valor * numero}')
