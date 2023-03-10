list = [[0,0,0],[0,0,0],[0,0,0]]
sum_e = sum_3c = hgval_l2 = 0
for l in range(0,3):
    for c in range(0,3):
        list[l][c] = int(input(f'Value [{l},{c}]: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{list[l][c]:^5}]',end='')
        if list[l][c]%2 == 0:
            sum_e += list[l][c]
        if  c == 2:
            sum_3c += list[l][c]
        if l==1 and list[l][c] >= hgval_l2:
            hgval_l2 = list[1][c] 
    print()
print('-=-'*15)
print(f'''Sum of the even values: {sum_e}
Sum of the values in the third column: {sum_3c}
Higher value in the second line: {hgval_l2}''')
