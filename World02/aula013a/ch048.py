n = int(input('Type a number: '))
s = 0
for n in range(n,501+n):
    s += n
print('The sum between {} and {} is {}.'.format(n, n+500, s))