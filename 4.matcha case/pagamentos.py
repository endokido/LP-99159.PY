import os
os.system('cls')

produto = float(input('Digite o valor do produto: '))

print("""
  1 - Pagamento à vista
  2 - Pagamento à prazo
""")

opcao = int(input('Digite a forma de pagamento: '))

match opcao:
    case 1:
        desconto = 10
        forma_pag ='À vista'
        desconto_real = (10 / 100) * produto
        total_a_vista = produto - ((10 / 100) * produto)
        
        print(f'Valor do produto: R${produto}')
        print(f'Forma de pagamento: {forma_pag}')
        print(f'Valor do desconto: R${desconto_real}')
        print(f'Valor a pagar: R${total_a_vista}')
    
    case 2:
        parcelas = int(input('Em quantas parcelas deseja dividir: '))
        #parcelas = 6
        forma_pag = 'À prazo'
        valor_parcela = produto / parcelas
        total_a_prazo = produto
        print('Produto: ')
        print(f'Valor do produto: R${produto}')
        print(f'Forma de pagamento: {forma_pag}')
        print(f'Valor por parcela: R${valor_parcela:.2f}')
        print(f'Valor a pagar: R${total_a_prazo}')
    case _:
        print('Erro')