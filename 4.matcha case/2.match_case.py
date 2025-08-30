import os
os.system('cls')

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
operador = input('Dgite o operador (+, -, *, /): ')

match operador:
    case '+':
        print(f'Resultado de {num_1} + {num_2} = {num_1 + num_2}')
    case '-':
        print(f'Rultado de {num_1} - {num_2} = {num_1 - num_2}')
    case '*':
        print(f'Resultado de {num_1} * {num_2} = {num_1 * num_2}')
    case '/':
        if num_1 or num_2 != 0:
            print(f'Resultado de {num_1} / {num_2} = {num_1 / num_2}')
        else:
            print('Erro! Não é possível dividir por zero.')      
    case _:
        print('Operador inválido!')
    