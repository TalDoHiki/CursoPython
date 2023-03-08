player = {}
scr_permat = []
ts = 0
player['Name'] = str(input('Name: ')).strip().title()
player['Match Count'] = int(input('Match Count: '))
for scr in range(1,player['Match Count']+1):
    scr_permat.append(int(input(f'Goals in match {scr}: ')))
    ts += scr_permat[-1]
player['Goals'] = scr_permat[:]
player['Total goals count'] = ts
print('{:=^30}'.format(' Result '))
for k,v in player.items():
    print(f'{k}: {v}')
print('-=-'*15)
ch = str(input('Specific data: [Y/N] ')).upper().strip().split()[0][0]
if ch == 'Y' or ch == 'YES':
    print('{:=^30}'.format(' Specific Data '))
    print(f'The player {player["Name"]} played {player["Match Count"]} match.')
    for i in range(player['Match Count']):
        print(f'=> In the match {i}, make {player["Goals"][i]} goals.')
    print(f'Total of {player["Total goals count"]}')
