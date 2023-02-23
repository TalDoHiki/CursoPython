sal = float(input('Type the functionary salary: R$'))
inc = 0
if sal > 1250:
    inc = sal + (sal*0.1)
else:
    inc = sal + (sal*0.15)
print('The new salary will be R${:.2f}.'.format(inc))