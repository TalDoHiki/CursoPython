sl = float(input('What is the salary? R$'))
up = float(input('And the percent of the raising? '))
ns = sl + (sl * (up/100))

print('The new salary of {} up percent the functionary will be R${:.2f}'.format(up,ns))