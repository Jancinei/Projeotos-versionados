cores = input('digite a cor  ')
if cores == 'amarelo':
    print (f'\033[1;43m {cores} \033[m' )
if cores == 'azul':
    print (f'\033[1;30;44m {cores} \033[m')
if cores == 'verde':
    print (f'\033[1;42m {cores} \033[m')
if cores == 'vermelho':
    print (f'\033[1;30;41m {cores} \033[m')
if cores != 'amrelo' and cores != 'azul' and cores != 'verde' and cores != 'vermelho':
    print('Você não digitou cor disponível')