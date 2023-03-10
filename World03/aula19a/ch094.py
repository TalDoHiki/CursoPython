person = {}
people = []
ag_ct = 0
while True:
    person['Name'] = str(input('Name: ')).title().strip()
    sx = ''
    sx = str(input('Sex: [M/F] ')).upper().strip().split()[0][0]
    while sx != 'M' and sx != 'F':
        print('[INVALID] Only Male or Female.')
        sx = str(input('Sex: [M/F] ')).upper().strip().split()[0][0]
    person['Sex'] = sx
    person['Age'] = int(input('Age: '))
    ag_ct += person['Age']
    people.append(person.copy())
    person.clear()
    ch = str(input('Continue? [Y/N] ')).upper().strip().split()[0][0]
    while ch not in 'YSN':
        print('[INVALID] Only afirmative or negative')
        ch = str(input('Continue? [Y/N] ')).upper().strip().split()[0][0]
    if ch == 'N':
        break
print('{:=^30}'.format(' Results '))
print(f'A total of {len(people)} people were registered.')
print(f'The age average is {ag_ct/len(people)}')
print("Womans in list:", end=' ')
for w in range(len(people)):
    if people[w]['Sex'] == 'F':
        print(people[w]['Name'], end=', ')
print('-'*10)
print('People that are above the average:')
for pa in range(len(people)):
    if people[pa]['Age'] > (ag_ct/len(people)):
        print(people[pa])
print('-'*10)
print('<< FINISHED >>')
