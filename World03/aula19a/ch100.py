from random import randint
def dice():
    numbers = []
    for c in range(1,6):
        numbers.append(randint(0,9))
    print(f'Numbers randomized: {numbers}')
def summ(n):
    sm = 0
    for c in n:
        if c%2 == 0:
            sm += c
    print(f'The sum between then is: {sm}.')
print(dice())
