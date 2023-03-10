list = []
for c in range(1,6):
    n = int(input(f'Value [{c}]: '))
    if c == 1:
        list.append(n)
    elif n in list:
        list.insert(list.index(n),n)
    elif n > max(list):
        list.append(n)
    elif n < min(list):
        list.insert(0,n)
    elif n > min(list) and n < max(list):
        list.insert(list.index(max(list)),n)
print(list)
