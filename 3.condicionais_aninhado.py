# Condicioanis aninhado.

import os
os.system('cls')

idade = int(input("Digite sua idade: ")) # pedir para que o usuário digitasse sua idade.

#idade = 20

if idade >= 18:
    print("Você é maior idade")
elif idade  >= 14:
    print("Você é dolecente")
else:
    print("Você é criança")

# o que eu estou querendo dizer?
# if - se a idade for >= que 18, é maior de idade,
# elif - senão, se for >= 14, é adolecente,
# else - se não for, é menor de idade. 
