from time import sleep
print ('Qual o valor da hiponenusa de qual trângulo')
cateto_oposto = eval(input('Digite o valor do cateto oposto '))
cateto_adjacente = eval(input('Digite o valor do cateto adjacente '))
hipotenusa = (((cateto_adjacente **2) + (cateto_oposto**2)) ** 0.5)
print ('PROCESSANDO')
sleep(2)
print (f'O valor da hipotenusa é {hipotenusa:.2f}')
