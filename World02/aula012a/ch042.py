sideang = []

while len(sideang) < 3:
    new_ang = float('Type a length of a triangle: ')
    sideang.append(new_ang)

sideang.sort()
if sideang[0] + sideang[1] < sideang[2]:
    print('With these three lines we cannot form a triangle.')
elif sideang[0] == sideang [1] == sideang[2]:
    print('We can form a equilateral triangle.')
elif sideang[2] == sideang[1]:
    print('We can form a isosceles triangle')
elif sideang[0] + sideang[1] > sideang[2]:
    print('We can form a scalene triangle')