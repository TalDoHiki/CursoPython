nbs = []
n = 0
while n < 3:
    new_numb = int(input('Type a number: '))
    nbs.append(new_numb)
    n += 1
nbs.sort(reverse = True)
print('The higher number is {}.'.format(nbs[0]))
nbs.sort()
print('The lower number is {}.'.format(nbs[0]))