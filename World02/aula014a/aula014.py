n = 1
even = odd = 0
while n != 0:
    n = int(input('Type a value: '))
    if n != 0:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
print('You typed {} even and {} odd numbers'.format(even,odd))