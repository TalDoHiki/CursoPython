n1 = int(input('Type a number: '))
n2 = int(input('Type other number: '))
s = n1 + n2
m = n1 * n2
d = n1/n2
div = n1//n2
e = n1 ** n2

print('The sum is {}, the product is {} and the div is {:.3f}'.format(s, m, d))
print('Int div is {} and the power {}'.format(div, e))