c50 = c20 = c10 = c1 = 0
print('{:=^40}'.format(' ATM '))
wd_value = int(input('Withdraw value: R$'))
while True:
    if wd_value >= 50:
        c50 += 1
        wd_value -= 50
    elif wd_value >= 20:
        c20 += 1
        wd_value -= 20
    elif wd_value >= 10:
        c10 += 1
        wd_value -= 10
    elif wd_value >= 1:
        c1 += 1
        wd_value -= 1
    elif wd_value == 0:
        break
if c50 > 0:
    print(f'Total of {c50} of R$50.00')
if c20 > 0:
    print(f'Total of {c20} of R$20.00')
if c10 > 0:
    print(f'Total of {c10} of R$10.00')
if c1 > 0:
    print(f'Total of {c1} of RS$1.00')