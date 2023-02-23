print('Welcome to the Del Hiki Bank, Lets go to the matters...')

loan = float(input('How much the loan will be? R$'))
sal = float(input('And your salary is? R$'))
time = int(input('The last... How many years do you pretend to pay? ')) * 12

pm = loan / time

print('[LOAN DENIED] The monthly payment percent exceed the max. You will need at least R${:.2f} more'.format(pm - (sal*0.3))) if pm > (sal * 0.3) else print('Good! Your monthly tax will be R${:.2f}.'.format(pm))