n = (input('Type a number between 0 and 9999: '))
if int(n) < 1000:
    n = int(n)
    u = n // 1 %10
    d = n // 10 %10
    c = n // 100 % 10
    m = n // 1000 % 10
    print('Unit: {}'.format(u))
    print('Ten: {}'.format(d))
    print('Hundred: {}'.format(c))
    print('Thousand: {}'.format(m))
else:
    print('Unit: {}'.format(n[3:]))
    print('Ten: {}'.format(n[2:3]))
    print('Hundred: {}'.format(n[1:2]))
    print('Thousand: {}'.format(n[0:1]))