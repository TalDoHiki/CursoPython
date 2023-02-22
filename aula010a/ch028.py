from random import randint
from time import sleep

hs = randint(0,5)
print('\033[1;33m-=-\033[m'*30)
print('Thinking in a number between 0 and 5...')
print('\033[1;33m-=-\033[m'*30)
sleep(3)
pl = int(input('Guess the random number that the house chose: '))
print('\033[33mThe house chose: {}\033[m'.format(hs))
print('\033[1;32mWow! Congratzz, you won!\033[m') if pl == hs else print('\033[1;31mDamn, better luck next time, fella.\033[m')