# Uma empresa concederá um aumento de salário aos funcionários
# que possuirem mais de 4 anos de serviço,
# mais de 3 dependentes e salário atual abaixo de R$500,00.
# Este programa recebe como input esses dados de um funcionário
# e imprime uma mensagem dizendo se o funcionário tem direito ao aumento ou não.
# Caso ele tenha este direito, o programa calcula o novo salário com 40% de aumento
# e mostra o salário antigo, o novo salário e a diferença.

def calcularNovoSalario(salarioAntigo):
    novoSalario = salarioAntigo + (salarioAntigo * 0.4)

    return (
        f'Salário antigo: {"%.2f" % salarioAntigo}\nNovo salário: {"%.2f" % novoSalario}'
        + f'\nDiferença entre os salários: {"%.2f" % (novoSalario - salarioAntigo)}'
    )

def verificarSeFuncionarioTemDireitoAUmAumento(dadosFuncionario):
    direitoAUmAumento = (
        True if dadosFuncionario["anos de serviço"] > 4
        and dadosFuncionario["número de dependentes"] > 3
        and dadosFuncionario["salário atual"] < 500
        else False
    )

    if(direitoAUmAumento):
        print('\nFuncionário tem direito ao aumento.')
        print(calcularNovoSalario(dadosFuncionario["salário atual"]))
    else:
        print('Funcionário NÃO tem direito ao aumento.')

#start point do programa
if __name__ == '__main__':
    dadosFuncionario = {}

    print('Entre com os dados do funcionário')
    dadosFuncionario["anos de serviço"] = int(input('Anos de serviço: '))
    dadosFuncionario["número de dependentes"] = int(input('Número de dependentes: '))
    dadosFuncionario["salário atual"] = float(input('Salário atual: '))

    verificarSeFuncionarioTemDireitoAUmAumento(dadosFuncionario)
