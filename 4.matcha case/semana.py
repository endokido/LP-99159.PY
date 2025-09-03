import os
os.system('cls')

dia = int(input('Digite um dia da semana: '))

match dia:
    case 1:
        dia = 'Segunda-feira'
    case 2:
        dia = 'Terça-feira'
    case 3: 
        dia = 'Quarta-feira'
    case 4:
        dia = 'Quinta-feira'
    case 5:
        dia = 'Sexta-feira'
    case 6:
        dia = 'Sábado'
    case 7:
        dia = 'Domingo'
    case _:
        print('Dia inválido!')

print(f'{dia}')