appsts = True
while appsts == True:

    n = int(input('Type a integer number: '))
    nt = n
    q = 1
    bl = []

    ch = int(input('Do you what type of conversion? [binary:1] [Octal:2] [Hexa:3] [Stop:0] '))

    if ch == 1:
        while q >= 1:
            r = n%2
            bl.insert(0,r)
            q = n // 2
            n = q
        b = ''.join([str(item) for item in bl])
        print('The number "{}" in binary is: {}'.format(nt,b))
    elif ch == 2:
        print('Teste')
    elif ch == 3:
        print('Test2')
    elif ch == 0:
        break
    appsts = False
print('Service Ended')