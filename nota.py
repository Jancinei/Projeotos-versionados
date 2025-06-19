import time
nota = eval(input('Digite a nota da atividade  '))
avaliação = eval(input('Digite a nota da avaliação  '))
print ('PROCESSANDO...')
time.sleep(2)
if nota + avaliação >= 7:
    print (f' Sua nota é {nota+avaliação :.2f} Você está aprovado')
else:
    print (f'Sua nota é {nota + avaliação :.2f} nota não satisfatória, Reprovado(a)!')

