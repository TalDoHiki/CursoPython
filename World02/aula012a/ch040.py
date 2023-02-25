print('\033[33m-=-\033[m'*30)
n1 = float(input('Type the first grade: '))
n2 = float(input('Type the second grande: '))
avg = (n1 + n2) / 2

print('\033[33m-=-\033[m'*30)
print('Your average grade is : {}{}{}'.format('\033[2m',avg,'\033[m'))
if avg < 5:
    print('\033[31mREPROVED\033[m')
elif avg >= 5 and avg < 7:
    print('\033[33mRETAKE\033[m')
elif avg >= 7:
    print('\033[32mAPROVED\033[m')

print('\033[33m-=-\033[m'*30)
