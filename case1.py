print ('PAGAMENTO')
print ('''    [1 - PIX]
    [2 - DÉBITO]
    [3 - CRÉDITO]  ''')
pay = int(input('ESCOLHA A FORMA DE PAGAMENTO  '))
while pay < 1 or pay >= 4:
    pay = int(input('OPÇÃO INVÁLIDA, ESCOLHA A FORMA DE PAGAMENTO  '))
match pay:
    case 1:
        print ('LEIA O QR CODE COM O APP DOS EU BANCO!') 
    case 2:
        print('INSERE OU APROXIMA O CARTÃO!')
    case 3:
        print('INSERE OU APROXIMA O CARTÃO!')
