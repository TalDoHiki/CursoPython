tb_br = ('Palmeiras','Internacional','Fluminense','Corinthians','Flamengo','Athletico-PR','Atletico-MG','Fortaleza','Sao Paulo','America-MG','Botafogo','Santos','Goias','Bragantino','Coritiba','Cuiaba','Ceara SC','Atletico-GO','Avai','Juventude')

print(f'Five firts classifieds: {tb_br[:5]}.')
print('-=-'*50)
print(f'Four lasts classifieds: {tb_br[-4:]}.')
print('-=-'*50)
print(f'Alphabetic Order: {sorted(tb_br)}.')
print('-=-'*50)
print(f'The Santos is in the {tb_br.index("Santos")+1}° Position.')
