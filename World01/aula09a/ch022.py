name = str(input('Type your fullname: '))

print(name.upper())
print(name.lower())

print('The name have a total of {} letters.'.format(len(name.replace(' ',''))))

print('Your first name is {} and have a total of {} letters.'.format(name.split()[0],len(name.split()[0])))