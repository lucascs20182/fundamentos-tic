# Programa que apresenta os 7 primeiros números múltiplos de 7.

if __name__ == '__main__':
    contador = 0
    multiplosDeSete = []
    numeroAtual = 0
    output = 'M(7) = {'

    while(contador < 7):
        multiplosDeSete.append(numeroAtual)

        numeroAtual += 7
        contador += 1

    for numero in multiplosDeSete:
        output += f'{numero}, '

    output = output[0: -2]
    output += '}'

    print(output)
