amt = []
i = 0
while i < 3:
    print('-=-'*15)
    new_rt = float(input('What is the length of the line: '))
    amt.append(new_rt)
    i += 1
amt.sort()
print('-=-'*30)
print('With these 3 lines we can form a triangle!') if amt[0] + amt[1] > amt[2] else print('We cannot form a triangle.')