soma = 0
cont = 0
for c in range(1, 5):
    num = int(input(f'Digite o {c}º número:  '))
    soma += num
    cont += 1
print (f'A soma dos valores digitados são: {soma}')
print(f'Você digitou {cont} números')
