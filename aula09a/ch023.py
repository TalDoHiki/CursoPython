n = str(input('Type a number between 0 and 9999: '))
if int(n) > 9999 or int(n) < 0:
    print('[ERROR]')
else:
    print('Unit:',n[3:])
    print('Ten:',n[2:3])
    print('Hundred:',n[1:2])
    print('Thousand:', n[0:1])