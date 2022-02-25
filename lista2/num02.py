# Programa para ler a temperatura de uma pessoa
# e exibir a mensagem "ESTÁ COM FEBRE" ou "ESTÁ NORMAL"
# considere o valor base como 36.5.

MAX_ESTADO_NAO_FEBRIL = 36.5

def checarTemperatura(temperatura):
    return temperatura > MAX_ESTADO_NAO_FEBRIL

#start point do programa
if __name__ == '__main__':
    temperatura = float(input('Entre com a temperatura da pessoa na escala Celsius: '))

    if(checarTemperatura(temperatura)):
        print("ESTÁ COM FEBRE")
    else:
        print("ESTÁ NORMAL")
