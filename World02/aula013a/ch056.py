agm = 0
agep = 0
nm = ''
wm20 = 0
c = 1
for c in range(1,5):
    print('{:=^40}'.format(' {} Person ').format(c))
    name = str(input('Type de name: ')).title().strip()
    age = int(input('Type the age: '))
    gender = str(input('Type the gender: [M/F] ')).upper().strip()
    if gender != 'M' and gender != 'F':
        print('[INVALID GENDER]')
        exit()
    agm += age
    if c == 1 and gender == 'M':
        agep = age
        nm = name
    if gender == 'M' and age > agep:
        agep = age
        nm = name
    if gender == 'F' and age < 20:
        wm20 += 1
print('{:=^40}'.format(' Result '))
print('''
Age Average: {:.1f}
Name of the oldest man: {}
Homens lower than 20 years old: {}'''.format(agm/c,nm,wm20))    
