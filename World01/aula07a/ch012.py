n1 = float(input('What is the price of the product? R$'))
ds = float(input('And the discount? '))
np = n1 - (n1*(ds/100))

print('The new price with {} percent of discount is {}'.format(ds,np))
