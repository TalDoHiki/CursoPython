dict = {}
dict['Name'] = str(input('Name: ')).title().strip()
dict['AVG'] = float(input('Average Grade: '))
if dict['AVG'] >=7:
    dict['Status'] = 'APROVED'
elif dict['AVG'] >= 5:
    dict['Status'] = 'RECAP'
else:
    dict['Status'] = 'REPROVED'
for k,v in dict.items():
    print(f'{k}: {v}')
