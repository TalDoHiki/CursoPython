from random import randint

rt = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))
print(f'Numbers generated: {rt}')
print(f'Higher number: {sorted(rt)[-1]}')
print(f'Lower number: {sorted(rt)[0]}')
