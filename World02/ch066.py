ct = s = 0
while True:
    n = int(input('Type a integer number: '))
    while n != int:
        n = int(input('[INVALID] Type a integer number: '))
    if n == 999:
        break
    s += n
    ct += 1
print(f'Total of {ct} numbers with the sum of {s}')