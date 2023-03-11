def valicur(txt):
    n = input(txt)
    n = n.replace(',','.')
    while n.replace(',','.').replace('.','').isnumeric() == False:
        print('\033[31m[ERROR] Type a valid number.\033[m')
        n = input(txt)
    return float(n)
