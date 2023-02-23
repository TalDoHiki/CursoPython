dist = float(input('What is the distance of the trip? '))
cs = 0
if dist <= 200 and dist > 0:
    cs = 0.5 * dist
elif dist > 200:
    cs = 0.45 * dist

print('The trip will cost R${:.2f}'.format(cs))