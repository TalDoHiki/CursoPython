n1 = int(input('Type a integer number: '))
n2 = int(input('Another one please: '))
lower = n1

if n1 > n2:
    print('The first value is higher.')
elif n2 > n1:
    print('The second value is higher.')
elif n1 == n2:
    print('Both of them have the same value.')