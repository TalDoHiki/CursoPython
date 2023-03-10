def title(txt):
    print('{:=^30}'.format(f' {txt} '))
def area(b,h):
    print(f'The area is {b*h}m².')
title('Terrain Control')
area(float(input('Width [m]: ')),float(input('Height [m]: ')))
