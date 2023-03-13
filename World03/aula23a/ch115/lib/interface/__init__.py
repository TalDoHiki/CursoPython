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


def lin(wid=60):
    return '-'*wid


def header(txt):
    print(lin())
    print(txt.center(60))
    print(lin())


def menu(list):
    header('MAIN MENU')
    c = 1
    for item in list:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(lin())
    ch = readInt('\033[33mYour choice: \033[m')
    return ch