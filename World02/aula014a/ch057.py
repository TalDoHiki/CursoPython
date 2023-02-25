gender = ""
count = 0
while gender != 'M' and gender != 'F':
    gender = (input('Type a gender: ')).strip().upper()[0]
    count += 1
print('You missed a total of {} times.'.format(count-1))
