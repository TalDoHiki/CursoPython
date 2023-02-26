n1 = float(input('Type the first term of the AP: '))
r = float(input('Type the ratio of the AP: '))
ct = int(input('How many terms do you want to know: '))
c = 1
while c <= ct:
    print('{}'.format(n1 + r*(c-1)), end=' -> ')
    c += 1
