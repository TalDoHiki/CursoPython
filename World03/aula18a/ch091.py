from random import randint
from time import sleep

players = []
player = {}
ct = 0
for pl in range(0,4):
    player['ID'] = pl
    player['Dice'] = randint(1,6)
    print(f'The Player {pl} dice number is {player["Dice"]}')
    if pl == 0:
        players.append(player.copy())
    elif player['Dice'] < players[-1]['Dice']:
        players.append(player.copy())
    elif player['Dice'] > players[0]['Dice']:
        players.insert(0,player.copy())
    else:
        players.insert(1,player.copy())
    sleep(1)
print('{:=^30}'.format(' Result '))
for pl in players:
    ct += 1
    print(f'{ct}° Rank: {pl}')
