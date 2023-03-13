from interface import header
from time import sleep

def archiveExist(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def archiveAdd(name):
    try:
        a = open(name, 'wt+')
        a.close
    except:
        print('\033[31mCreating archive error.\033[m')
    else:
        print(f'\033[32mArchive {name} successful created.\033[m')


def archiveRead(name):
    try:
        a = open(name, 'rt')
    except:
        print('\033[31mReading archive error.\033[m')
    else:
        header('PEOPLE REGISTRY')
        for line in a:
            data = line.split(';')
            data[1] = data[1].replace('\n','')
            print(f'{data[0]:<30}{data[1]:>20} years old')


def registry(arc, name='<unknown>', age=0):
    try:
        a = open(arc, 'at')
    except:
        print('\033[31mReading archive error.\033[m')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print('\033[31mWriting archive error.\033[m')
        else:
            print(f'\033[32mNew registry {name} added.\033[m')
            a.close()
