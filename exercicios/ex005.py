import os
os.system('cls')

primeiro_numero = int(input('Primeiro número: '))
segundo_numero = int(input('Segundo número: '))

soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero

media = soma / 2

if primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
else:
    maior = segundo_numero
    menor = primeiro_numero

print(f'Soma: {soma}')
print(f'Produto: {produto}')
print(f'Média: {media}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')

# VERIFICANDO SE OS NÚMEROS IFNORMADO PELO USUÁRIO SÃO IGUAIS!

if primeiro_numero == segundo_numero:
    print('Ambos os números informado pelo usuário são iguais!')
