name = str(input('Type a fullname: ')).title().strip().split()

print('The first name is: "{}". And the last name is: "{}".'.format(name[0], name[-1]))