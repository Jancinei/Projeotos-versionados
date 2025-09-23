frase = input('Digite uma frase  ') .strip() .upper() .split()
junto = ''.join(frase)
print(f'\033[1;31m{junto}')
