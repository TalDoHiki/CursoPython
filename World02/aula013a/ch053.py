phrase = str(input('Type a phrase: ')).title().strip()
print('Result: {}.'.format(phrase[::-1]))
if phrase.lower().strip().replace(' ','') == phrase.lower().strip().replace(' ','')[::-1]:
    print('{} is a palindrome.'.format(phrase))
else:
    print('{} is not a palindrome.'.format(phrase))
