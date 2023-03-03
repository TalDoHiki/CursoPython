list = []
std = []
while True:
    std.append(str(input('Name: ')).title().strip())
    std.append(float(input('Grade 1: ')))
    std.append(float(input('Grade 2: ')))
    list.append(std[:])
    std.clear()
    ch = input('dot to stop: ')
    if ch == '.':
        break
print('-=-'*15)
print('{:<3}'.format('ID'),'{:<15}'.format('Name'),'{:<3}'.format('AVG'))
print('-'*30)
for st in range(len(list)):
    print(f'{st:<3}',f'{list[st][0]:<15}',f'{(list[st][1] + list[st][2])/2:<3}')
print('-'*30)
while True:
    ch_st = int(input('For specified info type the student ID: [negative id stops] '))
    if ch_st < 0:
        break
    else:
        print(f'Name: {list[ch_st][0]} | Grades: {list[ch_st][1:]}')
        print('-'*30)
