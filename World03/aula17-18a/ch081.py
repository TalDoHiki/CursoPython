list = []
while True:
    list.append(int(input('Type a value: ')))
    ch = ''
    while ch != 'Y' and ch != 'N':
        ch = str(input('Continue? [Y/N] ')).upper().strip()
    if ch == 'N':
        print('-=-'*15)
        break
print(f'''Total of numbers: {len(list)}
Decrescent list: {sorted(list,reverse=True)}''')
if 5 in list:
    print('Number 5 are in list.')
else:
    print('Number 5 not in list')
