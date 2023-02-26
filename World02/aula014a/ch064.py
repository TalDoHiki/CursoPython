fl = 0
n = 0
totn = 0
while n != 999:
    n = int(input('Type a integer value (Will only stop when type 999): '))
    fl += n
    totn += 1
totn -= 1
fl -= 999
print('There was a total of {} numbers typed, and the sum between them is {}.'.format(totn, fl))
