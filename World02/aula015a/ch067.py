while True:
    c = 0
    n = int(input('Type a value to multiply: '))
    if n < 0:
        break
    while c <= 10:
        print(f'{n} x {c:2} = {n*c}')
        c += 1
print('SERVICE ENDED.')
print('-=-'*15)
