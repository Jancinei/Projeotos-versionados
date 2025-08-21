soma = 0
inicial = int(input('Digite o número inicial  '))
final = int(input('Digite o número final  '))
interv = int(input('Digite o intervalo  '))
for c in range(inicial, final, interv):
    if c % 3 ==0:
        soma += c
print(f'A soma da contagem é: {soma}')