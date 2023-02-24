nbl = []
s = 0
for c in range(1,7):
    n = int(input('Type a number: '))
    nbl.append(n)
    if n%2 == 0:
        s += n
print('The sum of the 6 integers numbers "{}" that are even is = {}.'.format(nbl,s))
