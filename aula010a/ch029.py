vel = float(input('What is the car speed? '))
pc = 7* (vel - 80)

if vel > 80:
    print('[MULTED!] You surpass the speed!')
    print('And the paycheck is: R${:.2f}.'.format(pc))
else:
    print('Great, Continue driving with safety.')