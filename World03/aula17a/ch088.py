from random import randint
from time import sleep

gn = int(input('How many games do you want? '))
list = []
data = []
print('{:=^30}'.format(f' Sorting {gn} Games '))
for c in range(1,gn+1):
    sleep(1)
    for n in range(0,6):
        data.append(randint(1,60))
    data.sort()
    list.append(data[:])
    data.clear()
    print(f'Game {c}: {list[:][c-1]}')
print('{:=^30}'.format(' Good luck '))
