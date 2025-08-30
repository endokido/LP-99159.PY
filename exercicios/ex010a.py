import os
os.system('cls')

primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))

soma = primeira_nota + segunda_nota
media = soma / 2

if media >= 9:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:
    conceito = "E"

if media >= 6:
    status = "Aprovado"
else:
    status = "Reprovado"


print(media)
print('\n')
print("Sua nota é {} você está {}.".format(conceito, status))