# EX007A - CORREÇÃO OU AJUSTE

import os 
os.system('cls')

primeiro_numero = int(input('Digite um valor: '))
segundo_numero = int(input('Digite outro valor: '))


if primeiro_numero == segundo_numero:
    print('Ambos os números são iguais')
else:
    maior = max(primeiro_numero, segundo_numero)
    menor = min(primeiro_numero, segundo_numero)

    print(f'{maior} é maior')
    print(f'{menor} é menor')