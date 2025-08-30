# EX009A - CORREÇÃO OU AJUSTE

import os
os.system('cls')

macas = int(input('Quantas maçãs você deseja? '))

if macas < 12:
    valor_total = macas * 1.30
else:
    valor_total = macas * 1.00

print("")
print("VALOR TOTAL DA COMPRA")
print("----------------------")
print(f'Quantidade: {macas}')
print(f'Preço unitário: R${1.30 if macas < 12 else 1.00:.2f}')
print(f'Valor total: R${valor_total:.2f}')
