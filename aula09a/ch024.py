name = input('Type a city name: ')

if 'Santo' in name.title().split()[0]:
    print('The city {} starts with "Santo"'.format(name.title()))
else:
    print('The city {} do not start with "Santo'.format(name.title()))