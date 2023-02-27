a = b = c = d = nine = 0
vt = (a, b, c, d)

a = int(input('Type a value: '))
b = int(input('Type a value: '))
c = int(input('Type a value: '))
d = int(input('Type a value: '))

print(f'9 appears a total of {vt.count(9)} times.')
print(f'The first 3 has appeared in the index {vt.index(3)}')
print(f'The even numbers is: {vt.index(a) if a%2 == 0 else print, vt.index(b) if b%2 == 0 else print, vt.index(c) if c%2 == 0 else print, vt.index(d) if d%2 == 0 else print}')