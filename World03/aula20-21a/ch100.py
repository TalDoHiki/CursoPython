from random import randint
from time import sleep
def dice(list):
    print('Randomizing numbers...',flush=True)
    sleep(0.3)
    for c in range(1,6):
        list.append(randint(0,9))
        print(list[-1],end=' -> ', flush=True)
        sleep(0.3)
    print('End!')
    
def summ(list):
    sm = 0
    for c in list:
        if c%2 == 0:
            sm += c
    print(f'The even sum between {list} is: {sm}.')
numbers = list()
dice(numbers)
summ(numbers)
