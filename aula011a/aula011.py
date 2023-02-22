print('\033[1;44mHello, World!\033[m')
print('\033[7;31;40mHello, World!\033[m')

name = 'Felpe'
print('Hello! Nice to met you, {}{}{}!!!'.format('\033[4;33m',name,'\033[m'))

colors = {
    'clear':'\033[m',
    'white':'\033[30m',
    'red':'\033[31m',
    'green':'\033[32m',
    'yellow':'\033[33m',
    'blue':'\033[34m',
    'purple':'\033[35m',
    'cian':'\033[36m',
    'grey':'\033[37m'
}

nm = str(input('Type your name: ')).title().strip()
fc = str(input('What is your favorite color, {}? '.format(nm.split()[0]))).strip().lower().split()[-1]

print('So you would like your name like this: {}{}{}.'.format(colors[fc],nm.split()[0],colors['clear']))