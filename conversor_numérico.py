num = int(input('Escolha um número inteiro   '))
opção = int(input('''Escolha uma opção de conversão:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal \n'''))
if opção == 1:
    print (f'{num} convertido para binário é igual a {bin(num)[2:]}')
elif opção == 2:
    print (f'{num} convertido para octal é igual a {oct(num)[2:]}')
elif opção == 3:
    print (f'{num} convertido para hexadecimal é igual a {hex(num)[2:]}')
else:
    print ('Opição inválida')

