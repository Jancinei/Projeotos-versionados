termo = int(input('Digite o termo   '))
razao = int(input('Digite a razão   '))
conte = 0
mais = 10
total = 0
while mais != 0:
    total += mais
    while conte <= total:
        print (' {} - ' .format(termo), end="")
        conte += 1
        termo += 1
    print ('PAUSA!')
    mais =int(input('Quantos termos você quer a mais?   '))
print('FIM!')
       