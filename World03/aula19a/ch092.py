from datetime import datetime

person = {}
person['Name'] = str(input('Name: ')).title().strip()
person['Age'] = datetime.now().year - int(input('Birth Year: '))
person['Work Card'] = int(input('Work Card: '))
if person['Work Card'] == 0:
    print('-=-'*15)
    for k,v in person.items():
       print(f'{k}: {v}')
else:
    person['Contract'] = int(input('Year of contract: '))
    person['Salary:'] = float(input('Salary: R$'))
    print('-=-'*15)
    person['Retariment'] = person['Age'] + ((person['Contract'] + 35) - datetime.now().year)
    for k,v in person.items():
        print(f'{k}: {v}')
        