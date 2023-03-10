def lin():
    print('-=-'*30)

def title(txt):
    print('-'*30)
    print('{:^30}'.format(f'{txt}'))
    print('-'*30)
tst = str(input('-> ')).upper().strip()
print(title(tst))
lin()

def summ(x,y):
    print(f'{x} + {y} = {x+y}')
summ(2,1)
summ(4,1)
lin()

def counter(*n):
    for v in n:
        print(f'{v}',end=' -> ')
    print('End!')
    print(f'Received the values {n} with a total of {len(n)} numbers')
counter(2,1,7)
counter(8,0)
counter(4,4,7,6,2)
lin()

def double(lst):
    for n in range(len(lst)):
        nn = lst[n]*2
        lst.pop(n)
        lst.insert(n,nn)
values = [7,2,5,0,4]
double(values)
print(values)
