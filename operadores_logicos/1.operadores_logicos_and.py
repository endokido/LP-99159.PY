import os
os.system('cls')

nota = 12

# Se nota maior ou igual que zero e 
# nota menor e igual que 10.
# AND -> Dentro de um intervalo definido
if nota >= 0 and nota <= 10:
    print('Nota inválida')
else:
    print(f"Nota: {nota}")