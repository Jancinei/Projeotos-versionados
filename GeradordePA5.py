termo = int(input('Digite o termo   '))
razao = int(input('Digite a razao   '))
conte = 1
while conte <= 10:
    print (' {} -' .format(termo), end=' ' )
    termo += razao
    conte += 1
print ('FIM!')