vt = (int(input('Type a value: ')), int(input('Type a value: ')), int(input('Type a value: ')), int(input('Type a value: ')))

print(f'9 appears a total of {vt.count(9)} times.')
if 3 in vt:
    print(f'The first 3 has appeared in the position {vt.index(3)+1}')
else:
    print('There is no 3 in this tuple')
print(f'The even numbers is: ', end='')
for n in vt:
    if n%2 == 0:
        print(n, end=' ')