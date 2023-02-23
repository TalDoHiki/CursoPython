from random import choice

names = []
stuN = int(input('How many students are there? '))
i=1
while i <= stuN:
    new_name = input('Type the name of the student {}: '.format(i))
    names.append(new_name)
    i += 1
print('The one who will be erasing the board is: {}'.format(choice(names)))