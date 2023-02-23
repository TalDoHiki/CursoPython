pc = float(input('What is the price of the product: R$'))
pm = int(input('And the payment method? [In cash(1)] [In cash card(2)] [2x card(3)] [3x or more on card (4)] '))

if pm == 1:
    pc = pc - (pc * 0.1)
elif pm == 2:
    pc = pc - (pc * 0.05)
elif pm == 3:
    pc = pc
elif pm == 4:
    pc = pc + (pc * 0.2)

print('The total you will have to pay is: R${}.'.format(pc))