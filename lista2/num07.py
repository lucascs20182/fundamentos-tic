# Programa que recebe como entrada três valores representando as notas de um aluno
# e informa a situação do aluno: Aprovado, Reprovado ou Prova Final.
# Considere:
# APROVADO - nota maior ou igual a 6;
# PROVA FINAL - nota entre 4 e 5.9;
# REPROVADO – nota menor que 4.

def verificarSituacaoDoAluno(notasAluno):
    media = sum(i for i in notasAluno) / len(notasAluno)

    if(media >= 6):
        return 'Aprovado'
    elif(media >= 4 and media <= 5.9):
        return 'Prova Final'
    else:
        return 'Reprovado'

#start point do programa
if __name__ == '__main__':
    notasAluno = []
    contador = 1

    while(contador <= 3):
        nota = float(input(f'Entre com a {contador}ª nota: '))
        notasAluno.append(nota)
        contador += 1

    print(f'Situação do aluno: {verificarSituacaoDoAluno(notasAluno)}')
