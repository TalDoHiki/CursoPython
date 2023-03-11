def double(n,fmt=False):
    if fmt == False:
        return n*2
    else:
        return f'R${n*2:.2f}'
def half(n,fmt=False):
    if fmt == False:
        return n/2
    else:
        return f'R${n/2:.2f}'
def pctIncrease(n, p,fmt=False):
    n += n*(p/100)
    if fmt == False:
        return n
    else:
        return f'R${n:.2f}'
def pctDecrease(n, p,fmt=False):
    n -= n*(p/100)
    if fmt ==  False:
        return n
    else:
        return f'R${n:.2f}'
def currencyf(n):
    return f'R${n:.2f}'
def csummary(n, p1=0, p0=0):
    print('-'*30)
    print('{:^30}'.format('Summary Of The Price'))
    print('-'*30)
    print('{:<15}'.format('Price:')+'{:>15}'.format(currencyf(n)))
    print('{:<15}'.format('Double:')+'{:>15}'.format(double(n,True)))
    print('{:<15}'.format('Half:')+'{:>15}'.format(half(n,True)))
    print('{:<15}'.format(f'{p1}% More:')+'{:>15}'.format(pctIncrease(n,p1,True)))
    print('{:<15}'.format(f'{p0}% Less:')+'{:>15}'.format(pctDecrease(n,p0,True)))
    print('-'*30)
