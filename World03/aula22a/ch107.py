from utility import numbers
p = float(input('Type a price: R$'))
print(f"""Result R${p}:
Half: R${numbers.half(p)}
Double: R${numbers.double(p)}
10% More: R${numbers.pctIncrease(p,10)}
13% Less: R${numbers.pctDecrease(p,13)}""")
