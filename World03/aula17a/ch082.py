list = []
le = []
lo = []
while True:
    list.append(int(input('Type a value: ')))
    ch = ''
    while ch != 'Y' and ch !='N':
        ch = str(input('Continue [Y/N] ')).upper().strip()
    if ch == 'N':
        print('-=-'*15)
        break
for n in list:
    if n%2 == 0:
        le.append(n)
    else:
        lo.append(n)
print(f'''Primary List: {list}
Even List: {le}
Odd List: {lo}''')
