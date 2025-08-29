import os
os.system('cls')

login_usuraio = 'Wesley'
login_senha = '123'

usuario = input('Usuário: ')
senha = input('Senha: ')

if usuario == login_usuraio and senha == login_senha:
    print('Bem-vindo!')
else:
    print('Usuário ou senha inválida.')
