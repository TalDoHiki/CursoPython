people = []
data = []
ow = uw = 0
while True:
    data.append(str(input('Type the name: ').title().strip()))
    data.append(float(input('Type the weight: ')))
    if len(people) == 0:
        ow = uw = data[1]
    else:
        if data[1] > ow:
            ow = data[1]
        if data[1] < uw:
            uw = data[1]
    people.append(data[:])
    data.clear()
    ch = input('Continue? [. = NO] ')
    if ch == '.':
        break
print('-=-'*30)
print(f'Result')
print(f'People Sign-in: {len(people)}')
print(f'Most overweight people: [{ow}Kg]',end=' ')
for p in people:
    if p[1] == ow:
        print(f'{p[0]}', end='.. ')
print(f'Most underweight people: [{uw}Kg]',end=' ')
for p in people:
    if p[1] == uw:
        print(f'{p[0]}', end='.. ')
