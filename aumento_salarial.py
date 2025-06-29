salario = eval(input('Digite seu salário  '))
if salario <= 1250:
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.10)
print (f'Seu novo salário é: R$ {novo :.2f}')


