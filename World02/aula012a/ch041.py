from datetime import date

by = int(input('Type the year of birth: '))
id = date.today().year - by
cl = str

if id <= 9:
    cl = 'Mirim'
elif id <= 14:
    cl = 'Infantil'
elif id <= 19:
    cl ='Junior'
elif id <= 20:
    cl = 'Senior'
else:
    cl = 'Master'

print('''
Date of Birth: {}
Athlete Age: {}
Rank: {}'''.format(by,id,cl))
