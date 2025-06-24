n1 = int(input('Digite um valor  '))
n2 = int(input('Digite outro valor  '))
n3 = int(input('Digite mais um valor  '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
else:
   maior = n3
print (maior)