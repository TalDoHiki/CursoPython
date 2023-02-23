from datetime import date

st = True
ge = int(input('Type your gender: Male(1) / Female(2)'))
if ge == 2:
    st = False
    print('You do not have to enroll a miliatry service.')

while st == True:
    by = int(input('Type the year of birth: '))
    id = date.today().year - by

    if id < 18:
        print('You will have to enroll the military service in {} years.'.format(18-id))
    elif id == 18:
        print('It is time to enroll military service this year.')
    elif id > 18:
        print('Dude! you withhold it for sure, like it was almost {} years ago.'.format(id-18))
    st = False