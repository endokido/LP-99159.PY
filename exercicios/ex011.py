import os 
os.system('cls')

# Entrada de dados
peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))

# Processamentos de dados

# IMC (Índice de Massa Corporal)
imc = peso / (altura**2) # Calculo para IMC: Altura ao quadrado dividido pelo peso.

# Saídad de dados
print('------')
print(f'Peso: {peso}kg')
print(f'Altura: {altura}m')
print('------')
print(f'O seu IMC é {imc:.2f}')
# Estrutura Condicionais
if imc < 18.5:
    print('abaixo do peso.')

elif imc > 18.5 and imc < 24.9:
    print('Peso ideial, parabéns!')

elif imc > 25.0 and imc < 29.9:
    print('Levimente acima do peso.')

elif imc > 30.0 and imc < 34.9:
    print('Obesidade grau I')

elif imc > 35.5 and imc < 39.9:
    print('Obesidade grau II, servera!')

elif imc >= 40:
    print('Obesidade III, mórbida!!')