lexp = []
exp = str(input('Type an expression: ')).replace(' ','')
for c in exp:
    lexp.append(c)
ptv = 0
if '(' in lexp:
    if lexp.count('(') == lexp.count(')'):
        ptv += 1
if ptv == 1:
    print('This expression is valid.')
else:
    print('Expression not valid.')
