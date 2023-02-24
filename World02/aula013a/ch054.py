from datetime import date

map = 0
mip = 0
for c in range(1,8):
    dt = int(input('Type the year of birth: '))
    if date.today().year - dt > 21:
        map += 1
    else:
        mip +=1
print('A total of {} people have reached in the majority and {} people have not reached.'.format(map,mip))