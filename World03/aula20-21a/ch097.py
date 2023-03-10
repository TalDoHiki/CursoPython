def write(txt):
    print('-=-'*(len(txt)))
    print(' '*len(txt),end='')
    print(txt,end='')
    print(' '*len(txt))
    print('-=-'*(len(txt)))
write(str(input('-> ')))
