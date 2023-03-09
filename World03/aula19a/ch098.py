from time import sleep
def counter(start,end,step):
    if start > end:
        step = -abs(step)
    if step != 0:
        for c in range(start,end+1,step):
            print(c, end=' -> ')
            sleep(1)
        print('END!')
    else:
        print("You cant count if you don't count, durr.")
counter(1,10,1)
counter(10,0,2)
counter(int(input('Start: ')),int(input('End: ')),int(input('Step: ')))
