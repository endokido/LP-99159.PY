

import os
os.system('cls')


# Solicitando a quantidade e o preço das maçãs. 
macas = int(input('Quantidade de maçãs: '))
#valor = float(input('Preço das maçãs: '))

#valor_total = valor * macas

valor_total = 1.30 * macas
valor_total = 1.00 * macas

print(f'Quantodade de maçãs {macas}')
print(f'Preço unitário: {1.30 if macas < 12 else 1.00}')
print(f'Valor total: {valor_total}')