import os
os.system('cls')

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
operador = input('Dgite o operador (+, -, *, /): ')

resultado = 0

match operador:
    case '+':
        resultado = num_1 + num_2
    case '-':
        resultado = num_1 - num_2
    case '*':
        resultado = num_1 * num_2
    case '/':
        if num_2 != 0:
            resultado = num_1 / num_2
        else:
            resultado = 'Erro! Não é possível dividir por zero.'
    case _:
        resultado = 'Operador inválido!'
    
print(f'Resultado: {resultado}')