import os
os.system('cls')

primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))
operador = str(input('Digite um operador: '))

soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
produto = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero

match operador:
    case '+':
        print(f'O operador escolhido foi {operador}')
        print(f'O resultado de {primeiro_numero} e {segundo_numero} é igual a {soma}')
match operador:
    case '-':
        print(f'O operador escolhido foi {operador}')
        print(f'O resultado de {primeiro_numero} e {segundo_numero} é igual a {subtracao}')
match operador:
    case '*':
        print(f'O operador escolhido foi {operador}')
        print(f'O resultado de {primeiro_numero} e {segundo_numero} é igual a {produto}')
match operador:
    case '/':
        print(f'O operador escolhido foi {operador}')
        print(f'O resultado de {primeiro_numero} e {segundo_numero} é igual a {divisao}')
    case _:
        print('Error')