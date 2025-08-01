#Alistamento militar#
from datetime import date
atual = date.today().year
nascimento = int(input('Digite seu ano de nascimento  '))
idade = atual - nascimento
if idade == 18:
    print(f'Você já completou 18 anos, procure um junta militar imediatamente')
elif idade> 18:
    print(f'Sua idade é {idade} anos, seu ano de alistamento foi {nascimento + 18}')
else:
    print(f'Sua idade é {idade} anos, você deve alistar-se em {18 - idade + atual}')
