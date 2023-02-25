sideang = []

while len(sideang) < 3:
    new_ang = float(input('Type a length of a triangle: '))
    sideang.append(new_ang)
sideang.sort()

if sideang[0] + sideang[1] < sideang[2] or sideang[0] + sideang[1] == sideang[2]:
    print('With these three lines we cannot form a triangle.')
else:
    print('We can form a ', end='')
    if sideang[0] == sideang [1] == sideang[2]:
        print('equilateral triangle.')
    elif sideang[2] == sideang[1]:
        print('isosceles triangle')
    elif sideang[0] + sideang[1] > sideang[2]:
        print('scalene triangle')
