list = []
for c in range(1,6):
    list.append(int(input('Type a value: ')))
print(f'List: {list}')
print(f'\nHigher Value: {sorted(list)[-1]} | Position: ', end='')
c = 0
for n in range(len(list)):
    if list[n] == sorted(list)[-1]:
        print(c+1, end='.. ')
    c += 1
print(f'\nLower Value: {sorted(list)[0]} | Position: ',end='')
c = 0
for n in range(len(list)):
    if list[n] == sorted(list)[0]:
        print(c+1, end='.. ')
    c += 1
