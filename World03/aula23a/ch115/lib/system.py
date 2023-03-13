from interface import *
from archive import *
from time import sleep

arc = 'lib/registry.txt'
if archiveExist(arc) == False:
    archiveAdd(arc)

while True:
    ch = menu(['See registry','New registry','Leave'])
    if ch == 1:
        header('Registry')
        archiveRead(arc)
    elif ch == 2:
        header('New Registry')
        name = str(input('\033[33mName: \033[m')).strip().title()
        age = readInt('\033[33mAge: \033[m')
        registry(arc, name, age)
    elif ch == 3:
        header('\033[35mLeaving the system... Until next time!\033[m')
        print('Credits: GitHub: TalDoHiki')
        sleep(3)
        break
    else:
        print('\033[31m[ERROR] Type a valid option.\033[m')
    sleep(2)
