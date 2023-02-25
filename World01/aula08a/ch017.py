from math import hypot

co = float(input('Opposite leg: '))
ca = float(input('Adjacent leg: '))

print('The hip length of this triangle is {}'.format(hypot(co,ca)))
