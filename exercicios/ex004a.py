# ALGORITMOS DIFERENTES COM OS MESMOS RESULTADOS!

import os
os.system('cls')
# Solicitando dados (ENTADA)
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
# Realizando cálculo (PROCESSAMENTO)
soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero
media = (primeiro_numero + segundo_numero) / 2

menor = min(primeiro_numero, segundo_numero)
maior = max(primeiro_numero, segundo_numero)
# Exibindo dados (SAÍDA)
print(soma)
print(produto)
print(media)
print(maior)
print(menor)