import os
os.system('cls')

macas = float(input('Quantas maçãs você deseja? '))

if macas < 12:
    valor_total = 1.30 * macas
else:
    valor_total = 1.00 * macas

print(f'Quantidade de mançãs: {macas}')

print(f'Preço unitário: {1.30 if macas < 12 else 1.00}')

print(f'Valor total: {valor_total}')
