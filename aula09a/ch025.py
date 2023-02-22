name = str(input('Type a person name: ')).strip().title()

if 'Silva' in name:
    print('The name {} have "Silva" on it.'.format(name))
else:
    print('The name {} does not have "Silva" on it.'.format(name))