ano = int(input('Quer saber se um determinado ano é bissexto? digite o ano aqui!  '))
if ano % 2 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print (f'O ano {ano} é bissexto')
else:
    print (f'O ano {ano} não é bissexto')