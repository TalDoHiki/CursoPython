wl = []
for c in range(1,6):
    wg = float(input('Type the {} people weight: '.format(c)))
    wl.append(wg)

wl.sort()
print('''
Max Weight: {}Kg
Min Weight: {}Kg'''.format(wl[-1],wl[0]))
