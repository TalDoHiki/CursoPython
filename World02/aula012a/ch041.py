from datetime import date

by = int(input('Type the year of birth: '))
id = date.today().year - by

if id > 20:
    print('Master')
elif id <= 20 and id > 19:
    print('Senior')
elif id <= 19 and id > 14:
    print('Junior')
elif id <= 14 and id >9:
    print('Infantil')
elif id <= 9:
    print('Mirim')