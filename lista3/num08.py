# Programa que registre diferentes notas de alunos de uma mesma turma.
# Ao ser digitado o valor 0 o programa é interrompido e apresenta a média das notas informadas.

if __name__ == '__main__':
    notas = []
    nota = float(input('Entre com a nota de um aluno: '))
    media = 0

    while(nota != 0):
        notas.append(nota)
        nota = float(input('Entre com a nota do próximo aluno: '))

    for i in notas:
        media += i

    media /= len(notas)

    print(f'A média das notas informadas é {media}')
