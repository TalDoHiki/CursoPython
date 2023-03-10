from datetime import date
def vote():
    bd = int(input('Year of birth: '))
    age = date.today().year - bd
    return age
ag = vote()
if ag < 16:
    print('DENIED.')
elif ag < 18 or ag >= 65:
    print('OPTIONAL.')
else:
    print('OBRIGATORY.')
