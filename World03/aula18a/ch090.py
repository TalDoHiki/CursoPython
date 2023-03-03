dict = {}
dict['Name'] = str(input('Name: ')).title().strip()
dict['AVG'] = float(input('Average Grade: '))
if dict['AVG'] >=7:
    dict['Status'] = 'APROVED'
else:
    dict['Status'] = 'REPROVED'
for k,v in dict.items():
    print(f'{k}: {v}')
    