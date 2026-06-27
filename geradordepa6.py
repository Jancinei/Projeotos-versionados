termo = int(input('Digite o termo   '))
razao = int(input('Digite a razão   '))
conte = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while conte <= total:
        print (' {} - ' .format(termo), end="")
        termo += razao
        conte += 1
    print ('PAUSA!')
    mais =int(input('Quantos termos você quer a mais?   '))
print('FIM!')
    