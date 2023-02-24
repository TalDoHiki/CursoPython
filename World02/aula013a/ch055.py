wl = []
for c in range(1,6):
    wg = float(input('Type the weight: '))
    wl.append(wg)

wl.sort()
print('''
Max Weight: {}
Min Weight: {}'''.format(wl[-1],wl[0]))