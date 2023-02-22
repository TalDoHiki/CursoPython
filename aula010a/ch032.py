from datetime import date

yr = int(input('Type a year [Type 0 for the currently year]: '))
yr = date.today().year if yr == 0 else yr
print('{} is a leap year.'.format(yr)) if yr%4 == 0 and yr%100 !=0 or yr%400 ==0 else print('{} is not a leap year.'.format(yr))