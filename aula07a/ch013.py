sl = float(input('What is the salary? R$'))
up = float(input('And the percent of the raising? '))
ns = sl + ((up/100) * sl)

print('The new salary of {} up percent the functionary will be R${}'.format(up,ns))