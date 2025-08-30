import os
os.system('cls')

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura**2) 

if imc < 18.5:
    resultado = "Abaixo do peso." 
elif imc < 25:
    resultado = "Peso ideal, parabéns!"
elif imc < 30.0:
    resultado = "Levimente acima do peso."
elif imc < 30.5:
    resultado = "Obesidade de Grau I."
elif imc < 35.5:
    resultado = "Obesidade de Grau II, severa"
elif imc < 40:
    resultado = "Obesidade de Grau III, mórbida!!"
else:
    resultado = "Obesidade de Grau III, mórbida!!"

print(f'{imc:.1f}')
print(resultado)