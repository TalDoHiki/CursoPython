list = []
while True:
    #Add a value and don't repeat

    ch = ''
    while ch != 'Y' and ch != 'N':
        ch = str(input('Continue? [Y/N] ')).upper().strip()[0]
    if ch == 'N':
        break
print(sorted(list))