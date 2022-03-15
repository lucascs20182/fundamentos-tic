# Programa que lê as notas de um aluno em cada questão, de uma prova de 10 questões
# Se for digitada a nota zero para uma questão, o sistema para imediatamente
# Informando a mensagem "Não aprovado".

if __name__ == '__main__':
    NUMERO_QUESTOES = 10

    for questao in range(NUMERO_QUESTOES):
        nota = float(input(f'Entre com a nota do aluno na questão {questao + 1}a: '))

        if(nota == 0):
            print("Não aprovado.")
            break
