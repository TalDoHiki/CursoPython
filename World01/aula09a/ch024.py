name = input('Type a city name: ').title().strip()

if 'Santo' in name.split()[0]:
    print('The city {} starts with "Santo"'.format(name))
else:
    print('The city {} do not start with "Santo'.format(name))