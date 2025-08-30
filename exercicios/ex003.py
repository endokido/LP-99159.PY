# Aprovado ou Reprovado?

import os
os.system('cls')

primeira_nota = float(input('Primeira nota: '))
segunda_nota = float(input('Segunda nota: '))
terceira_nota = float(input('Terceira nota: '))
print("")

media = (primeira_nota + segunda_nota + terceira_nota) / 3

if media >= 7:
    status = 'Aprovado!'
    print(f'Aprovado, sua média é de {media:.1f}')
else:
    status = 'Reprovado! 😱'
    print('Reprovado, sua médie é de {:.1f}'.format(media))

print("")

print('==VISÃO GERAL==')

print("")

print('Wesley Souza')
print(f'{media:.1f}')
print(status)


