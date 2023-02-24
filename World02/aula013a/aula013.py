for c in range (7,1,-1):
    print(c)
print('End.')
print('-=-'*30)

st = int(input('Start: '))
ed = int(input('End: '))
stp = int(input('Step: '))
for c in range (st, ed+1, stp):
    print(c)
print('End.')

s = 0
for c in range(0,4):
    n = int(input('Type a number: '))
    s += n
print('The total of the values typed is {}.'.format(s))