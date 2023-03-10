def sheet(name='',goals=''):
    name = name.title().strip()
    if name == '':
        name = '<unknown>'
    print('--'*len(name)*2)
    if goals == '':
        goals = 0
    print(f'Name: {name} | Goals: {goals}')
    print('--'*len(name)*2)
sheet(str(input('Player Name: ')),input('Goals: '))
