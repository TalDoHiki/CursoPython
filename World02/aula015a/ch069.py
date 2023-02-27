ct_age = ct_M = ct_M20 = ct_F = ct_F20 = ct_P = ct_avg = 0
while True:
    ct_P += 1
    print('{:=^40}'.format(f' {ct_P}° Person '))
    age = int(input('Type de age of the person: '))
    gender = ''
    while gender != 'M' and gender != 'F':
        gender = str(input('Type the gender of the person: [M/F] ')).upper().strip()[0]
    if age > 18:
        ct_age += 1
    if gender == 'M':
        ct_M += 1
    if gender == 'M' and age <20:
        ct_M20 += 1
    if gender == 'F':
        ct_F += 1
    if gender == 'F' and age <20:
        ct_F20 += 1
    ct_avg += age
    ch = ''
    while ch != 'Y' and ch != 'N':
        ch = str(input('Continue? [Y/N] ')).upper().strip()[0]
    if ch == 'Y':
        print('-=-'*15)
    elif ch == 'N':
        print('-=-'*15)
        break    
print(f'''Results:
Total: {ct_P}
Age Average: {ct_avg/ct_P}
Majority: {ct_age}
Mans: {ct_M}
Mans Minority: {ct_M20}
Homens: {ct_F}
Homens Minority: {ct_F20}''')
