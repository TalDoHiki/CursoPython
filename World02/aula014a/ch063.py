n = int(input('How many terms do you want: '))
c = 1
tot = 0
lt = [0, 1]
tot = lt[-1] + lt[-2]
print ('{} -> {}'.format(lt[0], lt[1], end=' -> '))
while c <= n:
    print('{}'.format(lt[-1] + lt[-2]), end=' -> ')
    lt.append(lt[-1] + lt[-2])
    c += 1
