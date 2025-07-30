#Bot para compra da casa própria#
valor_da_casa = eval(input('Qual o valor da casa?  '))
salário = eval(input('Qual seu salário?  '))
tempo = eval(input('Em quantos meses pretende pretende pagar?  '))
taxa_de_juros = eval(input('Qual a taxa de juros?  '))
parcelas = (valor_da_casa * (1 + taxa_de_juros) **tempo) /tempo
if parcelas > salário*0.3:
    print ('Crédito negado')
elif parcelas < salário * 0.3:
    print (f'O valor fixo da parcela será {parcelas:.2f}, você tem margem para mais!')
else:
    print (f'O valor da parcela é {parcelas :.2f}')




