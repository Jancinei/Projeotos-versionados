from random import randint
from time import sleep
itens = ('Rato', 'Gato', 'Mulher')
computador = randint(0,2)
jogador = int(input('''Vamos jogar o jogo do medo? Escolha uma das opções abaixo:
[0] Rato
[1] Gato
[2] Mulher  '''))
print ('PROCESSANDO...')
sleep(2)
print(f'O coputador escolheu {itens[computador]}')
print(f'Você escolheu {itens[jogador]}')
if computador == 0:
    if jogador ==0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHA!')
    elif jogador == 2:
        print('COMPUTADOR GANHA!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador ==0:
        print('COMPUTADOR GANHA!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR GANHA!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador ==0:
        print('JOGADOR GANHA!')
    elif jogador == 1:
        print('COMPUTADOR GANHA!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
