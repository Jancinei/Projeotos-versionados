from random import randint
from time import sleep
account = int(input('contagem de pares, digite o número desejado  '))
for par in range(0, account+1, 2):
    sleep(1)
    print(par)
print('FIM')