# EX008

# Adicionadno mais um terceiro valor; 

import os 
os.system('cls')

primeiro_numero = int(input('Digite um valor: '))
segundo_numero = int(input('Digite outro valor: '))
terceiro_numero = int(input('Digite mais um valor: '))


if primeiro_numero == segundo_numero == terceiro_numero:
    print('Ambos os números são iguais')
else:
    maior = max(primeiro_numero, segundo_numero, terceiro_numero)
    menor = min(primeiro_numero, segundo_numero, terceiro_numero)

    print(f'{maior} é maior')
    print(f'{menor} é menor')