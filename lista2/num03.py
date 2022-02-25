# Programa para ler dois valores e imprimir "EM ORDEM" caso o primeiro seja menor que o segundo
# e "FORA DE ORDEM" no caso contrário
# sugestão de enunciado/regra de negócio:
# considerar ordenado se o primeiro valor é menor OU IGUAL o segundo valor

def checarOrdenacao(valor1, valor2):
    return valor1 < valor2

#start point do programa
if __name__ == '__main__':
    valor1 = float(input('Entre com o 1º valor: '))
    valor2 = float(input('Entre com o 2º valor: '))

    if(checarOrdenacao(valor1, valor2)):
        print("EM ORDEM")
    else:
        print("FORA DE ORDEM")
