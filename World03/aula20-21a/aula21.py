# def fact(num=1):
#     f = 1
#     for c in range(num,0,-1):
#         f *= c
#     return f

# f1 = fact(5)
# f2 = fact(4)
# f3 = fact()
# print(f'Results: {f1}, {f2}, {f3}')

def even(n=0):
    if n%2 == 0:
        return True
    else:
        return False
if even(int(input('-> '))) == True:
    print('Even!')
else:
    print('Odd!')