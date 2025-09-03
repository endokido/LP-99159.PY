import os
os.system('cls')

print('MENU')
print('-' * 40)
print("""
código \t Prato            \t Valor
 
  1    \t Picanha          \t R$25,00
  2    \t Lasanha          \t R$20.00
  3    \t Strognoff        \t R$18.00
  3    \t Bife Acebolado   \t R$20.00
  5    \t Oão com ovo      \t R#20.00
""")
print('-' * 40)
codigo = int(input('Digite o código de seu prato: '))

match codigo:
    case 1:
        print('Picanha: R$25,00')
    case 2:
        codigo = '2'
        print('Lasanha: R$20,00')
    case 3:
        codigo = '3'
        print('Strogonoff: R$18,00')
    case 4:
        codigo = '4'
        print('Bife Acebolado: 15,00')
    case 5:
        codigo = '5'
        print('Pão com ovo: R$5,00')
    case _:
        print('Este prato não existe.')
