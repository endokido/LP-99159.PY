import os
os.system("cls")

from datetime import datetime
ano_atual = datetime.now().year

matricula = int(input("Digite a sua matrícula: "))
ano_nascimento = int(input("Dgite o ano de seu nascimento: "))
tempo_trabalho = int(input("Digite o tempo de contribuíção: "))

idade = ano_atual - ano_nascimento

if tempo_trabalho > idade:
    print("ERRO: O tempo de trabalho não pode ser maior que idade")
elif idade >= 65 or  tempo_trabalho >= 30:
    print(matricula)
    print(f"Sua idade: {idade}")
    print(f"Anos de contribuíção {tempo_trabalho}")
    print("Requer aposentadoria")
elif idade <= 65 or tempo_trabalho <= 30:
    print(matricula)
    print(f"Sua idade: {idade}")
    print(f"Anos de contribuíção {tempo_trabalho}")
    print("Não requer aposentadoria")