primeiro = int(input('Digite o primeiro valor  '))
razão = int(input('Digite a razão  '))
último = primeiro + (10-1) * razão + 1
for c in range(primeiro, último, razão):
    print(f'{c}', end= ' - ')
print('FIM')