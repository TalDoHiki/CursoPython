num = int(input('Type an integer number: '))
print('''Choose your conversion type:
[1] BINARY
[2] OCTAL
[3] HEXADECIMAL''')
op = int(input('Your chose: '))
if op != 1 and op !=2 and op != 3:
    print('Type a valid chose.')
elif op == 1:
    print('{} converted to binary is {}.'.format(num,bin(num)[2:]))
elif op == 2:
    print('{} converted to octal is {}.'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} converted to hexadecimal is {}.'.format(num, hex(num)[2:]))