ct = 1
while True:
    print(ct, '->', end='')
    ct += 1
    if ct == 10000:
        break
print('Over')

n = s = 0

while True:
    n = int(input('Type a number: '))
    if n == 999:
        break
    s+=n
print(f'The sum is {s}')

name = str(input('Type a name: ')).title().strip().split()[0]
age = int(input(f'Type the age of {name}: '))
sl = float(input(f'Type the salary of {name}: R$'))
print(f'The {name} works for R${sl:.2f} and is {age} years old.')