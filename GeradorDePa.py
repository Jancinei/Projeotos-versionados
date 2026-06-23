termo = int(input('Digite o termo  '))
razao = int(input('Digite a razão   '))
conte = 1
while conte <= 10:
    print ('{} -' .format(termo), end='')
    termo += razao
    conte += 1
