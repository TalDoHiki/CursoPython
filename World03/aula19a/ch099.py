def lin():
    print('-'*30)
def higher(*n):
    print('Analasing the values...')
    print(f'Total of {len(n)} numbers choose, being: {n}')
    print(f'The higher number is {max(n)}.')
lin()
higher(2,5,4,7,6,9,1)
lin()
higher(1,2,)
lin()
higher(4,7,0)
