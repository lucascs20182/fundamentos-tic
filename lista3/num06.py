# Programa que solicita pesos de produtos e verifica se é um peso inválido
# pesos inválidos são pesos registrados abaixo de 100 ou acima de 900 (gramas).
# O programa encerra ao ser digitado o valor "0".
# Ao encerrar, o programa exibe quantos valores inválidos foram digitados.

if __name__ == '__main__':
    peso = int(input('Entre com o peso de um produto: '))
    contadorPesosInvalidos = 0

    while(peso != 0):
        if peso < 100 or peso > 900:
            contadorPesosInvalidos += 1

        peso = int(input('Entre com o peso do próximo produto: '))

    print(f'Ao total, {contadorPesosInvalidos} valores inválidos foram digitados.')
