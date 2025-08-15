
import os
os.system("cls")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digte o segundo número: "))

soma = numero1 + numero2
subtrair = numero1 - numero2
multiplicar = numero1 * numero2
divisao = numero1 / numero2

print("= RESULTADO =") 
print("")
print(f"O resultado da soma é: {soma}")
print("")
print(f"O resultado da subtração é: {subtrair}")
print("") # Pula uma linha.
print(f"O resultado da multiplicação é: {multiplicar}")
print("")
print(f"O resultado da divisão é: {divisao:.2}")