def fact(n):
    f = 1
    for c in range(1,n+1):
        f *= c
    return f
def double(n):
    return n*2
def triple(n):
    return n*3
def half(n):
    return n/2
def pctIncrease(n, p):
    n += n*(p/100)
    return n
def pctDecrease(n, p):
    n -= n*(p/100)
    return n
def curformat(n):
    return f'R${n:.2f}'