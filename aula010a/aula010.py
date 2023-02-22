

ch = int(input('Do you wanna try (name[1]) or (grade[2])? '))

if ch == 1:
    name = str(input('What is your name: ')).capitalize().strip().split()[0]
    if name == 'Felpe':
        print('Hello, {}!'.format(name))
    else:
        print('Get out of here, {}!!!'.format(name))
elif ch == 2:
    n1 = float(input('Type your first grade: '))
    n2 = float(input('Type your second grade: '))
    avg = (n1 + n2) / 2
    print('Your average is ..{}, then you are...'.format(avg))
    print('APRROVED') if avg >= 6.0 else print('REPROVED')