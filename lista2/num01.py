# Programa que recebe como entrada uma distância (em Km) e o tempo de viagem (em Horas)
# e diz se a velocidade média foi superior ao limite (80 Km/h) ou não.

LIMITE_DE_VELOCIDADE = 80

def verificarSeVelocidadeMediaESuperiorAoLimite(distancia, tempo):
    return (distancia / tempo) > LIMITE_DE_VELOCIDADE

#start point do programa
if __name__ == '__main__':
    distancia = float(input('Digite uma distância (em km): '))
    tempo = float(input('Digite o tempo de viagem (em horas): '))

    if(verificarSeVelocidadeMediaESuperiorAoLimite(distancia, tempo)):
        print("A velocidade média foi superior ao limite de 80Km/h.")
    else:
        print("A velocidade média NÃO foi superior ao limite de 80Km/h.")
