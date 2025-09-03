import os
os.system('cls')

while True: 

    sexo = input('Qual é o seu sexo: ')
    altura = float(input('Qual é a sua altura: '))

    match sexo:
        case 'm':
            sexo = (72.7 * altura ) - 58
            print(f'Masculino: {sexo}')
            
        case 'f':
            sexo = (62.1 * altura) - 44.7
            print(f'Femnino: {sexo}')
        case _:
            print('Informação inválida')
    
    continuar = input('Deseja continuar? (s/n)').lower()
    
    if continuar != "s":
        break

print('FIM')