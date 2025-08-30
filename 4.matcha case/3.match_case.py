import os
os.system('cls')

num_1 = int(input('Digite o primeiro número: '))
operadores = input('Dgite o operador (+, -, *, /): ')
num_2 = int(input('Digite o segundo número: '))

match operadores:
    case '+':
        soma = num_1 + num_2
        print(f"Resultado de {num_1} + {num_2} = {soma}")
    case '-':
        subtracao = num_1 - num_2
        print(f"Resultado de {num_1} - {num_2} = {subtracao}")
    case '*':
        multiplicacao = num_1 * num_2
        print(f'Resultado de {num_1} * {num_2} = {multiplicacao}')
    case '/':
        divisao = num_1 / num_2
        if num_2 != 0:
            print(f'Resuldade de {num_1} / {num_2} = {divisao}')
        else:
            print('Erro! Não é possível dividir por zero.')
    case _:
        print('Operador inválido')
            