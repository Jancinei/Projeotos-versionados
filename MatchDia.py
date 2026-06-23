dia = int(input('Digite um valor correspondente a um dia da semana  '))
while dia < 1 or dia > 7:
    dia = int(input('Digite um número válido  '))
match dia:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda-feira')
    case 3:
        print('Terça-feira')
    case 4:
        print('Quarta-feira')
    case 5:
        print('Quinta-feira')
    case 6:
        print('Sexta-feira')
    case 7:
        print('Sábado')
print(dia)
