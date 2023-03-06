from datetime import date

person = {}
person['Name'] = str(input('Name: ')).title().strip()
person['Age'] = date.today().year - int(input('Birth Year: '))
person['Work Card'] = int(input('Work Card: '))
person['Contract'] = int(input('Year of contract: '))
person['Salary:'] = float(input('Salary: R$'))
print('-=-'*15)
if person['Work Card'] == 0:
    person.pop('Work Card','Salary')
    for k,v in person.items():
       print(f'{k}: {v}')
else:
    for k,v in person.items():
        print(f'{k}: {v}')
    print(f'Retirement: {date.today().year - person["Contract"]}')
