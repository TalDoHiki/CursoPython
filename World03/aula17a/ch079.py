list = []
while True:
    n = int(input('Type a value: '))
    if n in list:
        print('[ERROR] Value already in list.')
    else:
        list.append(n)
    ch = ''
    while ch != 'Y' and ch != 'N':
        ch = str(input('Continue? [Y/N] ')).upper().strip()[0]
    if ch == 'N':
        break
print(sorted(list))
