print('-=-'*30)
print('{:=^40}'.format(' Del Hiki Store '))
pc = float(input('What is the price of the product: R$'))
print('''
[In cash(1)] 
[In cash card(2)] 
[2x card(3)] 
[3x or more on card (4)]''')
pm = int(input('And the payment method? '))

if pm == 1:
    pc = pc - (pc * 0.1)
elif pm == 2:
    pc = pc - (pc * 0.05)
elif pm == 3:
    pc = pc
elif pm == 4:
    pc = pc + (pc * 0.2)
else:
    pc = 0
    print('[INVALID OPTION]')

print('The total you will have to pay is: R${}.'.format(pc))
print('-=-'*15)
