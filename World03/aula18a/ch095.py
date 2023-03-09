player = {}
players = []
goals = []
print('{:=^40}'.format(' Football Player List '))
while True:
    player['Name'] = str(input('Name: ')).title().strip()
    player['Match Count'] = int(input('Match played: '))
    if player['Match Count'] != 0:
        for m in range(player['Match Count']):
            goals.append(int(input(f'Match {m+1} goals: ')))
        player['Goals'] = goals.copy()
        goals.clear()
        player['Total Goals'] = sum(player['Goals'])
    else:
        player['Goals'] = [0]
        player['Total Goals'] = 0
    players.append(player.copy())
    player.clear()
    ch = str(input('Continue? [Y/N] ')).upper().strip().split()[0][0]
    print('-'*20)
    if ch == 'N':
        break
print('{:=^60}'.format(' Results '))
print('{:<3}'.format('ID'), '{:<15}'.format('Name'), '{:<15}'.format('Goals'), '{:<3}'.format('Total Goals'))
print('-'*60)
pll = []
for pl in range(len(players)):
    print(f'{pl:<3}',f'{players[pl]["Name"]:<15}','{:<15}'.format('{}'.format(players[pl]["Goals"][:])),f'{players[pl]["Total Goals"]:<3}')
    pll.append(pl)
print('-'*60)
print(pll)
while True:
    chp = int(input('Type the ID for data info: [NEGATIVE ID END THE PROCESS] '))
    if chp < 0:
        break
    elif chp in pll:
        print(f'-- PLAYER {players[chp]["Name"]} DATA:')
        for c in range(len(players[chp]['Goals'])):
            print(f'In the game {c+1} make {players[chp]["Goals"][c]} goals.')
    else:
        print(f'[ERROR] There is no player ID {chp}.')
    print('-'*45)
print('<< PROCESS ENDED >>')
