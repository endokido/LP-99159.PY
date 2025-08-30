import os
os.system('cls')


# Solicitando dados (ENTADA)
primeiro_numero = int(input('Primeiro número: '))
segundo_numero = int(input('Segundo número: '))

# Realizando cálculo (PROCESSAMENTO)
soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero
media = soma / 2

# Tomada de decisões (CONDIÇÃO)
if primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
else:
    maior = segundo_numero
    menor = primeiro_numero

# Exibindo dados (SAÍDA)
print(f'Soma: {soma}')
print(f'Produto: {produto}')
print(f'Média: {media}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
