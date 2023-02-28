list = ('Notebook',5600.90,'Smartphone',1500.90,'Sfiha',7.00,'Mensalidade',469,'Husky Bag',209.90)

print('-'*40)
print('{:^40}'.format('Price List'))
print('-'*40)

for c in range(0,len(list),2):
    print('{:.<15}'.format(list[c])+'{:.>15}'.format('R$'),'{:>7.2f}'.format(list[c+1]))
print('-'*40)
