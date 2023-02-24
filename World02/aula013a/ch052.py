n = int(input('Type a number: '))
tot = 0

for c in range(1,n+1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mThe number {} was divided {} times'.format(n,tot))
if tot == 2 or n == 1:
    print("That's why he's a prime number")
else:
    print("That's why he isn't a prime number")