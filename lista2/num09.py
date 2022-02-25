# Programa que efetua a leitura de três valores (A, B e C)
# relativos aos coeficientes de uma equação do segundo grau,
# calcula e apresenta as raízes desta equação.
# Se para os valores informados for possível efetuar o referido cálculo.
# Informar, também, a classificação das raízes:
# "Raízes não-reais" quando Delta < 0, "Raiz Única" quando Delta = 0 e "Raízes Distintas" quando Delta > 0

def calcularRaizes(a, b, c, raizUnica = False):
    delta = b**2 - 4 * a * c
    x1 = (-b + delta**(1/2)) / (2 * a)
    x2 = (-b - delta**(1/2)) / (2 * a)

    if(raizUnica):
        print('Valor de x1 e x2: {0}'.format(x1))
    else:
        print('Valor de x1: {0}'.format(x1))
        print('Valor de x2: {0}'.format(x2))

def verificarClassificacaoDasRaizes(a, b, c):
    delta = b**2 - 4 * a * c

    if(delta < 0):
        print('Raízes não-reais')
        return
    elif(delta == 0):
        print('Raiz Única')
        return calcularRaizes(a, b, c, True)
    else:
        print('Raízes Distintas')
        return calcularRaizes(a, b, c)

#start point do programa
if __name__ == '__main__':
    print('Entre com os coeficientes da equação de 2º grau')

    a = float(input('Entre com o valor de A: '))
    b = float(input('Entre com o valor de B: '))
    c = float(input('Entre com o valor de C: '))

    verificarClassificacaoDasRaizes(a, b, c)
