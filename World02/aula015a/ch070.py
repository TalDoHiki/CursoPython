ct_spt = ct_1000 = low_nm = low_pc = ct =  0
while True:
    ct += 1
    print('{:=^40}'.format(f' {ct}° Product '))
    nm_proct = str(input('Name product: ')).title().strip()
    pc_proct = float(input('Price product: R$'))
    ct_spt += pc_proct
    if pc_proct > 1000:
        ct_1000 += 1
    if ct == 1:
        low_nm = nm_proct
        low_pc = pc_proct
    if low_pc > pc_proct:
        low_nm = nm_proct
        low_pc = pc_proct
    ch = ''
    while ch != 'Y' and ch != 'N':
        ch = str(input('Continue? [Y/N] ')).upper().strip()[0]
    if ch == 'N':
        break
print('-=-'*15)
print(f'''Results:
Total Spent: R${ct_spt:.2f}
Products higher than R$1000: {ct_1000}
Most lower product: {low_nm} / price: R${low_pc:.2f}''')
