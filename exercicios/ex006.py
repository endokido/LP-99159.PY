
import os 
os.system('cls')

# Solicitando dados (ENTADA)
idade = int(input('Digite sua idade: '))

# Tomada de decisões (CONDIÇÃO)
if idade < 16:
    print('Você não pode votar.')
elif idade > 16 and idade < 17:
    print('Seu voto é opcional.')
elif idade > 18 and idade < 65:
    print('Seu voto é obrigatório.')
else:
    print('Você não é obrigado a votar.')