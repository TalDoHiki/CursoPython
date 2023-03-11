def intRead():
    vld = input('Type a number: ')
    while vld.isnumeric() == False :
        print('\033[31m[ERROR] Type a valid integer number.\033[m')
        vld = input('Type a number: ')
    return vld
n = intRead()
print(f'The number typed was {n}.')
