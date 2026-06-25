termo = int(input('Digite o termo   '))
razao = int(input('Digite a razão   '))
conte = 0
while conte <= 10:
    print (' {}-' .format(termo), end='')
    conte += 1
    termo += razao
print ('FIM!')

