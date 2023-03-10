def fact(n=1,show=False):
    """
    -> Used to calculate a factorial number.
    :param n: target number.
    :param show: -> display the equation.
    :return: -> factorial number of n.
    """
    f = 1
    if show == False:
        for c in range(n, 0, -1):
            f *= c
        return f
    else:
        for c in range(n,1,-1):
            f *=c
            print(f'{c}', end=' X ')
        print(f'1 = {f}')
help(fact)
