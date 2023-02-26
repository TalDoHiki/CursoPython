print('{:=^40}'.format(' Logic Calculator '))

calc_s = True
while calc_s == True:
    numb_st = True
    n1 = int(input('Type the first number: '))
    n2 = int(input('Type the second number: '))
    while numb_st == True:
        print('-=-'*15)
        print('''Here are the functions:
        [1] SUM       [4] DIVIDE
        [2] SUB       [5] COMPARE
        [3] MULTIPLY  [6] NEW NUMBERS
        [0] TURN OFF''')
        calc_ch = int(input('So what you wanna do with {} and {}? '.format(n1,n2)))
        if calc_ch == 1:
            print('Result:')
            print('{} + {} = {}'.format(n1,n2,n1+n2))
        elif calc_ch == 2:
            print('Result:')
            print('{} - {} = {}'.format(n1,n2,n1-n2))
        elif calc_ch == 3:
            print('Result:')
            print('{} x {} = {}'.format(n1,n2,n1*n2))
        elif calc_ch == 4:
            print('Result:')
            print('{} / {} = {}'.format(n1,n2,n1/n2))
        elif calc_ch == 5:
            print('Result:')
            if n1 > n2:
                print('{} > {}'.format(n1,n2))
            elif n1 < n2:
                print('{} < {}'.format(n1,n2))
            else:
                print('{} = {}'.format(n1,n2))
        elif calc_ch == 6:
            print('Changing the numbers then...')
            numb_st = False
        elif calc_ch == 0:
            print('Goodbye!')
            calc_s = False
            numb_st = False
