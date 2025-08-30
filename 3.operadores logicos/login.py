import os
os.system('cls')

# Simulando um login

# Dados do banco de dados
usuario = 'Wesley'
senha = '1234'

# Dados do usuário (ENTADA DE DADOS)
input_usuario = input('Usuário: ')
input_senha = input('Senha: ')

# Verificando se o usuário e a senha estão corretos

if usuario == input_usuario and senha == input_senha:
    print('Login realizado com sucesso!') # Se o usuario é igual ao input_usuario E a senha é igual ao input_senha: print('Login realizado com sucesso!')
else:
    print('Usuário ou senha inválida!') # Senão: print('Usuário ou senha inválida!')