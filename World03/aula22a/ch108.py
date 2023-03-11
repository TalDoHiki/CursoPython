from utility import currency

p = float(input('Type a price: R$'))
print(f"""Result R${p:.2f}:
Half: {currency.currencyf(currency.half(p))}
Double: {currency.currencyf(currency.double(p))}
10% More: {currency.currencyf(currency.pctIncrease(p,10))}
13% Less: {currency.currencyf(currency.pctDecrease(p,13))}""")
