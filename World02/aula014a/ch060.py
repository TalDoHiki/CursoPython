n = int(input('Type a integer number: '))
fn = n
c = n - 1
print('{} x '.format(n), end='')
while c != 1:
    print('{} x '.format(c), end='')
    n *= c
    c -= 1
print('1 = {}.'.format(n))