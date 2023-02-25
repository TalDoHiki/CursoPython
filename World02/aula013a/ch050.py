nbl = []
s = 0
count = 0
for c in range(1,7):
    n = int(input('Type the {} number: '.format(c)))
    nbl.append(n)
    if n%2 == 0:
        s += n
        count += 1
print('The sum of the 6 integers numbers "{}" that are even({}) is = {}.'.format(nbl,count,s))
