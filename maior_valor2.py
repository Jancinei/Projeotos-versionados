from time import sleep
n1 = eval(input('Vamos ver qual o maior valor entre três números aleatórios? digite o primerio número  '))
n2 = eval(input('Digite o segundo número  '))
n3 = eval(input('Digite o terceiro número  '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print ('PROCESSANDO...')
sleep(2)
print (f'O maior valor é {maior}')

