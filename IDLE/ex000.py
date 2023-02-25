import random

n1 = int(input('Digite um numero: '))
parimp = input('Escolha par ou impar: ')
x = random.randint(1,2)

if (n1%x == 0):
    if parimp == 'par':
        print('Você venceu!')
    else:
        print('Você perdeu.')
elif(n1%x == 0):
    if parimp == 'par':
        print('Você perdeu.')
    else:
        print('Você venceu!')
