from datetime import date

by = int(input('Type the year of birth: '))
id = date.today().year - by

if id < 18:
    print('You will have to enroll the military service in {} years.'.format(18-id))
elif id == 18:
    print('It is time to enroll military service this year.')
elif id > 18:
    print('Dude! you withhold it for sure, like it was almost {} years ago.'.format(id-18))