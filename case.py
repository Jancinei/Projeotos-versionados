print ('''       [1-AL]
       [2-BA]
       [3-CE]
       [4-DF]
       [5-GO]
       [6-MA]
       [7-MG]''')
estados = int(input('QUAL DOS ESTADOS VOCÊ NASCEU     ')) 
match estados:
    case 1:
        print ('ALAGOAS')
    case 2:
        print ('BAHIA')
    case 3:
        print ('CEARÁ')
    case 4:
        print ('DISTRITO FEDERAL')
    case 5:
        print ('GOIÁS')
    case 6:
        print ('MARANHÃO')
    case 7:
        print('MINAS GERAIS')
print('FIM!')