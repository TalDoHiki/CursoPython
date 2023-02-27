lunch = ('Hamburger','Juice','Pizza','Pudding','Fries') #Imutable
print(lunch)
print(lunch[0])
print(lunch[-1])
print(lunch[1:3])



for pos, c in enumerate(lunch):
    print(f"I'm gonna eat {c} [Position {pos}]")  #or lunch[cont]
print('I ate a lot.')
