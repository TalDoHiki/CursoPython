def pyHelp():
    """
    -> Interactive and customized help python function by TalDoHiki
    """
    from time import sleep
    from datetime import datetime
    from colorama import just_fix_windows_console
    just_fix_windows_console()
    print('\033[42m-'*30)
    print('{:^30}'.format('PyHELP HELP SYSTEM'))
    print('-'*30,end='')
    print('\033[m')
    hr = datetime.today().time().hour
    msg = ''
    if hr < 12 and hr >= 00:
        msg = 'Good morning'
    elif hr >=12 and hr < 18:
        msg = 'Good afternoon'
    elif hr >= 18 and hr < 00:
        msg = 'Good evening'
    while True:
        sleep(0.5)
        hp = input(f'{msg}! What can I help you? ').strip()
        sleep(0.5)
        if hp == 'end':
            print('\033[41m-'*15)
            print('{:^15}'.format('GOOD BYE!'))
            print('-'*15,end='')
            print('\033[m')
            print('\033[31mGitHub: \033[33mTalDoHiki\033[m')
            sleep(3)
            break
        print('\033[44m~'*(23+len(hp)))
        print('{:^15}'.format(f'Retrieving {hp} manual data'))
        print('~'*(23+len(hp)),end='')
        print('\033[m')
        sleep(0.5)
        print('\033[45m')
        help(hp)
        print('\033[m')
pyHelp()
