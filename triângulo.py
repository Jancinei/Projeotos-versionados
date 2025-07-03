lado_a = eval(input('Digite o lado a do triâgulo  '))
lado_b = eval(input('Digite o lado b do triâgulo  '))
lado_c = eval(input('Digite o lado c do triâgulo  '))
if lado_a < lado_b and lado_a < lado_c  and lado_b > lado_a and lado_b < lado_c and lado_c > lado_a and lado_c > lado_b:
    print ('É um triâgolo')
else:
    print('Não é um triângulo')