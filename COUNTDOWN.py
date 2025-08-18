from random import randint
from time import sleep
countdown = int(input('Contagem regressiva, insira os minutos desejados  '))
for c in range(countdown, 0,  -1):
    print(c)
    sleep(1)
print('START')