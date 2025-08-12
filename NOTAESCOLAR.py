avaliação = eval(input('Digite sua nota da avaliação  '))
atividade = eval(input('Digite sua nota da atividade '))
media = (avaliação + atividade) /2
if media >= 7:
    print (f'Sua média é {media:.2F}, você está APROVADO')
else:
    print (f'sua nota é {media :.2f}, você foi reprovado, acompanhe pelo portal a data do exame')

