from time import sleep
from emoji import emojize

print('-=-'*30)
print('{:=^40}'.format(' \033[33mIt is New Year Eve\033[m '))
sleep(1)
print("Let's start the regressive counting...")
sleep(1)
for c in range (10, 0, -1):
    print('\033[33m{}\033[m..'.format(c))
    sleep(1)
print(emojize(('\033[33mHappy New Year!!!\033[m:fireworks:')))