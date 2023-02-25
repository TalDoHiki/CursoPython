from random import shuffle, randint

stuN = int(input('How many students have for the seminary? '))
names = []
i = 1

while i <= stuN:
    new_name = input("Type the student {} name: ".format(i))
    names.append(new_name)
    i += 1
    
shuffle(names)
print('The order of apresentation will be: {}'.format(names))
