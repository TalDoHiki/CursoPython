def readInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (TypeError,ValueError):
            print('\033[31m[ERROR] Type a valid integer number.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[35mUser preferred to not inform the value.\033[m')
            return 0
        else:
            return n
def readFloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (TypeError,ValueError):
            print('\033[31m[ERROR] Type a valid float number.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[35mUser preferred to not inform the value.\033[m]')
            return 0
        else:
            return n
n1 = readInt('Integer number: ')
n2 = readFloat('Float number: ')
print(f'Numbers typed: Integer: {n1} | Float: {n2}')
