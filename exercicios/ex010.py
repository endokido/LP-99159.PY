import os
os.system('cls')

# Nome do aluno
nome = str(input('Qaul é o seu nome Wesley? '))
# Notas do aluno
primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota:'))

# PROCESSAMENTO

# expressão numérica
media = (primeira_nota + segunda_nota) / 2
# SAÍDA
print('------------')
print('BOLETIM')
print('------------')
print(f'Olá {nome}, sua média é {media}')
print('')
# Estrutura de condições
if media >= 9:
    status = 'Aprovado' 
    print(f'Sua nota é A! {status}')
elif media >= 7.5 and media < 9:
    status = 'Aprovado' 
    print(f'Sua nota é B! {status}')
elif media >= 6 and media < 7.5:
    status = 'Arpovado'
    print(f'Sua nota é C! {status}')
elif media >= 4 and media < 6:
    status = 'Reprovado'
    print(f'Sua nota é D! {status}')
else: #elif (else + if)
    if media < 4:
        status = 'Reprovado'
        print(f'Sua nota é E! {status}')
# Fim da estrutura de condiçoes.