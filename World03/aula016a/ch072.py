nbs = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
ch = -1
while ch not in nbs:
    ch = int(input('Type a integer number between 0 and 20: '))
nbs_e = ('zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty')
print(f'The number {ch} in extence is {nbs_e[ch]}')
