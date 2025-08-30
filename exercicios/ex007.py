import os 
os.system('cls')

primeiro_numero = int(input('Digite um valor: '))
segundo_numero = int(input('Digite outro valor: '))


if primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
else:
    maior = segundo_numero
    menor = primeiro_numero

print(f'{maior} é maior')
print(f'{menor} é menor')
