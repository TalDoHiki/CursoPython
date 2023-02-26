n1 = float(input('Type the first term: '))
r = float(input('Type the ratio: '))
ct = int(input('How many terms do you want to know? '))
c = 1
nt = 0
ct_st = True
while ct_st == True:
    while c <= ct:
        print('{} Term: {}'.format(c, n1 + (r*(c-1))), end=' | ')
        c += 1
    ct_st = False
    nt = int(input('\nDo you want more terms? [Y-How Many? / No - 0] '))
    if nt > 0:
        ct_st = True
        ct += nt
print('Bye')
