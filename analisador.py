somaidade = 0
mediaidade = 0
mais_velho = 0
mais_novo = 0
from datetime import date
ano_atual = date.today() .year
for c in range(1, 3):
    print(f'_____________ {c}ª pessoa ____________')
    nome = input('Digite o nome   ') .strip()
    nascimento = int(input('Digite o ano de nascimento  '))
    sexo = input(('Escolha o sexo [M/f]: ')).strip()
    idade = ano_atual - nascimento
    print (f'Sua idade é {idade} anos')
    somaidade += idade
    mediaidade += idade/2
    if c == 1:
        mais_velho = idade
        mais_novo = idade
    else:
        if idade > mais_velho:
            mais_velho = idade
        if idade < mais_novo:
            mais_novo = idade
print(f'A soma das idade é {somaidade}')
print(f'A média de idade é {mediaidade}')
print(f'O mais velho tem {mais_velho} anos')
print(f'O mais novo tem {mais_novo} anos')