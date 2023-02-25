rs = float(input('How much do you have in your wallet: R$'))
dl = rs / 5.17
yen = rs / 0.039

print('You can buy: US${:.2f} and {:.0f}JPY.'.format(dl, yen))
