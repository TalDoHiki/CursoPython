from utility import currency

p = float(input('Type a price: R$'))
print(f"""Result {p}:
Half: {currency.half(p,True)}
Double: {currency.double(p,True)}
10% More: {currency.pctIncrease(p,10,True)}
13% Less: {currency.pctDecrease(p,13,True)}""")
