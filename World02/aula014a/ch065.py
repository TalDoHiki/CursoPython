n = 0
flag = True
hn = 0
ln = 0
avgn = 0
totn = 0
while flag == True:
    ch = ''
    n = int(input('Type a integer number: '))
    if avgn == 0:
        hn = n
        ln = n
    if n > hn:
        hn = n
    if n < ln:
        ln = n
    totn += n
    avgn += 1
    flag = False
    while ch != 'Y' and ch != 'N':
        ch = str(input('Continue? [Y/N] ')).strip().upper()[0]
        if ch == 'Y':
            flag = True
        elif ch == 'N':
            print('Ok.')
print('''Results:
Total Numbers: {}
Average: {}
Higher Number: {}
Lower Number: {}'''.format(avgn, totn/avgn, hn, ln))
