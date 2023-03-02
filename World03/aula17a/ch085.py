list = [[],[]]
for c in range(1,8):
    n = int(input(f'Number [{c}]: '))
    if n%2 == 0:
        list[0].append(n)
    else:
        list[1].append(n)
list[0].sort
list[1].sort
print(f'''Result
Even List: {list[0]}
Odd List: {list[1]}''')
