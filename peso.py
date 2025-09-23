maior = 0
menor = 0
for p in range(1, 6):
    peso = eval(input(f'Peso da {p}ª pessoa  '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'o maior peso é {maior}')
print(f'O menor peso é {menor}')
