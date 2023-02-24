phrase = str(input('Type a phrase: ')).lower().strip().replace(' ','')

if phrase == phrase[::-1]:
    print('Is a palindrome.')
else:
    print('Is not a palindrome.')